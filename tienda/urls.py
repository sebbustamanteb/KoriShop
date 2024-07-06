from django.urls import path
from . import views
from .views import consulta_list_view, consulta_create_view, consulta_update_view, consulta_delete_view


urlpatterns = [
    path('', views.index, name='index'),
    path('peluches/', views.peluches, name='peluches'),
    path('almohadas/', views.almohadas, name='almohadas'),
    path('donaciones/', views.donaciones, name='donaciones'),
    path('pago/', views.pago, name='pago'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('consultas/', views.consultas, name='consultas'),
    path('form_consultas/', views.form_consulta_view, name='form_consultas'),
    path('consultas/', consulta_list_view, name='consulta_list'),
    path('consultas/nueva/', consulta_create_view, name='consulta_create'),
    path('consultas/editar/<int:pk>/', consulta_update_view, name='consulta_update'),
    path('consultas/eliminar/<int:pk>/', consulta_delete_view, name='consulta_delete'),

]