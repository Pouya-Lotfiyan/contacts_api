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
        return self.first_name




class PhoneNumber(models.Model):

    class PhoneNumberType(models.TextChoices):
        MOBILE = 'MO'
        HOME = 'HO'

    number = models.CharField("number", max_length=10)
    type = models.CharField(
    max_length=2,
    choices=PhoneNumberType.choices,
    default=PhoneNumberType.HOME,
    )
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, db_constraint=True, related_name='phoneNumbers')
