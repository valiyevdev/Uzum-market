from django import forms
from backend.models import Narsalar
from django import forms
from backend.models import Narsalar

class MahsulotForm(forms.ModelForm):
    class Meta:
        model = Narsalar
        fields = '__all__'


class MahsulotForm(forms.ModelForm):
    class Meta:
        model = Narsalar
        # Faqat to‘ldirilishi mumkin bo‘lgan maydonlarni tanlaymiz
        fields = [
            'category', 'nomi', 'img', 'asl_narhi', 'nasiya_narhi', 'skid_narhi', 
            'boshqa_uslnarx', 'original', 'is_active', 'is_sotilgan', 'tavsifi', 'sharhlar',
            'bir','ikki','uch','tort','besh','olti','yetti','sakkiz'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'nomi': forms.TextInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'asl_narhi': forms.NumberInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'nasiya_narhi': forms.NumberInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'skid_narhi': forms.NumberInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'boshqa_uslnarx': forms.NumberInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'original': forms.CheckboxInput(attrs={'class': 'mr-2'}),
            'tavsifi': forms.Textarea(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'sharhlar': forms.TextInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'mr-2'}),
            'is_sotilgan': forms.CheckboxInput(attrs={'class': 'mr-2'}),
        }
