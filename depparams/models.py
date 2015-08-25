from django.db import models


class Article(models.Model):
    name = models.CharField(null=False, max_length=200)
    actual_first_sale_amount = models.DecimalField(null=False)
    average_first_sale_amount = models.DecimalField(null=False)
    months_since_first_sale = models.IntegerField(null=False)
    

class DepParam(models.Model):
    name = models.CharField(null=False, max_length=200)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    max_value = models.DecimalField(null=False)
    min_value = models.DecimalField(null=False)
    weightage = models.DecimalField(null=False)
    # depreciation_curve = ?? #TODO: Need to find a way to define and use algebraic curves entered by the user
