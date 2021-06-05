from django.db import models


class Contact(models.Model):

    first_name = models.CharField("first_name", max_length=50)
    last_name = models.CharField("last_name", max_length=50)
    postal_code = models.CharField("postal_code", max_length=50)
    city = models.CharField("city", max_length=50)
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    update_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


