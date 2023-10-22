from django.db import models


#Create your models here.
class Ingredients(models.Model):
    in_name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=200, default="")
    in_price = models.FloatField(default=0.0)

    def __str__(self):
        return f"""
        name={self.in_name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.in_price}
        """


class MenuItem(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.FloatField(default=0)

    def __str__(self):
        return f"title={self.item_name}; price={self.item_price}"


class RecipeRequirements(models.Model):
    item_name = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    in_name = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"menu_item={self.item_name.item_name}; ingredients={self.in_name.in_name}; qty={self.quantity}"


class PurchaseLog(models.Model):
    item_name = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"menu_item=[{self.item_name.__str__()}]; time={self.timestamp}"

    def get_absolute_url(self):
        return "purchase_log/"