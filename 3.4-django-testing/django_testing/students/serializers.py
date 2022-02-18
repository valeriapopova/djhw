from rest_framework import serializers

from students.models import Course

from django_testing import settings


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, value):
        if settings.MAX_STUDENTS_PER_COURSE < len(value):
            raise serializers.ValidationError('превышено максимальное число студентов на курсе(20)')
        return value
