from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

# Create your models here.
GENDER_CHOICES = (
    ('f', 'female'),
    ('m', 'male'),
    ('r', 'rather not say ')
)

CATEGORY_CHOICES = (
    ('d', 'Doctor'),
    ('p', 'Patient'),
    ('r', 'Receptionist'),
    ('a', 'Admin'),
    ('s', 'Staff'),
)


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, default="India")
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=7)
    soft_delete = models.BooleanField(default=False)
    cr_by = models.ForeignKey(
        'User', on_delete=models.RESTRICT, related_name="clinic_cr_by",
        null=True, blank=True
    )
    up_by = models.ForeignKey(
        'User', on_delete=models.RESTRICT, related_name="clinic_up_by",
        null=True, blank=True
    )

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(
        AbstractBaseUser,
        PermissionsMixin
):
    clinic = models.ForeignKey(
        Clinic, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, blank=True)
    email = models.EmailField(
        verbose_name='email address', unique=True
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(
        upload_to="user_images", null=True, blank=True
    )
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, default="m"
    )

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    manager = models.BooleanField(default=False)  # a superuser
    username = None

    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="p"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    soft_delete = models.BooleanField(default=False)
    cr_by = models.ForeignKey(
        'User', on_delete=models.RESTRICT, related_name="user_cr_by",
        null=True, blank=True
    )
    up_by = models.ForeignKey(
        'User', on_delete=models.RESTRICT, related_name="user_up_by",
        null=True, blank=True
    )

    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_manager(self):
        "Is the user a member of manager?"
        return self.manager

    @property
    def category_name(self):
        "Is the user has a category?"
        return self.category.name if self.category else ""


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, default="India")
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=7)
    soft_delete = models.BooleanField(default=False)
    cr_by = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name="address_cr_by", null=True, blank=True)
    up_by = models.ForeignKey(User, on_delete=models.RESTRICT,
                              related_name="address_up_by", null=True, blank=True)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}"

    @property
    def full_add(self):
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}"

    class Meta:
        verbose_name_plural = 'Addresses'
