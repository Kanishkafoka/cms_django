# cms_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminViewSet, AuthorViewSet, home,register_user,login_user
from .views import success_page,logout_user,search


router = DefaultRouter()
router.register(r'users', AdminViewSet)
router.register(r'content-items', AuthorViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('search/', search, name='search'),

    path('success/', success_page, name='success_page'),
    path('register/', register_user, name='register_user'),

    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    




]
