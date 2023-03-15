from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, MultiField, Div

class UserRegForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'ucalgary email please'}), required=True)
    phone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Numbers only please'}))

    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'username', 'phone', 'email', 'password1', 'password2'}

        def save(self, commit=True):
            user = super(UserRegForm, self).save(commit=False)
            user.email = self.cleand_data['email']
            if commit:
                user.save()

            return user
    
        # def __init__(self, *args, **kwargs):
        #     super(UserRegForm, self).__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.layout = Layout(
        #         MultiField(
        #             Div(
        #             'username',
        #             ),
        #             Div(
        #             'first_name',
        #             'last_name',
        #             ),
        #             Div(
        #             'email',
        #             'phone',
        #             ),
        #             Div(
        #             'password1',
        #             'password2',
        #             )
        #         )
        # #     Row(
        # #         Column('username', css_class='form-group col-md-3 mb-0 input'),
        # #         Column('email', css_class='form-group col-md-3 mb-0 input'),
        # #         Column('password2', css_class='form-group col-md-3 mb-0 input'),
        # #         Column('password1', css_class='form-group col-md-3 mb-0 input'),
        # #         Column('phone', css_class='form-group col-md-3 mb-0 input'),
        # #         Column('first_name', css_class='form-group col-md-3 mb-0 input'),
        # #         Column('last_name', css_class='form-group col-md-3 mb-0 input'),
        # #         css_class='form-row'
        # #     )
        #     )
            
        #     return self
        