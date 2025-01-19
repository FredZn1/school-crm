from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from groups.models import Group


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student-list.html', ctx)


def student_create(request):
    groups = Group.objects.all()
    error = None

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group_id = request.POST.get('group')
        date_of_birth = request.POST.get('date_of_birth')
        telephone_number = request.POST.get('telephone_number')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        group = None


        if group_id and group_id.isdigit():
            group = get_object_or_404(Group, pk=group_id)
        elif group_id:
            error = 'Guruh identifikatori noto‘g‘ri formatda yuborildi.'


        if not error and all([first_name, last_name,
                              date_of_birth, telephone_number,
                              address, image]):
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                group=group,
                date_of_birth=date_of_birth,
                telephone_number=telephone_number,
                address=address,
                image=image
            )
            return redirect('students:list')
        else:
            error = error or 'Iltimos, barcha maydonlarni to‘ldiring.'

    ctx = {'groups': groups, 'error': error}
    return render(request, 'students/student-add.html', ctx)


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    groups = Group.objects.all()
    error = None
    if request.method == 'POST':
        student.first_name = request.POST.get('first_name', student.first_name)
        student.last_name = request.POST.get('last_name', student.last_name)
        group_id = request.POST.get('group')
        if group_id and group_id.isdigit():
            student.group = get_object_or_404(Group, pk=group_id)
        elif group_id:
            error = 'Guruh identifikatori noto‘g‘ri formatda yuborildi.'
        else:
            student.group = None
        student.date_of_birth = request.POST.get('date_of_birth', student.date_of_birth)
        student.telephone_number = request.POST.get('telephone_number', student.telephone_number)
        student.address = request.POST.get('address', student.address)
        if 'image' in request.FILES:
            student.image = request.FILES.get('image')

        if not error:
            student.save()
            return redirect(student.get_detail_url())

    ctx = {'students': student, 'groups': groups, 'error': error}
    return render(request, 'students/student-add.html', ctx)


def student_detail(request, pk):
    students = get_object_or_404(Student, pk=pk)
    ctx = {'students': students}
    return render(request, 'students/student-detail.html', ctx)


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:list')
