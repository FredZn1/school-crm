from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher


def home(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'index.html', ctx)


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teacher-list.html', ctx)


def teacher_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        telephone_number = request.POST.get('telephone_number')
        work_expert = request.POST.get('work_expert')
        subject_id = request.POST.get('subject')
        image = request.FILES.get('image')

        if all([first_name, last_name, email, telephone_number, work_expert, image]):

            subject = None
            if subject_id:
                subject = subject_id

            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                telephone_number=telephone_number,
                work_expert=work_expert,
                subject_id=subject,
                image=image
            )
            return redirect('teachers:list')
    return render(request, 'teachers/teacher-add.html')


def teacher_update(request, pk):
    teachers = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teachers.first_name = request.POST.get('first_name', teachers.first_name)
        teachers.last_name = request.POST.get('last_name', teachers.last_name)
        teachers.email = request.POST.get('email', teachers.email)
        teachers.telephone_number = request.POST.get('telephone_number', teachers.telephone_number)
        teachers.work_expert = request.POST.get('work_expert', teachers.work_expert)
        subject_id = request.POST.get('subject')


        if subject_id:
            teachers.subject_id = subject_id
        if 'image' in request.FILES:
            teachers.image = request.FILES.get('image')

        teachers.save()
        return redirect(teachers.get_detail_url())
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teacher-add.html', ctx)


def teacher_detail(request, pk):
    teachers = get_object_or_404(Teacher, pk=pk)
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teacher-detail.html', ctx)


def teacher_delete(request, pk):
    teachers = get_object_or_404(Teacher, pk=pk)
    teachers.delete()
    return redirect('teachers:list')
