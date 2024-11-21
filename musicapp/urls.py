from django.urls import path
from . import views

urlpatterns = [
    path('music_list/',views.music_list_view,name='music_list'),
    path('signup/',views.signup,name='signup'),

]
