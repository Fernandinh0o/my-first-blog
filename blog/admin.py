from django.contrib import admin
from .models import Post, Product  # Asegúrate de que Product esté definido en models.py

admin.site.register(Post)
admin.site.register(Product)