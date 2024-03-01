from django.contrib import admin
from hospitallapp.models import users,product,Member,Message

# Register your models here.
admin.site.register(users)
admin.site.register(product)
admin.site.register(Member)
admin.site.register(Message)

