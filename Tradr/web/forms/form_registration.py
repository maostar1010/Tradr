from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User as defUser
from web.models import User
from django.contrib.auth import authenticate

class UserRegForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'ucalgary email please'}), required=True)
    # phone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Numbers only please'}))

    class Meta:
        model = User
        fields = {'email', 'username', 'password1', 'password2'}

    def __init__(self, *args, **kwargs):
        super(UserRegForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'], self.fields['username'], self.fields['password1'], self.fields['password2']):
            field.widget.attrs.update({'class':'form-control'})
    
    # def clean_email(self):
    #     if self.is_valid():
    #         email = self.cleaned_data['email']
    #         try:
    #             user = User.objects.exclude(pk = self.instance.pk).get(email=email)
    #         except User.DoesNotExist:
    #             return email
    #         raise forms.ValidationError("Email '%s' already in use." %email)
    
    # def clean_username(self):
    #     if self.is_valid():
    #         username = self.cleaned_data['username']
    #         try:
    #             user = User.objects.exclude(pk = self.instance.pk).get(username=username)
    #         except User.DoesNotExit:
    #             return username
    #         raise forms.ValidationError("Username '%s' already in use." %username)

class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'], self.fields['password']):
            field.widget.attrs.update({'class':'form-control'})

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username')
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'], self.fields['username']):
            field.widget.attrs.update({'class':'form-control'})

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = User.objects.exclude(pk = self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' already in use." %email)
    
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                user = User.objects.exclude(pk = self.instance.pk).get(username=username)
            except User.DoesNotExit:
                return username
            raise forms.ValidationError("Username '%s' already in use." %username)


        # def save(self, commit=True):
        #     user = super(UserRegForm, self).save(commit=False)
        #     user.email = self.cleand_data['email']
        #     if commit:
        #         user.save()

        #     return user
    
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
        