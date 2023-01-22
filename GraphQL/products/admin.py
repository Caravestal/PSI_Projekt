from django.contrib import admin
from .models import Nauczyciele, Lekcje, LekcjeNauczycieli
# Register your models here.

admin.site.register(Nauczyciele)
admin.site.register(Lekcje)
admin.site.register(LekcjeNauczycieli)