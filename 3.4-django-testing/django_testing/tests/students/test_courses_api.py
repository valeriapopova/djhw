import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course

from students.filters import CourseFilter


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_first_course(client, course_factory):
    course = course_factory(_quantity=1)
    first_course = course[0]

    response = client.get(f"/api/v1/courses/{first_course.id}/")

    assert response.status_code == 200
    assert response.data['name'] == first_course.name


@pytest.mark.django_db
def test_all_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    assert len(response.data) == len(courses)


@pytest.mark.django_db
def test_filter(client, course_factory):
    courses = course_factory(_quantity=5)
    course = CourseFilter(data={'id': courses[0].id})

    response = client.get('/api/v1/courses/', data={'id': courses[0].id})

    assert response.status_code == 200
    assert response.data[0]['id'] == course.data['id']


@pytest.mark.django_db
def test_name(client, course_factory):
    courses = course_factory(_quantity=30)
    course = CourseFilter(data={'name': courses[1].name})

    response = client.get('/api/v1/courses/', data={'name': courses[1].name})

    assert response.status_code == 200
    assert response.data[0]['name'] == course.data['name']


@pytest.mark.django_db
def test_new_course(client, student_factory):
    count = Course.objects.count()
    student = student_factory(_quantity=1)

    response = client.post('/api/v1/courses/', data={'name': 'new курс', 'students': student[0].id})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update(client, course_factory):
    course = course_factory(_quantity=1)
    update_data = {'name': 'python разработчик с нуля'}

    response = client.patch(f'/api/v1/courses/{course[0].id}/', update_data)

    assert response.status_code == 200
    assert response.data['name'] == update_data['name']


@pytest.mark.django_db
def test_delete(client, course_factory):
    count = Course.objects.count()
    course = course_factory(_quantity=1)

    response = client.delete(f'/api/v1/courses/{course[0].id}/')

    assert response.status_code == 204
    assert Course.objects.count() == count


@pytest.mark.parametrize("num_students, code", [(20, 201), (21, 400)])
@pytest.mark.django_db
def test_limit(client, course_factory, student_factory, num_students, code, settings):
    settings.MAX_STUDENTS_PER_COURSE = 20
    students = student_factory(_quantity=num_students)
    students_id = [student.id for student in students]
    course = course_factory(_quantity=1)

    response = client.post('/api/v1/courses/', data={'name': course[0].name, 'students': students_id})

    assert response.status_code == code
    assert settings.MAX_STUDENTS_PER_COURSE
