from rest_framework.generics import ListAPIView

from openedx.student.models import Student
from ..serializers import StudentSerializer


class StudentListAPIView(ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
