from django.contrib import admin

import models

admin.site.register(models.Group)
admin.site.register(models.Artist)
admin.site.register(models.Album)
admin.site.register(models.Song)