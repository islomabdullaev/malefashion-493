from django.core.exceptions import ValidationError

def rating_value_validate(value):
    if not 1 <= value <= 5:
        raise ValidationError(
                ("Value error !"),
                params={"value": value},
            )
