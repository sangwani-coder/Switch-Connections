from django.db import models

class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Service categories"

    def __str__(self):
        return self.category_name


class ServiceListings(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.CharField(max_length=100)
    service_price = models.CharField(max_length=10)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Service listings"

    def __str__(self):
        return self.service_name
