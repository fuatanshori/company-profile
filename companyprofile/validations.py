from django.core.exceptions import ValidationError

def validate_is_published_false(value):
    print(value)
    if value:
        raise ValidationError('Hanya diizinkan is_published=False')