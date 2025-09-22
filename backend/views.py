from django.shortcuts import render
from .models import Narsalar
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .models import Narsalar, Caruselimg

def home(request):
    narsalar = Narsalar.objects.all()
    caruselimg = Caruselimg.objects.all()   
    return render(request, 'home.html', {'narsalar': narsalar, 'caruselimg': caruselimg})

def detail(request, detail_id):
    narsalar = get_object_or_404(Narsalar, id = detail_id)    
    return render(request, 'detail.html', {'narsalar': narsalar})

def search_detail(request):
    query = request.GET.get('q', "")
    product = Narsalar.objects.all()
    
    if query:
        product = product.filter(nomi__icontains=query)   

    context = {
        'query': query,
        'product': product
    }
    return render(request, 'search_detail.html', context)
    



def haftaliktavarlar(request):
    narsalar = Narsalar.objects.all()
    return render(request, 'haftaliktavarlar.html', {'narsalar': narsalar})

def savat(request):
    return render(request, 'savat.html')

def savol(request):
    return render(request, 'savoljavob.html')

def sotuvchi_bolish(request):
    return render(request, 'sotuvchi_bolish.html')

def rasmiylashtirish(request):
    return render(request, 'rasmiylashtirish.html')

def saralangan(request):
    narsalar = Narsalar.objects.all()
    return render(request, 'saralangan.html', {'narsalar': narsalar})


def katalog(request):
    return render(request, 'katalog.html')

def punkt(request):
    return render(request, 'punkt.html')

def maxfiylik_kelishuvi(request):
    return render(request, 'maxfiylikk.html')

from django.shortcuts import render
from .models import Narsalar

def narsalar_list(request, category):
    # Asosiy filtr - kategoriya
    narsalar = Narsalar.objects.filter(category=category)
    
    # Kategoriya nomini modeldagi tanlangan qiymat bo'yicha olish
    category_choices = dict(Narsalar.CATEGORY_CHOICES)
    category_display = category_choices.get(category, category)
    
    # Narx filtri
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if min_price:
        narsalar = narsalar.filter(skid_narhi__gte=min_price)
    if max_price:
        narsalar = narsalar.filter(skid_narhi__lte=max_price)
    
    # Original mahsulot filtri
    original = request.GET.get('original')
    if original:
        narsalar = narsalar.filter(original=True)
    
    return render(request, 'category.html', {
        'narsalar': narsalar,
        'category': category,
        'category_display': category_display,
        'min_price': min_price,
        'max_price': max_price,
        'original': original,
        'product_count': narsalar.count(),
    })



from django.conf import settings
from django.utils import translation
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def change_language(request):
    if request.method == 'POST':
        lang = request.POST.get('language', 'uz')
        translation.activate(lang)
        response = redirect(f'/{lang}/')
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
        return response

