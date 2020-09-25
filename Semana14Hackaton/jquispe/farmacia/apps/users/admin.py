from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'first_name', 'last_name','last_login')
	serach_fields = ('username', 'email')
	list_filter=('is_superuser',)
	ordering = ('username',)
	filter_horizontal = ("groups", "user_permissions")
	


	fieldsets = (
		('User', {'fields' : ('username', 'password')}),
		('Persona Info' , {'fields' : ('first_name',
						'last_name',
						'email',
						'avatar'
						)}),
		('Permissions' , {'fields' : ('is_active',
						'is_staff',
						'is_superuser',
						'groups',
						'user_permissions')}),
		)


