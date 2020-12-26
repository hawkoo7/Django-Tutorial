from django.urls import path
from DjangoAppTwo import views

app_name='DjangoAppTwo'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('other/',views.other,name='other'),
    path('user_login/',views.user_login,name='user_login'),
]
