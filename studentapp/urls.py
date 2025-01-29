
from django.urls import path # type: ignore
from .views import *

urlpatterns = [
    path('home/', home_view,name="home"),
    path('create/',create_view, name="create"),
    path('display/',display_view,name="display"),
    path('register/',register_view,name="register"),
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('delete/<id>/',delete_view),
    path('update/<id>/',update_view), # type: ignore

]
