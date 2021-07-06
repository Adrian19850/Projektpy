from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from zaliczeniepy.views import wszystkie_filmy, nowy_film, edytuj_film, usun_film
from django.contrib.auth import views as auth_views

from rest_framework import routers
from zaliczeniepy.views import UserView, FilmView

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'filmy', FilmView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wszystkie/', wszystkie_filmy, name="wszystkie_filmy"),
    path('nowy/', nowy_film, name="nowy_film"),
    path('edytuj/<int:id>/', edytuj_film, name="edytuj_film"),
    path('usun/<int:id>/', usun_film,  name="usun_film"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('', include(router.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
