from django.db import models

# Product model
class Product(models.Model):
    id = models.AutoField
    productName = models.CharField(max_length=60)
    productDescription = models.CharField(max_length=250)

    price = models.DecimalField(max_digits=5, decimal_places=2)

    # currency
    tk = 'taka'
    rp = 'rupe'
    Currency = [
        (tk, 'taka'),
        (rp, 'rupe')
    ]
    currency = models.CharField(max_length=6, choices=Currency, default=tk,)

    madeDate = models.DateField()
    expireDate = models.DateField()

    # stock_status
    IS = 'In stock'
    OS = 'Out of stock'
    Status_Of_Product = [
        (IS, 'In stock'),
        (OS, 'Out of stock'),
    ]

    status_of_product = models.CharField(
        max_length=15,
        choices=Status_Of_Product,
        default=IS,
    )

    view = models.IntegerField(default=0)

    # adding the name of product instade of deafult products object(value)
    def __str__(self):
        return self.productName
