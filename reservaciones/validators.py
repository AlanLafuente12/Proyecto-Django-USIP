from django.core.exceptions import ValidationError

def validar_par (value):
    if value % 2 != 0:
        # %( )s para poner un valor
        raise ValidationError("%(value)s no es un numero par", params={'value':value})
    
def validar_categoria (value):
    if value == 'No permitido':
        # %( )s para poner un valor
        raise ValidationError("No es una opcion permitida")
    
    
def validar_nombre(value):
    if value == "Comida":
        raise ValidationError('%(value)s no es un texto permitido', params={'value': value})