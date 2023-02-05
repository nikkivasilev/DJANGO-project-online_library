from django.contrib.auth import get_user_model
from django.db import models

from online_library.accounts.validators import validate_file_size

UserModel = get_user_model()

class Book(models.Model):
    TITLE_MAX_LENGTH = 75
    TYPE_MAX_LENGTH = 75
    DESCRIPTION_MAX_LENGTH = 355

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        null=True,
        blank=True,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )
    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    def __str__(self):
        return f'{self.title} - {self.type}'
