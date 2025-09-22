from django.db import models


class Caruselimg(models.Model):
    img = models.ImageField(upload_to='media/', blank=True, null=True)

class Narsalar(models.Model):
    CATEGORY_CHOICES = [
        ('elektronika', 'Elektronika'),
        ('maishiytexnika', 'Maishiy texnika'),
        ('kiyim', 'Kiyim'),
        ('poyabzallar', 'Poyabzallar'),
        ('aksessuarlar', 'Aksessuarlar'),
        ("gozallikvaparvarish", "Go'zallik va parvarish"),
        ('salomatlik', 'Salomatlik'),
        ("uyrozg`orbuyumlari", "Uy-ro'zg'or buyumlari"),
        ("qurilishvatamirlash", "Qurilish va ta'mirlash"),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='telefon')

    nomi = models.TextField( blank=True, null=True)
    img = models.ImageField(upload_to='media/', blank=True, null=True)  # ✅ rasm majburiy emas
    asl_narhi = models.IntegerField()
    nasiya_narhi = models.IntegerField(default=0)  # ✅ default qo‘shildi
    skid_narhi = models.IntegerField(blank=True, null=True)
    boshqa_uslnarx = models.IntegerField(blank=True, null=True)
    original = models.BooleanField()
    is_sotilgan = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    tavsifi = models.TextField()
    sharhlar = models.CharField(max_length=500)

    bir = models.ImageField(upload_to='media/', blank=True, null=True)
    ikki = models.ImageField(upload_to='media/', blank=True, null=True)
    uch = models.ImageField(upload_to='media/', blank=True, null=True)
    tort = models.ImageField(upload_to='media/', blank=True, null=True)
    besh = models.ImageField(upload_to='media/', blank=True, null=True)
    olti = models.ImageField(upload_to='media/', blank=True, null=True)
    yetti = models.ImageField(upload_to='media/', blank=True, null=True)
    sakkiz = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.tavsifi




class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

