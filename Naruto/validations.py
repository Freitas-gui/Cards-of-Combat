# do validations of forms

def name_invalid_value(field_name, field_value, list_errors):
    if len(field_value) > 20:
        list_errors[field_name] = "Name cannot have grater than 20 chars."

def description_invalid_value(field_name, field_value, list_errors):
    if len(field_value) < 100:
        list_errors[field_name] = "Description cannot have less than 100 chars."
    elif len(field_value) > 250:
        list_errors[field_name] = "Description cannot have grater than 250 chars."



def level_invalid_value(field_name, field_value, list_errors):
    if field_value < 1:
        list_errors[field_name] = "This value cannot be less than 1."
    elif field_value > 10:
        list_errors[field_name] = "This value cannot be greater than 10."


def attack_or_defense_invalid_value(field_name, field_value, list_errors):
    if field_value < 0:
        list_errors[field_name] = "This value cannot be less than 0."
    elif field_value > 1000:
        list_errors[field_name] = "This value cannot be greater than 1000."

