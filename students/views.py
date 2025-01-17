from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from groups.models import Group


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student-list.html', ctx)


def student_create(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group_id = request.POST.get('group')  # Guruhni olish
        date_of_birth = request.POST.get('date_of_birth')
        telephone_number = request.POST.get('telephone_number')
        address = request.POST.get('address')
        image = request.FILES.get('image')

        # Guruhni tekshirish: ixtiyoriy
        group = None
        if group_id:
            group = get_object_or_404(Group, pk=group_id)

        # Tekshiruvdan "group_id" ni olib tashladik
        if all([first_name, last_name, date_of_birth, telephone_number, address, image]):
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
    ctx = {'groups': groups}
    return render(request, 'students/student-add.html', ctx)


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    groups = Group.objects.all()
    if request.method == 'POST':
        student.first_name = request.POST.get('first_name', student.first_name)
        student.last_name = request.POST.get('last_name', student.last_name)

        group_id = request.POST.get('group')

        if group_id:
            student.group = get_object_or_404(Group, pk=group_id)
        else:
            student.group = None

        student.date_of_birth = request.POST.get('date_of_birth', student.date_of_birth)
        student.telephone_number = request.POST.get('telephone_number', student.telephone_number)
        student.address = request.POST.get('address', student.address)
        if 'image' in request.FILES:
            student.image = request.FILES.get('image')
        student.save()
        return redirect(student.get_detail_url())
    ctx = {'students': student, 'groups': groups}
    return render(request, 'students/student-add.html', ctx)


def student_detail(request, pk):
    students = get_object_or_404(Student, pk=pk)
    ctx = {'students': students}
    return render(request, 'students/student-detail.html', ctx)


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:list')
