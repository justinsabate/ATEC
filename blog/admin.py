from django.contrib import admin
from .models import Post

admin.site.register(Post) ## pour que notre modèle soit visible dans l'interface admin