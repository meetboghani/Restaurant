from django.contrib import admin
from .models import Gallery
from .models import Chef
from .models import testimonal,Party,SpecialItem,Menus1
# Register your models here.

admin.site.register(Gallery)
admin.site.register(Chef)
admin.site.register(testimonal)
admin.site.register(Party)
admin.site.register(SpecialItem)
admin.site.register(Menus1)
