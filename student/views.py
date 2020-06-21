from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import StudentForm
from .models import Student

#分离get，post的处理逻辑

class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students =Student.get_all()
        context = {
            'students':students,
        }
        return context

    def get(self,request):
        context = self.get_context()
        form =StudentForm()
        context.update({
            'form':form
        })
        return render(request,self.template_name,context=context)

    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form':form
        })
        return render(request,self.template_name,context=context)

    def test_get_index(self):
        #测试首页的可用性
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code,200,'status code must be 200!')
    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_post',
            sex=1,
            email='333@dd.com',
            profession="程序员",
            qq='3333',
            phone = '3222',
        )
        response = client.post('/',data)
        self.assertEqual(response.status_code,302,'status code must be 302!')

        response = client.get('/')
        self.assertTure(b'test_for_post' in response.content,
                        'response content must contain "test_for_post"')
# def index(request):
#     # words = 'World!'
#     #return render(request, 'index.html', context={"words":words})
#     students = Student.get_all()
#     #students = Student.objects_all()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             # cleaned_data = form.cleaned_data
#             # student = Student()
#             # student.name = cleaned_data['name']
#             # student.sex = cleaned_data['sex']
#             # student.email = cleaned_data['profession']
#             # student.qq = cleaned_data['qq']
#             # student.phone = cleaned_data['phone']
#             form.save()
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         form = StudentForm()
#
#     context = {
#           'students': students,
#           'form': form,
#         }
#   return render(request, "index.html", context=context)