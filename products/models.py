from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

# Create a model class
# Go to the settings.py and umder installed apps add the path to the product project
# Type the following command for making migration
#  python manage.py makemigrations
# To manage the migration use the following command
# python manage.py migrate
# Use the sqllite tool to import the db.sqlite3 file
