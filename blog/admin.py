from django.contrib import admin

# Register your models here.
from .form import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__string__", "timestamp", "update"]
    form = SignUpForm
    # class Meta:
    #     model = SignUp

admin.site.register(SignUp, SignUpAdmin)