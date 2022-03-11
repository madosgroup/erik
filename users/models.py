import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from rooms.models import Room
class ContactInformation(models.Model):
    email = models.CharField(max_length =100)
    phone = models.CharField(max_length =100)


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_FRENCH = "fr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_FRENCH, "French"))

    CURRENCY_USD = "usd"
    CURRENCY_BR = "BRF"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_BR, "BRF"))

    LOGIN_EMAIL = 'email'
    LOGIN_GITHUB = 'github'
    LOGIN_FACEBOOK = 'facebook'
    LOGIN_TWITTER = 'twitter'
    LOGIN_GOOGLE = 'google'
    LOGIN_KAKAO = 'kakao'

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, 'Email'),
        (LOGIN_GITHUB, 'Github'),
        (LOGIN_KAKAO, 'Kakao'),
    )

    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True, upload_to='avatars')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_FRENCH)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_BR)
    host = models.BooleanField(default=False) #Rename this to IS_Publisher
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, blank=True, default="")
    login_method = models.CharField(max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL)
    contact = models.ForeignKey("ContactInformation", on_delete=models.CASCADE, related_name="ContactInformation",null=1,blank=1)
    like = models.ManyToManyField(Room,related_name='Liked',default=None,blank=True)
    # likes = models.ForeignKey(Room,related_name='Liking',default=None,blank=True,null=True,on_delete=models.CASCADE)
    objects = UserManager()

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if not self.email_verified:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string("emails/verify_email.html", context={"secret": secret})
            send_mail(
                "Verify Mados Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message
            )
            self.save()
        return




