# do validations of forms

def level_invalid_value(field_name, field_value, lista_erros):
    if field_value < 1:
        lista_erros[field_name] = "This value cannot be less than 1."
    elif field_value > 10:
        lista_erros[field_name] = "This value cannot be greater than 10."

def attack_or_defense_invalid_value(field_name, field_value, lista_erros):
    if field_value < 0:
        lista_erros[field_name] = "This value cannot be less than 0."
    elif field_value > 1000:
        lista_erros[field_name] = "This value cannot be greater than 1000."

