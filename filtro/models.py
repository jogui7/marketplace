from django.db import models

# Create your models here.
class Anuncio (models.Model):

    CONDITION = (
        ('novo','Novo'),
        ('usado','Usado')
    )

    CATEGORY = (
        ('romance','romance'),
        ('ficcao','ficcao'),
        ('autoajuda', 'autoajuda'),
        ('didatico', 'didatico'),
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    shortDescription = models.TextField(max_length=200)
    price = models.FloatField()
    condition = models.CharField(
        max_length = 10,
        choices = CONDITION,
    )
    category = models.CharField(
        max_length = 10,
        choices = CATEGORY,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

