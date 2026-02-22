from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Guruh
from apps.patoklar.models import Patok
from .forms import GuruhForm


@login_required
def guruh_create(request, patok_pk):
    patok = get_object_or_404(Patok, pk=patok_pk, oqituvchi=request.user)
    if request.method == 'POST':
        form = GuruhForm(request.POST)
        if form.is_valid():
            guruh = form.save(commit=False)
            guruh.patok = patok
            guruh.save()
            messages.success(request, f"'{guruh.nomi}' guruhi yaratildi!")
            return redirect('guruh_detail', pk=guruh.pk)
    else:
        form = GuruhForm()
    return render(request, 'guruhlar/form.html', {
        'form': form, 'patok': patok, 'title': 'Yangi guruh'
    })


@login_required
def guruh_detail(request, pk):
    guruh = get_object_or_404(Guruh, pk=pk, patok__oqituvchi=request.user)
    q = request.GET.get('q', '').strip()
    talabalar = guruh.talabalar.prefetch_related('vazifalar').all()
    if q:
        talabalar = talabalar.filter(ism_familya__icontains=q)

    # Ensure all task records exist for all students
    from apps.talabalar.models import VazifaBajarish
    all_talabalar = guruh.talabalar.all()
    for t in all_talabalar:
        existing = set(t.vazifalar.values_list('vazifa_raqam', flat=True))
        new_records = [
            VazifaBajarish(talaba=t, vazifa_raqam=i, bajarildi=False)
            for i in range(1, guruh.jami_vazifalar + 1)
            if i not in existing
        ]
        if new_records:
            VazifaBajarish.objects.bulk_create(new_records)

    # Re-fetch with fresh data
    talabalar = guruh.talabalar.prefetch_related('vazifalar').all()
    if q:
        talabalar = talabalar.filter(ism_familya__icontains=q)

    return render(request, 'guruhlar/detail.html', {
        'guruh': guruh,
        'talabalar': talabalar,
        'q': q,
        'task_range': range(1, guruh.jami_vazifalar + 1),
        'jami': guruh.jami_vazifalar,
    })


@login_required
def guruh_edit(request, pk):
    guruh = get_object_or_404(Guruh, pk=pk, patok__oqituvchi=request.user)
    if request.method == 'POST':
        form = GuruhForm(request.POST, instance=guruh)
        if form.is_valid():
            form.save()
            messages.success(request, "Guruh yangilandi!")
            return redirect('guruh_detail', pk=guruh.pk)
    else:
        form = GuruhForm(instance=guruh)
    return render(request, 'guruhlar/form.html', {
        'form': form, 'patok': guruh.patok, 'guruh': guruh, 'title': 'Guruhni tahrirlash'
    })


@login_required
def guruh_delete(request, pk):
    guruh = get_object_or_404(Guruh, pk=pk, patok__oqituvchi=request.user)
    if request.method == 'POST':
        patok_pk = guruh.patok.pk
        nomi = guruh.nomi
        guruh.delete()
        messages.success(request, f"'{nomi}' guruhi o'chirildi!")
        return redirect('patok_detail', pk=patok_pk)
    return render(request, 'guruhlar/confirm_delete.html', {'guruh': guruh})


@login_required
@require_POST
def guruh_vazifa_soni(request, pk):
    guruh = get_object_or_404(Guruh, pk=pk, patok__oqituvchi=request.user)
    try:
        yangi_son = int(request.POST.get('jami_vazifalar', guruh.jami_vazifalar))
        if yangi_son < 1:
            yangi_son = 1
        if yangi_son > 500:
            yangi_son = 500

        eski_son = guruh.jami_vazifalar
        guruh.jami_vazifalar = yangi_son
        guruh.save()

        # Add new task records if count increased
        if yangi_son > eski_son:
            from apps.talabalar.models import Talaba, VazifaBajarish
            for talaba in guruh.talabalar.all():
                existing = set(talaba.vazifalar.values_list('vazifa_raqam', flat=True))
                new_records = [
                    VazifaBajarish(talaba=talaba, vazifa_raqam=i, bajarildi=False)
                    for i in range(eski_son + 1, yangi_son + 1)
                    if i not in existing
                ]
                if new_records:
                    VazifaBajarish.objects.bulk_create(new_records)

        messages.success(request, f"Vazifalar soni {yangi_son} ga o'zgartirildi!")
    except (ValueError, TypeError):
        messages.error(request, "Noto'g'ri son kiritildi!")

    return redirect('guruh_detail', pk=pk)
