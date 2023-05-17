from django import forms
from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        models = Image
        fields = ('title', 'url', 'description')
        widgets = {'url': forms.HiddenInput,}

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extension = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extension:
            raise forms.ValidationError('The given URL does not ' \
                                        'match valid image extensions.'
                                        )
        return url