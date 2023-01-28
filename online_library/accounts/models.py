from django.contrib.auth import models as auth_models
from django.core import validators

from django.db import models

from online_library.accounts.validators import validate_only_letters, validate_file_size


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        validators=[validate_file_size, ],
        null=True,
        blank=True,
    )