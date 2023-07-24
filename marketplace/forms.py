from django import forms
# from .models import Product, Category
from .models import Product

class ProductForm(forms.ModelForm):
    # カテゴリーの選択肢をカスタマイズ
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)

    class Meta:
        model = Product
        # fields = ('name', 'description', 'price', 'category', 'image')
        fields = ('name', 'description', 'price', 'image')
