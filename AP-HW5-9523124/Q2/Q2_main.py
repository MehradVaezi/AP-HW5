def func(a, b, *args, **keywords):
    print(f'A = {a} and B = {b}')
    for arg in args:
        print(arg, ",")
    for key in keywords:
        print(key, keywords[key])

func("Num1", "Num2", "Num3", "Num4", "Num5", Student1="John", Student2="Paul", Student3="Guido")   