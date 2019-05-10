"""
Instructor file API endpoint
"""
# pylint: disable=import-error
from __future__ import absolute_import, unicode_literals

import hashlib

import six
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import CourseAccessRole
from student.roles import CourseStaffRole


class ReportView(APIView):
    """API endpoint to control access to CSV export files"""

    permission_classes = (IsAuthenticated,)

    # pylint: disable=unused-argument
    def get(self, request, version, course_sha1, filename):
        """
        API endpoint that control access to instructors CSV export files,
        then redirects to Nginx.
        Users requesting access to a CSV file sould be superuser or
        belong to course staff.
        """

        # Retrieve all courses for which user is staff and compare their sha1 to
        # the requested one.
        if not request.user.is_superuser:
            courses = CourseAccessRole.objects.filter(
                user=request.user, role=CourseStaffRole.ROLE
            )
            for course in courses:
                hashed_course_id = hashlib.sha1(
                    six.text_type(course.course_id)
                ).hexdigest()
                if hashed_course_id == course_sha1:
                    break
            else:
                # None matches, user does not have rights to request this file
                return Response({}, status=status.HTTP_403_FORBIDDEN)

        # Redirect browser to an internal Nginx location
        response = Response({})
        response["Content-Disposition"] = "attachment; filename={0}".format(filename)
        response["X-Accel-Redirect"] = "/restricted/{course_sha1}/{filename}".format(
            course_sha1=course_sha1, filename=filename
        )
        return response
