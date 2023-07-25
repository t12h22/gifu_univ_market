from django.urls import path
from . import views

urlpatterns = [
    # 商品一覧ページのURLパターン
    path('', views.product_list, name='product_list'),
    
    # 商品詳細ページのURLパターン
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # 商品登録ページのURLパターン
    path('product/create/', views.product_create, name='product_create'),

    # 商品削除ページのURLパターン
    path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
]
