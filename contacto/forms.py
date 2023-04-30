from django import forms
from django.forms import ValidationError
import requests, json

def chkEmail(email):
    url = 'https://emailvalidation.abstractapi.com/v1/'
    api_key = 'f796c4051157457f929760de818e88dc'
    try:
        response = requests.get(url + '/?api_key=' + api_key + '&email=' + email)
        res = json.loads(response.content)
        if (res['deliverability'] == 'DELIVERABLE'):
            return(True)
        else:
             raise ValidationError('Correo electrónico inválido')
        return(False)
    except requests.exceptions.RequestException as api_error:
        return(False)
    
class FormularioContacto(forms.Form):
	nombre = forms.CharField(label="Nombre", required=True)
	email = forms.CharField(label="Email", required=True, validators=(chkEmail,))
	contenido = forms.CharField(label="Contenido", widget=forms.Textarea)
