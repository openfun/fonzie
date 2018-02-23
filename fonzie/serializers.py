from rest_framework.serializers import ModelSerializer

from openedx.student.models import Student


class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
