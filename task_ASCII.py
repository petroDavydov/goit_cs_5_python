# Задача на визначення ASCII кожної букви у слові

def number_of_ASCII(string: str) -> dict:
    code_letter = {}

    for ch in string:
        if ch not in code_letter:
            code_letter[ch] = ord(ch)
    return code_letter


result = number_of_ASCII("academy")
print(result)
# ---------------------------------------------------
# те саме але повторювані букви відтворюються


def number_of_ASCII(string: str) -> list:
    code_list = []

    for ch in string:
        code_list.append((ch, ord(ch)))
    return code_list


result = number_of_ASCII("academy")
print(result)
