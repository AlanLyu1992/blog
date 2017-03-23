from django.contrib import admin
from blogpost.models import Blogpost
from blogpost.models import Person
class BlogpostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class PersonAdmin(admin.ModelAdmin):
	pass
admin.site.register(Blogpost, BlogpostAdmin)
admin.site.register(Person, PersonAdmin)
# Register your models here.
