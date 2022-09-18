number = int(input("Введите число меньшее, чем 100: "))

if (number >= 100):
    print("Извините, вы нарушили условие! Попробуйте еще раз.")
    number = int(input("Введите число еще раз: "))
    print(f"Ваше число: {number}")
else:
    print(f"Ваше число: {number}")