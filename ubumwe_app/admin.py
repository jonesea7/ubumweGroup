from django.contrib import admin

from .models import Member, Contribution, Loan

admin.site.register(Member)
admin.site.register(Contribution)
admin.site.register(Loan)
