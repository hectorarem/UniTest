from django.utils.deconstruct import deconstructible
from django.core.validators import BaseValidator
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year

@deconstructible
class MinAgeValidator(BaseValidator):
    message = "La edad esta comprendida entre 18 y 27 años"
    code = 'min_age'

    def compare(self, born, min):
        return calculate_age(born) < min

@deconstructible
class MaxAgeValidator(BaseValidator):
    message = "La edad esta comprendida entre 18 y 27 años"
    code = 'max_age'

    def compare(self, born, max):
        return calculate_age(born) > max