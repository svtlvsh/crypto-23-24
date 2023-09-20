# Додаткова функція для удобного виводу  результатів біграм

def print_result():
    for key, number in sorted_dictionary.items():
        number = round(number, 5)
        print(f"{number}")
        #{key} {number}

print_result()
