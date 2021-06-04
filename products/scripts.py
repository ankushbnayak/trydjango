from products.models import Product

obj=Product.objects.get
print(obj.__name__)