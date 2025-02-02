from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm


# def home(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         password = request.POST['password']
#         photo = request.FILES.get('photo')
#         checkbox = request.POST['checkbox']
#         if checkbox == 'on':
#             checkbox = True
#         else:
#             checkbox = False
#         student = Student(name=name, email=email, phone=phone, password=password, checkbox=checkbox, photo=photo)
#         student.save()
#         print(photo)
#         return render(request,'student/home.html')

#     return render(request, 'student/home.html')


def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'student/index.html', {'form': form})

def list_view(request):
    students = Student.objects.all()
    return render(request,'student/student_list.html', {'students': students})

def individual_information(request, id):
    student = Student.objects.get(id=id)
    context = {
       'student': student
    }
    return render(request, 'student/individual_student.html', context)

# def update_student(request, id):
#     student = get_object_or_404(Student, id=id)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         student = Student.objects.get(id=id)
#         context = {'form': student}
#         return render(request, 'student/update.html', context)
def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'student/index.html', {'form': form, 'update': True})
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')
