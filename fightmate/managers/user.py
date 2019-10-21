from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):

	def create_user(self, email, first_name, password, is_staff=False, is_admin=False, is_superuser=False):
		user_obj = self.model.objects.create(
			email=email,
			first_name=first_name,
			is_staff=is_staff,
			is_admin=is_admin,
			is_superuser=is_superuser
		)
		
		user_obj.set_password(password)

		user_obj.save()

		return user_obj

	def create_superuser(self, email, first_name, password):
		user = self.create_user(
			email=email,
			first_name=first_name,
			password=password,
			is_admin=True,
			is_staff=True,
			is_superuser=True
		)
