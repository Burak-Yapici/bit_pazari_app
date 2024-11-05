from django.db import models
from django.contrib.auth.models import User

class product(models.Model):  # Model adını büyük harfle başlatmak yaygın bir isimlendirme kuralıdır
    sallername = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    productname = models.CharField(max_length=50)
    productinfo = models.CharField(max_length=250)
    image = models.ImageField(upload_to='product_images/')  # Resim yükleme yolu

    def __str__(self):
        return f"SATICININ ADI : {self.username} ÜRÜN ADI: {self.productname} ÜRÜN BİLGİSİ: {self.productinfo}"
    


