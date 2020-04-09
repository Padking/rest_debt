from django.db import models


class Debtor(models.Model):
    debtor_name = models.CharField(max_length=255)
    debt_amount = models.CharField(max_length=255)

    def __str__(self):
        return self.name
