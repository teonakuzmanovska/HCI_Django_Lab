from django import forms
# from django.contrib.auth.models import User

from .models import UserModel, Publication, BlockedUsers


class UserForm(forms.ModelForm):
    # za da se prati odma so klasa "form-control"
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        # model = User
        # model = UserModel
        model = BlockedUsers
        exclude = ("user",)


class PublicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublicationForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Publication
        exclude = ("user",)
