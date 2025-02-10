from django import forms
from django.contrib.gis.forms import PointField
from leaflet.forms.widgets import LeafletWidget
from .models import NotablePlace

class NotablePlaceForm(forms.ModelForm):
    coordinates = PointField(widget=LeafletWidget())

    class Meta:
        model = NotablePlace
        fields = '__all__'
    
class UploadFileForm(forms.Form):
    file = forms.FileField()