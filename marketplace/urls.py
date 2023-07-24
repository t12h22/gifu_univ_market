from django.urls import path
from . import views

urlpatterns = [
    # 商品一覧ページのURLパターン
    path('', views.product_list, name='product_list'),
    
    # 商品詳細ページのURLパターン
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # 商品登録用のURLパターンを追加
    path('product/create/', views.product_create, name='product_create'),

    path('product/<int:product_id>/delete/', views.delete_product, name='product_delete'),
]
