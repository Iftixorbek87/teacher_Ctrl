from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student, TaskCompletion
from apps.groups.models import Group
from .forms import StudentForm


@login_required
def student_add(request, group_pk):
    group = get_object_or_404(Group, pk=group_pk, teacher=request.user)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.group = group
            student.save()
            # Create task completions
            for task_num in range(1, group.total_tasks + 1):
                TaskCompletion.objects.get_or_create(
                    student=student,
                    task_number=task_num,
                    defaults={'completed': False}
                )
            messages.success(request, f"'{student.full_name}' ro'yxatga qo'shildi!")
            return redirect('group_detail', pk=group.pk)
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form, 'group': group, 'title': "O'quvchi qo'shish"})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk, group__teacher=request.user)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "O'quvchi ma'lumotlari yangilandi!")
            return redirect('group_detail', pk=student.group.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/form.html', {'form': form, 'group': student.group, 'student': student, 'title': "O'quvchini tahrirlash"})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk, group__teacher=request.user)
    group_pk = student.group.pk
    if request.method == 'POST':
        name = student.full_name
        student.delete()
        messages.success(request, f"'{name}' ro'yxatdan o'chirildi!")
        return redirect('group_detail', pk=group_pk)
    return render(request, 'students/confirm_delete.html', {'student': student})


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk, group__teacher=request.user)
    tasks = student.task_completions.all().order_by('task_number')
    context = {
        'student': student,
        'tasks': tasks,
        'completed': student.completed_tasks_count(),
        'total': student.group.total_tasks,
        'progress': student.progress_percent(),
    }
    return render(request, 'students/detail.html', context)


@login_required
@require_POST
def toggle_task(request):
    """AJAX endpoint to toggle task completion"""
    try:
        data = json.loads(request.body)
        student_id = data.get('student_id')
        task_number = data.get('task_number')
        
        student = get_object_or_404(Student, pk=student_id, group__teacher=request.user)
        task, _ = TaskCompletion.objects.get_or_create(
            student=student,
            task_number=task_number,
            defaults={'completed': False}
        )
        task.completed = not task.completed
        if task.completed:
            from django.utils import timezone
            task.completed_at = timezone.now()
        else:
            task.completed_at = None
        task.save()
        
        return JsonResponse({
            'success': True,
            'completed': task.completed,
            'completed_count': student.completed_tasks_count(),
            'total': student.group.total_tasks,
            'progress': student.progress_percent(),
            'is_graduated': student.is_graduated(),
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
