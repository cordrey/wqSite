
from django.contrib import admin
from .models import Tjros
from django.conf.locale.en import formats as en_formats

en_formats.DATETIME_FORMAT = "Y-m-d H:i"

#TODO: add search

admin.site.register(Tjros)
