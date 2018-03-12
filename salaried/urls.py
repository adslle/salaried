from django.urls import path,re_path
from . import views


urlpatterns = [
    path('',views.index,name='salaried.index'),
    path('<int:id>',views.show,name='salaried.show'),
    path('create',views.create,name='salaried.create'),
    path('update/<int:id>',views.update,name='salaried.update'),
    path('delete/<int:id>',views.delete,name='salaried.delete'),
    path('<int:salaried_id>/documents/delete/<int:document_id>',views.delete_document,name='salaried.documents.delete'),
    path('<int:salaried_id>/documents/create',views.create_document,name='salaried.documents.create'),
    path('<int:salaried_id>/documents/update/<int:document_id>',views.update_document,name='salaried.documents.update'),
]

