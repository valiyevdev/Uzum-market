from django.shortcuts import render
from backend.models import Narsalar
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .forms import MahsulotForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def dashboard(request):
    users = User.objects.all()
    total_users = users.count()
    latest_user = users[:10]
    items = Narsalar.objects.all()
    total_items = items.count()
    sotilganlar = Narsalar.objects.filter(is_sotilgan=True)
    sotilganlar_soni= sotilganlar.count()
    data = (
        Narsalar.objects
        .values('category')
        .annotate(total=Count('id'))
        .order_by('category')
    )

    # Grafik uchun alohida ro‘yxatlar
    labels = []
    values = []
    for item in data:
        labels.append(dict(Narsalar.CATEGORY_CHOICES)[item['category']])  # nomini olish
        values.append(item['total'])  # sonini olish

    if request.method == 'POST':
        form = MahsulotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mahsulotlar')  # refresh qilinganda yangilanadi
    else:
        form = MahsulotForm()

    context = {
        'labels': labels,
        'values': values,
        'total_users': total_users,
        'latest_user': latest_user,
        'users': users,
        'items': items, 
        'total_items': total_items,
        'sotilganlar': sotilganlar,
        'form': form,
        'sotilganlar_soni': sotilganlar_soni
    }
 
    return render(request, 'dashboard.html', context,)

def sotuvlar_api(request):
    try:
        days = int(request.GET.get("days", 7))
        today = timezone.now().date()
        start_date = today - timedelta(days=days-1)

        # Bazadan mavjud kunlar bo‘yicha sotuvlar
        db_data = (
            Narsalar.objects.filter(
                created_at__date__gte=start_date,
                is_sotilgan=True
            )
            .values('created_at__date')
            .annotate(total=Count('id'))
            .order_by('created_at__date')
        )

        # Dict qilib olamiz (sana: miqdor)
        sales_dict = {
            item['created_at__date']: item['total'] for item in db_data
        }

        # Hamma kunlar bo‘yicha ro‘yxat yaratamiz
        labels = []
        values = []

        for i in range(days):
            day = start_date + timedelta(days=i)
            labels.append(day.strftime('%Y-%m-%d'))
            values.append(sales_dict.get(day, 0))  # Agar sotuv yo‘q bo‘lsa, 0

        return JsonResponse({"labels": labels, "data": values})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Donut chart — kategoriya bo'yicha sotuvlar
def kategoriya_api(request):
    data = (
        Narsalar.objects.filter(is_sotilgan=True)
        .values('category')
        .annotate(total=Count('id'))
        .order_by('category')
    )

    labels = [dict(Narsalar.CATEGORY_CHOICES)[item['category']] for item in data]
    values = [item['total'] for item in data]

    return JsonResponse({"labels": labels, "data": values})

def mahsulotlar(request):
    items = Narsalar.objects.all()  # doimo QuerySet bo'lishi kerak
    total_items = items.count()
    faol_mahsulotlar = items.filter(is_active=True)
    nofaol_mahsulotlar = items.filter(is_active=False)

    if request.method == 'POST':
        mahsulot_id = request.POST.get('mahsulot_id')
        if mahsulot_id:
            mahsulot = get_object_or_404(Narsalar, id=mahsulot_id)
            form = MahsulotForm(request.POST, request.FILES, instance=mahsulot)
        else:
            form = MahsulotForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('mahsulotlar')  # <-- bu juda muhim
    else:
        form = MahsulotForm()


    context = {
        'items': items,  # doimo iterable bo'ladi
        'form': form,
        'total_items': total_items,
        'faol_mahsulotlar': faol_mahsulotlar,
        'nofaol_mahsulotlar': nofaol_mahsulotlar,
    }
    return render(request, 'mahsulotlar.html', context)


def mahsulot_json(request, id):

    mahsulot = get_object_or_404(Narsalar, id=id)
    return JsonResponse({
        'id': mahsulot.id,
        'category': mahsulot.category,
        'nomi': mahsulot.nomi,
        'asl_narhi': mahsulot.asl_narhi,
        'nasiya_narhi': mahsulot.nasiya_narhi,
        'skid_narhi': mahsulot.skid_narhi,
        'boshqa_uslnarx': mahsulot.boshqa_uslnarx,
        'original': mahsulot.original,
        'is_sotilgan': mahsulot.is_sotilgan,
        'is_active': mahsulot.is_active,
        'tavsifi': mahsulot.tavsifi,
        'sharhlar': mahsulot.sharhlar,
    })

@csrf_exempt
def mahsulot_ochirish(request, id):
    if request.method == 'POST':
        mahsulot = get_object_or_404(Narsalar, id=id)
        mahsulot.delete()
        return redirect('mahsulotlar')  # sahifaga qaytarish
    return redirect('mahsulotlar')


def buyurtmalar(request):
    users = User.objects.all()
    total_users = users.count()
    latest_user = users[:10]
    return render(request, 'buyurtmalar.html', {'users': users, 'total_users': total_users, 'latest_user': latest_user})


def mijozlar(request):
    users = User.objects.all()
    total_users = users.count()
    latest_user = users[:10]
    return render(request, 'mijozlar.html', {'users': users, 'total_users': total_users, 'latest_user': latest_user})

def hisobotlar(request):
    return render(request, 'hisobotlar.html')

def adminnav(request):
    return render(request, 'adminnav.html')

def adminbars(request):
    return render(request, 'adminbars.html')
