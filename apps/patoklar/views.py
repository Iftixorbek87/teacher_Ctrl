from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patok
from .forms import PatokForm


@login_required
def dashboard(request):
    patoklar = Patok.objects.filter(oqituvchi=request.user)
    context = {
        'patoklar': patoklar,
        'patoklar_soni': patoklar.count(),
        'jami_talabalar': sum(p.talabalar_soni() for p in patoklar),
        'jami_guruhlar': sum(p.guruhlar_soni() for p in patoklar),
    }
    return render(request, 'base/dashboard.html', context)


@login_required
def patok_list(request):
    q = request.GET.get('q', '').strip()
    patoklar = Patok.objects.filter(oqituvchi=request.user)
    if q:
        patoklar = patoklar.filter(nomi__icontains=q)
    return render(request, 'patoklar/list.html', {'patoklar': patoklar, 'q': q})


@login_required
def patok_create(request):
    if request.method == 'POST':
        form = PatokForm(request.POST)
        if form.is_valid():
            patok = form.save(commit=False)
            patok.oqituvchi = request.user
            patok.save()
            messages.success(request, f"'{patok.nomi}' patogi yaratildi!")
            return redirect('patok_detail', pk=patok.pk)
    else:
        form = PatokForm()
    return render(request, 'patoklar/form.html', {'form': form, 'title': 'Yangi patok'})


@login_required
def patok_detail(request, pk):
    patok = get_object_or_404(Patok, pk=pk, oqituvchi=request.user)
    q = request.GET.get('q', '').strip()
    guruhlar = patok.guruhlar.all()
    if q:
        guruhlar = guruhlar.filter(nomi__icontains=q)
    return render(request, 'patoklar/detail.html', {
        'patok': patok,
        'guruhlar': guruhlar,
        'q': q,
    })


@login_required
def patok_edit(request, pk):
    patok = get_object_or_404(Patok, pk=pk, oqituvchi=request.user)
    if request.method == 'POST':
        form = PatokForm(request.POST, instance=patok)
        if form.is_valid():
            form.save()
            messages.success(request, "Patok yangilandi!")
            return redirect('patok_detail', pk=patok.pk)
    else:
        form = PatokForm(instance=patok)
    return render(request, 'patoklar/form.html', {'form': form, 'title': 'Patokni tahrirlash', 'patok': patok})


@login_required
def patok_delete(request, pk):
    patok = get_object_or_404(Patok, pk=pk, oqituvchi=request.user)
    if request.method == 'POST':
        nomi = patok.nomi
        patok.delete()
        messages.success(request, f"'{nomi}' patogi o'chirildi!")
        return redirect('patok_list')
    return render(request, 'patoklar/confirm_delete.html', {'patok': patok})
