from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser, Connection
from django.contrib.gis import forms
from .widgets import CustomOpenLayersWidget

class CustomUserChangeForm(UserChangeForm):
    location = forms.PointField(widget=forms.OSMWidget(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}))
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'home_address', 'location')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-3', 'autocomplete': 'off'})
            if field == 'location':
                self.fields[field].widget.attrs.update({'id':'map'})

    def as_bootstrap(self):
        return self._html_output(
            normal_row='<div class="row mb-3"><div class="col-sm-3 col-form-label">%s</div><div class="col-sm-9">%s</div></div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html='<div class="form-text">%s</div>',
            errors_on_separate_row=True,
        )

class ConnectionForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(label='Your Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com'}))
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message'}))

    class Meta:
        model = Connection
        fields = ('name', 'email', 'subject', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-3', 'autocomplete': 'off'})
           