# do validations of forms

def description_invalid_value(field_name, field_value, list_errors):
    if len(field_value) < 100:
        list_errors[field_name] = "Description cannot have less than 100 chars."
    if len(field_value) > 300:
        list_errors[field_name] = "Description cannot have grater than 300 chars."



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

