from django.db import models
from py_expression_eval import Parser

class Article(models.Model):
    name = models.CharField(null=False, max_length=200, unique=True)
    description = models.CharField(null=True, max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)


class ArticleAttribute(models.Model):
    name = models.CharField(null=False, max_length=200)
    description = models.CharField(null=True, max_length=2000)
    target_article = models.OneToOneField(Article, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    max_value = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    min_value = models.DecimalField(null=True, max_digits=10, decimal_places=2)

class CostParam(models.Model):
    name = models.CharField(null=False, max_length=200)
    description = models.CharField(null=True, max_length=2000)
    positive_contrib = models.BooleanField(null=False)
    target_article = models.OneToOneField(Article, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    max_value = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    min_value = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    # weightage = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    depreciation_curve = models.CharField(null=False, max_length=2000)

    def get_pure_depreciation_contribution(self):
        par = Parser()
        equation = self.depreciation_curve.trim()
        return par.parse(equation).evaluate({'x': self.target_attribute.value})

    def get_depreciation_contribution(self):
        pure_dep = self.get_pure_depreciation_contribution()
        dep_con = pure_dep
        if pure_dep > self.max_value:
            dep_con = self.max_value
        elif pure_dep < self.min_value:
            dep_con = self.min_value
        return dep_con * self.weightage
