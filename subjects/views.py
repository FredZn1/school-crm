from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject

def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subject-list.html', ctx)

def subject_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Subject.objects.create(name=name)
            return redirect('subjects:list')
    return render(request, 'subjects/subject-add.html')

def subject_update(request, pk):
    subjects = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            subjects.name = name
            subjects.save()
            return redirect(subjects.get_detail_url())
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subject-add.html', ctx)

def subject_detail(request, pk):
    subjects = get_object_or_404(Subject, pk=pk)
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subject-detail.html', ctx)

def subject_delete(request, pk):
    subjects = get_object_or_404(Subject, pk=pk)
    subjects.delete()
    return redirect('subjects:list')
