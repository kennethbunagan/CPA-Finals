from django.conf.urls import url
from . import  views

app_name = 'foods'

urlpatterns = [
    #foods homepage #http://127.0.0.1:8000/foods/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/foods/1/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/foods/product/add/
    url(r'product/add/$', views.ProductCreate.as_view(), name='product-add'),
    #/foods/product/pk/
    url(r'product/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name='product-update'),
    #/foods/product/pk/delete/
    url(r'product/(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name='product-delete'),

    #/foods/productdetails/add/
    url(r'productdetails/add/$', views.ProductDetailsCreate.as_view(), name='productdetails-add'),
    #/foods/productdetails/pk/
    url(r'productdetails/(?P<pk>[0-9]+)/$', views.ProductDetailsUpdate.as_view(), name='productdetails-update'),
    #/foods/productdetails/pk/delete
    url(r'productdetails/(?P<pk>[0-9]+)/delete/$', views.ProductDetailsDelete.as_view(), name='productdetails-delete'),
]