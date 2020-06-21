from django.test import TestCase, Client

from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='the5fire',
            sex=1,
            email='nobody@fire.com',
            profession='程序员',
            qq='3333',
            phone='2222',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@yu.com',
            profession='程序汪',
            qq='3366',
            phone='111',
        )
        self.assertEqual(student.sex_show,'男','性别字段内容跟展示不一致!')

    def test_filter(self):
        Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@yu.com',
            profession='程序汪',
            qq='3366',
            phone='111',
        )
        name = 'huyang',
        students =Student.objects.filter(name=name)
        self.assertEqual(students.count(),0,
                         '应该只存在一个名称为{}的记录'.format(name))