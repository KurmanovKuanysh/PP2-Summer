def myfunc():
    global x  # это делает переменную глобальной и доступной не только внутри функции
    x = "fantastic"
    print("Это печатается функцией!")


myfunc()

print("Python is " + x)
