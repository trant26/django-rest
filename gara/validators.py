from django.core.exceptions import ValidationError

def validate_name(value):
    if value.isnumeric():
        raise ValidationError("Name is not include number!")


def validate_email(value):
    seria_number = value
    if ".edu" in email:
        raise ValidationError("We do not accept edu emails")

def validate_number(value):
    if value < 0:
        raise ValidationError("It must be a number larger 0!")

def validate_phone(value):
    if value.isalpha(): 
        raise ValidationError("Phone is number and not over 13 number")
    if len(value) > 13 and len(value) < 10: 
        raise ValidationError("Phone is number and not over 13 number")


CATEGORIES = ['Mexican', 'Asian', 'American', 'Italian', 'Chinese', 'Thai', 'Pizza', 'Other']

def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f"{value} not a valid category")