from django.db import models

# Create your models here.
class Operator(models.Model):
      name = models.CharField(max_length=120)
      address1 = models.CharField(max_length=200)
      numDogs = models.IntegerField()
      numCats = models.IntegerField()
      completed = models.BooleanField(default=False)

      def _str_(self):
        return self.name