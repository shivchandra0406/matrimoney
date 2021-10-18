from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations=True
    def create(self,mobilenumber,password=None,**extra_fields):
        if mobilenumber:
            user=self.model(mobilenumber=mobilenumber,**extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        else:
            raise ValueError('Mobile number is required')
    def create_superuser(self,mobilenumber,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff is true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user have is_superuser is true')
        return self.create(mobilenumber,password,**extra_fields)