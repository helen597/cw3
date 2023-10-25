def format_number(account):
    """Преобразовывает номер карты в формат:
    Visa Platinum 7000 79** **** 6361
    или номер счета в формат:
    Счет ** 9638"""
    formatted_number = ""
    if "Счет" in account:
        formatted_number = "Счет **" + account[-4:]
    else:
        masked_account = account[-16:-12] + " " + account[-12:-10] + "** **** " + account[-4:]
        if "Maestro" in account:
            formatted_number = "Maestro " + masked_account
        elif "MasterCard" in account:
            formatted_number = "MasterCard " + masked_account
        elif "Visa Classic" in account:
            formatted_number = "Visa Classic " + masked_account
        elif "Visa Platinum" in account:
            formatted_number = "Visa Platinum " + masked_account
        elif "Visa Gold" in account:
            formatted_number = "Visa Gold " + masked_account
        elif "МИР" in account:
            formatted_number = "МИР " + masked_account
    return formatted_number
