Stanserca = list()

def sums_rufye (text_name, text_age, btn4_text, btn3_text_3):
    rufye_result_value = (4 * (int (text_age) + int (btn4_text) + int (btn3_text_3)) - 200) / 10  # Приклад значення

    age = int(text_age)
    normal_age = (min (age, 15) - 7) // 2
    riven = 21 - normal_age * 1.5
    global result
    result = proc_serdca(rufye_result_value, riven)

    return f"{text_name} \n Ваш індекс Руф'є: {rufye_result_value}.\nПрацездатність серця: {Stanserca [0]}."

def proc_serdca(rufye_result_value, riven):
    if rufye_result_value >= riven:
        Stanserca.append("Висока.")
        return 0
    riven -= 4
    if rufye_result_value >= riven:
        Stanserca.append("Задовільна")
        return 1
    riven -= 5
    if rufye_result_value >= riven:
        Stanserca.append("Вище сер")
        return 2
    riven -= 5.5
    if rufye_result_value >= riven:
        Stanserca.append("Середня")
        return 3
    Stanserca.append("Низька")
    return 4