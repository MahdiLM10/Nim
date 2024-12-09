from django.urls import path 
from . import views


urlpatterns = [
    path('add/',views.cart_add,name='cart_add'),
    path('delete/',views.cart_delete,name='cart_delete'),
    path('',views.cart_summary,name='cart_summary'),
    path('ShopVerify/',views.shopverify,name='shopverify'),
    path('Form/',views.fill_form,name='fillform'),
    path('create_order/',views.create_order_view, name='create_order'),
    # path('update/',views.cart_update,name='cart_update'),
    # path('color/',views.color_add,name='color_add'),

]
