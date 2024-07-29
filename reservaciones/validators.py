from django.core.exceptions import ValidationError
import re

def validar_texto (value):
    for i in value:
        if i in '0123456789':
            raise ValidationError("No se permiten números en este campo")
    
def validar_numero (value):
    if re.match('^[0-9.]+$', value) == False:
        raise ValidationError("Solo se permiten números y signos de puntuación en este campo")
