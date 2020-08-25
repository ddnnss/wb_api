from django.contrib import admin
from .models import *

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(BlackListType)
admin.site.register(BlackListItem)
# Register your models here.
