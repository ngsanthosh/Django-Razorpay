from django.db import models
#This model is used to store the customer credentials who has successfully made a payement.

class ColdCoffee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return (self.name+" - Rs."+str(int(self.amount)/100))
