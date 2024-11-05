from django import forms
from .models import product  # Product modelinizi buradan içe aktardığınızdan emin olun
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class AddProductForm(forms.ModelForm):
    class Meta:
        model = product  # Kullanacağınız model
        fields = ['sallername', 'productname', 'productinfo', 'image']  # Formda yer alacak alanlar

        # Opsiyonel: İsteğe bağlı olarak form alanları için widget'lar belirtebilirsiniz
        widgets = {
            'productname': forms.TextInput(attrs={'placeholder': 'Ürün Adını Girin'}),
            'productinfo': forms.Textarea(attrs={'placeholder': 'Ürün Bilgilerini Girin'}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),  # Çoklu resim yüklemeyi devre dışı bırakma
        }



User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # E-posta alanını ekleyin

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # E-posta alanını dahil edin

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # E-postayı kaydet
        if commit:
            user.save()
        return user


