from django.db import models

# Create your models here.

class Lista(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nome}"
    
    def total(self):
        return sum(item.preco for item in self.app_set.all())

    total.short_description = "Total"

  


class App(models.Model):
    compra = models.CharField(max_length=64)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID:{self.id} Preço:{self.preco}  Produto:{self.compra} Lista:{self.lista} "

