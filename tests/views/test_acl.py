# -*- coding: utf-8 -*-
"""
Tests for the `fonzie` acl module.
"""
# pylint: disable=no-member,import-error
from __future__ import absolute_import, unicode_literals

import hashlib

import six
from rest_framework import status
from rest_framework.test import APITestCase

from django.core.urlresolvers import reverse

from student.roles import CourseStaffRole
from student.tests.factories import UserFactory
from xmodule.modulestore import ModuleStoreEnum
from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase
from xmodule.modulestore.tests.factories import CourseFactory


class ReportViewTestCase(ModuleStoreTestCase, APITestCase):
    """Tests for the InstructorFilesView API endpoint"""

    def setUp(self):
        """
        Set common parameters for unit tests.
        """
        super(ReportViewTestCase, self).setUp()

        # this file format is used for student profiles
        self.filename = "fun_test_00_student_profile_info_2019-04-19-1406.csv"
        self.course = CourseFactory.create(default_store=ModuleStoreEnum.Type.split)
        self.course_staff = UserFactory(
            username="course_staff", email="course_staff@fun-mooc.fr"
        )
        CourseStaffRole(self.course.id).add_users(self.course_staff)
        self.course_sha1 = hashlib.sha1(six.text_type(self.course.id)).hexdigest()

        self.url = reverse(
            "fonzie:acl:report",
            kwargs={
                "version": "1.0",
                "course_sha1": self.course_sha1,
                "filename": self.filename,
            },
        )

    def test_user_is_not_logged_in(self):
        """
        User should be logged in, if not the view should return 403
        """
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_is_not_staff(self):
        """
        User should not be a just student, if so the view should return 403
        """
        normal_user = UserFactory(
            username="normal_user", email="normal_user@fun-mooc.fr"
        )
        self.client.force_authenticate(normal_user)
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_is_staff_on_other_course(self):
        """
        User should belong to this course staff, if not the view should return 403
        """
        course = CourseFactory.create(default_store=ModuleStoreEnum.Type.split)
        other_course_staff = UserFactory(
            username="other_course_staff", email="other_course_staff@fun-mooc.fr"
        )
        CourseStaffRole(course.id).add_users(other_course_staff)
        self.client.force_authenticate(other_course_staff)
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_has_correct_rights(self):
        """
        User fullfils all conditions, then he should be redirected to Nginx
        """
        self.client.force_authenticate(self.course_staff)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.get("X-Accel-Redirect"),
            "/restricted/%s/%s" % (self.course_sha1, self.filename),
        )
        self.assertEqual(
            response.get("Content-Disposition"),
            "attachment; filename=%s" % self.filename,
        )

    def test_user_can_download_problem_response(self):
        """
        User fullfils all conditions and downloads a problem response file,
        he should be redirected to Nginx
        """
        # this file format is used by problem responses files
        filename = (
            "edX_DemoX_Demo_Course_student_state_from_block-v1_edX+DemoX"
            "+Demo_Course+type@problem+block@d1b84dcd39b0423d9e288f27f0f7f242_"
            "2019-10-09-1219.csv"
        )
        url = reverse(
            "fonzie:acl:report",
            kwargs={
                "version": "1.0",
                "course_sha1": self.course_sha1,
                "filename": filename,
            },
        )

        self.client.force_authenticate(self.course_staff)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.get("X-Accel-Redirect"),
            "/restricted/%s/%s" % (self.course_sha1, filename),
        )
        self.assertEqual(
            response.get("Content-Disposition"),
            "attachment; filename=%s" % filename,
        )

    def test_user_has_correct_rights_old_course_id_format(self):
        """
        Ensure endpoint also works with legacy course id format
        (org.1/course_1/Run_1 against course-v1:org.1+course_1+Run_1)
        """
        course = CourseFactory.create()  # create a course with old course_id format
        CourseStaffRole(course.id).add_users(self.course_staff)
        course_id = six.text_type(course.id)
        self.client.force_authenticate(self.course_staff)
        url = reverse(
            "fonzie:acl:report",
            kwargs={
                "version": "1.0",
                "course_sha1": hashlib.sha1(course_id).hexdigest(),
                "filename": self.filename,
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.get("X-Accel-Redirect"),
            "/restricted/%s/%s"
            % (hashlib.sha1(six.text_type(course_id)).hexdigest(), self.filename),
        )

    def test_user_is_superuser(self):
        """
        Super users should always get requested file.
        """
        super_user = UserFactory(
            username="super_user",
            email="super_user@fun-mooc.fr",
            is_superuser=True
        )
        self.client.force_authenticate(super_user)
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.get("X-Accel-Redirect"),
            "/restricted/%s/%s" % (self.course_sha1, self.filename),
        )
        self.assertEqual(
            response.get("Content-Disposition"),
            "attachment; filename=%s" % self.filename,
        )
