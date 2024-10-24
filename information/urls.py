from django.urls import path
from . import views

urlpatterns=[
path("",views.index, name="index"),
path('get_value/',views.get_value, name='get_value'),
path('get_value/save_data',views.save_data, name='save_data'),
]