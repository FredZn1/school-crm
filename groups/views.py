from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from teachers.models import Teacher

def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/group-list.html', ctx)

def group_create(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        teacher_id = request.POST.get('teacher')


        teacher = None
        if teacher_id:
            teacher = get_object_or_404(Teacher, pk=teacher_id)

        if group_name:
            Group.objects.create(
                group_name=group_name,
                teacher=teacher  )
            return redirect('groups:list')
    ctx = {'teachers': teachers}
    return render(request, 'groups/group-add.html', ctx)

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        group.group_name = request.POST.get('group_name', group.group_name)

        teacher_id = request.POST.get('teacher')
        if teacher_id:
            group.teacher = get_object_or_404(Teacher, pk=teacher_id)
        else:
            group.teacher = None
        group.save()
        return redirect('groups:detail', pk=group.pk)
    ctx = {'group': group, 'teachers': teachers}
    return render(request, 'groups/group-add.html', ctx)

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'groups/group-detail.html', ctx)

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups:list')
