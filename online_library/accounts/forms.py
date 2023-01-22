from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class EditUserForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name',)
        field_classes = {'username': auth_forms.UsernameField}


class CreateUserForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email')
