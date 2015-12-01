from django.forms import ModelForm
from sla_app.models import Company

class CompanyForm(ModelForm):
    class Meta:
        model=Company
        fields=['name','service']