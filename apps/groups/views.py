from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Group
from .forms import GroupForm


@login_required
def dashboard(request):
    groups = Group.objects.filter(teacher=request.user)
    total_students = sum(g.get_student_count() for g in groups)
    context = {
        'groups': groups,
        'total_students': total_students,
        'total_groups': groups.count(),
    }
    return render(request, 'base/dashboard.html', context)


@login_required
def group_list(request):
    groups = Group.objects.filter(teacher=request.user)
    
    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        groups = groups.filter(name__icontains=search_query)
    
    return render(request, 'groups/list.html', {
        'groups': groups,
        'search_query': search_query
    })


@login_required
def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.teacher = request.user
            group.save()
            messages.success(request, f"'{group.name}' guruhi muvaffaqiyatli yaratildi!")
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm()
    return render(request, 'groups/form.html', {'form': form, 'title': 'Yangi guruh yaratish'})


@login_required
def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk, teacher=request.user)
    students = group.students.all()
    
    # Handle search
    search_query = request.GET.get('q', '')
    if search_query:
        students = students.filter(full_name__icontains=search_query)
    
    # Initialize task completions for all students
    from apps.students.models import TaskCompletion
    for student in students:
        for task_num in range(1, group.total_tasks + 1):
            TaskCompletion.objects.get_or_create(
                student=student,
                task_number=task_num,
                defaults={'completed': False}
            )
    
    # Refresh students data with search filter applied
    students = students.prefetch_related('task_completions').all()
    
    context = {
        'group': group,
        'students': students,
        'task_range': range(1, group.total_tasks + 1),
        'total_tasks': group.total_tasks,
        'search_query': search_query,
    }
    return render(request, 'groups/detail.html', context)


@login_required
def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk, teacher=request.user)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, "Guruh muvaffaqiyatli yangilandi!")
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm(instance=group)
    return render(request, 'groups/form.html', {'form': form, 'title': 'Guruhni tahrirlash', 'group': group})


@login_required
def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk, teacher=request.user)
    if request.method == 'POST':
        name = group.name
        group.delete()
        messages.success(request, f"'{name}' guruhi o'chirildi!")
        return redirect('group_list')
    return render(request, 'groups/confirm_delete.html', {'group': group})
