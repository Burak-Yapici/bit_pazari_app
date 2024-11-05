from django.shortcuts import render, redirect
from . import models
from django.urls import reverse,reverse_lazy 
from django.http import HttpResponse
from .forms import AddProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django .views.generic import CreateView
from .forms import CustomUserCreationForm


# Create your views here.

def showcase(request):
    all_product = models.product.objects.all()  # Burada Product modelinizi doğru bir şekilde kullandığınızdan emin olun
    
    product_dict = {"products": all_product,
                    "username": request.user.username
                    }
    return render(request, 'bit_pazari_app/showcase.html', context=product_dict)

@login_required(login_url="/login")
def addproduct(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)  # request.FILES ile dosyaları alıyoruz
        if form.is_valid():
            form.save()  # Formu doğrudan kaydediyoruz
            return redirect(reverse('bit_pazari_app:showcase'))
        else:
            print("error in form")
            return render(request, 'bit_pazari_app/addproduct.html', context={"form": form})
    else:
        form = AddProductForm()
        return render(request, 'bit_pazari_app/addproduct.html', context={"form": form})

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Kullanıcıyı giriş yapmış olarak ayarlama
            return redirect('home')  # Kayıt sonrası yönlendirme
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

    

class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # UserCreationForm yerine CustomUserCreationForm kullan
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Kullanıcıyı otomatik olarak giriş yaptır
        return super().form_valid(form)
