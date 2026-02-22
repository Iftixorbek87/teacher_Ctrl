import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Talaba, VazifaBajarish
from apps.guruhlar.models import Guruh
from .forms import TalabaForm


@login_required
def talaba_add(request, guruh_pk):
    guruh = get_object_or_404(Guruh, pk=guruh_pk, patok__oqituvchi=request.user)
    if request.method == 'POST':
        form = TalabaForm(request.POST)
        if form.is_valid():
            talaba = form.save(commit=False)
            talaba.guruh = guruh
            talaba.save()
            # Bulk create task records
            vazifalar = [
                VazifaBajarish(talaba=talaba, vazifa_raqam=i, bajarildi=False)
                for i in range(1, guruh.jami_vazifalar + 1)
            ]
            VazifaBajarish.objects.bulk_create(vazifalar)
            messages.success(request, f"'{talaba.ism_familya}' ro'yxatga qo'shildi!")
            return redirect('guruh_detail', pk=guruh.pk)
    else:
        form = TalabaForm()
    return render(request, 'talabalar/form.html', {
        'form': form, 'guruh': guruh, 'title': "O'quvchi qo'shish"
    })


@login_required
def talaba_edit(request, pk):
    talaba = get_object_or_404(Talaba, pk=pk, guruh__patok__oqituvchi=request.user)
    if request.method == 'POST':
        form = TalabaForm(request.POST, instance=talaba)
        if form.is_valid():
            form.save()
            messages.success(request, "O'quvchi ma'lumotlari yangilandi!")
            return redirect('guruh_detail', pk=talaba.guruh.pk)
    else:
        form = TalabaForm(instance=talaba)
    return render(request, 'talabalar/form.html', {
        'form': form, 'guruh': talaba.guruh, 'talaba': talaba, 'title': "O'quvchini tahrirlash"
    })


@login_required
def talaba_delete(request, pk):
    talaba = get_object_or_404(Talaba, pk=pk, guruh__patok__oqituvchi=request.user)
    guruh_pk = talaba.guruh.pk
    if request.method == 'POST':
        nomi = talaba.ism_familya
        talaba.delete()
        messages.success(request, f"'{nomi}' ro'yxatdan o'chirildi!")
        return redirect('guruh_detail', pk=guruh_pk)
    return render(request, 'talabalar/confirm_delete.html', {'talaba': talaba})


@login_required
def talaba_detail(request, pk):
    talaba = get_object_or_404(Talaba, pk=pk, guruh__patok__oqituvchi=request.user)
    vazifalar = talaba.vazifalar.all()
    return render(request, 'talabalar/detail.html', {
        'talaba': talaba,
        'vazifalar': vazifalar,
        'bajarilgan': talaba.bajarilgan_soni(),
        'jami': talaba.guruh.jami_vazifalar,
        'foiz': talaba.foiz(),
    })


@login_required
@require_POST
def vazifa_toggle(request):
    try:
        data = json.loads(request.body)
        talaba_id = data.get('talaba_id')
        vazifa_raqam = data.get('vazifa_raqam')

        talaba = get_object_or_404(Talaba, pk=talaba_id, guruh__patok__oqituvchi=request.user)
        vazifa, _ = VazifaBajarish.objects.get_or_create(
            talaba=talaba, vazifa_raqam=vazifa_raqam,
            defaults={'bajarildi': False}
        )
        vazifa.bajarildi = not vazifa.bajarildi
        if vazifa.bajarildi:
            from django.utils import timezone
            vazifa.vaqt = timezone.now()
        else:
            vazifa.vaqt = None
        vazifa.save()

        return JsonResponse({
            'success': True,
            'bajarildi': vazifa.bajarildi,
            'bajarilgan': talaba.bajarilgan_soni(),
            'jami': talaba.guruh.jami_vazifalar,
            'foiz': talaba.foiz(),
            'bitirdi': talaba.bitirdimi(),
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
