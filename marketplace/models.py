from django.db import models
from django.conf import settings
import os

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

#     class Meta:
#         app_label = 'marketplace'

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # 画像ファイルの削除
        if self.image:
            # ファイルのフルパスを取得
            file_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
            # ファイルを削除
            if os.path.exists(file_path):
                os.remove(file_path)
        super(Product, self).delete(*args, **kwargs)