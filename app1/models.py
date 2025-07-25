from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class product(TimeStampedModel):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    valid_time = models.DateTimeField()

    def __str__(self):
        return self.name


class costumer(TimeStampedModel):
    name = models.CharField(max_length=255)
    addres = models.TextField()
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name


class orders(TimeStampedModel):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    costumer = models.ForeignKey(costumer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    requared_date = models.DateTimeField()
    shipped_date = models.DateTimeField()

    def __str__(self):
        return f"{self.product} - {self.costumer}"
