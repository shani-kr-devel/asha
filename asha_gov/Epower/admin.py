from django.contrib import admin
from .models import Epower,UserReview,shope,UserProfile
# Register your models here.
class ReviewInline(admin.TabularInline):
    model=UserReview
    extra=2
class Epdata(admin.ModelAdmin):
    list_display=('name','type','date')
    inlines=[ReviewInline]

class storeadmin(admin.ModelAdmin):
    list_display=('user','epower')

class userP_admin(admin.ModelAdmin):
    list_display=('user','address')


admin.site.register(Epower)
admin.site.register(UserReview,storeadmin)
admin.site.register(shope)
admin.site.register(UserProfile,userP_admin)



