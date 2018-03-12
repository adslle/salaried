from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='bu.index'),
    path('<int:id>',views.show,name='bu.show'),
    path('create',views.create,name='bu.create'),
    path('update/<int:id>',views.update,name='bu.update'),
    path('delete/<int:id>',views.delete,name='bu.delete'),
]