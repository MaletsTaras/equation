# запитуємо доданки та суму
a = input("Перше число (або x): ")
b = input("Друге число (або x): ")
result = input("Результат:")
operation = input("Який знак стоїть між двома числами(доступними знаками є + та -): ")


# зменшуємо всі змінні
a = a.lower()
b = b.lower()
result = result.lower()
operation = operation.lower()

# перевіряємо чи користувач ввів число в змінну result 
try:
    result = float(result)
except ValueError:
    print("Результат повинен бути числом!")
else:
    # перевіряємо умови для визначення "X"

    # якщо operation == "+"
    if operation == "+":
        # якщо a == x
        if a == "x" and b != "x":
            x = result - float(b)
            print(f"X = {x}")
        
        # якщо b == x
        elif b == "x" and a != "x":
            x = result - float(a)
            print(f"X = {x}")

    # якщо operation == "-"
    elif operation == "-":
        # якщо a == x
        if a == "x" and b != "x":
            x = result + float(b)
            print(f"X = {x}")
        
        # якщо b == x
        elif b == "x" and a != "x":
            x = float(a) - result
            print(f"X = {x}")
    
    # якщо помилка
    else:
        print("Не можна вводити два числа X, або ви не ввели X, або не ввели знак між числами!")