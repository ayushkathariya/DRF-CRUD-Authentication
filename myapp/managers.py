from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")

        # Normalize the email address
        email = self.normalize_email(email)

        # Create a new user instance
        user = self.model(email=email, **extra_fields)

        # Set the password for the user
        user.set_password(password)

        # Save the user object into the database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        # Create a user with the provided email and password
        user = self.create_user(email, password, **extra_fields)

        # Set the is_staff and is_superuser flags to True
        user.is_staff = True
        user.is_superuser = True

        # Save the user object into the database
        user.save(using=self._db)

        return user
