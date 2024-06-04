from django import forms


class UploadFileForm(forms.Form):
    nama = forms.CharField(max_length=50)
    data_file = forms.FileField()
