from django import forms

class LoadData(forms.Form):
    query = forms.CharField(label='query', max_length=100, required=False)
    limit = forms.IntegerField(label="limit", min_value=0, max_value=100, required=False)

