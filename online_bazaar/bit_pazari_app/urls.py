from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from . import views  # views'i içe aktarıyoruz
from .forms import CustomUserCreationForm, AddProductForm 


app_name ='bit_pazari_app'

urlpatterns = [
    path('',views.showcase,name='showcase'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('register/', views.user_register, name='register'),

   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

