# Базово что-нибудь считать с консоли можно вот так:
a = input()

# Потом можно вывести его обратно:
print(a)

# Кстати. Как думаете, какой будет тип, если ввести число? Давайте посмотрим.
print(type(a))

# Разумеется, кастовать считанное к нужному типу можно. Даже нужно.
i = int(a)
f = float(a)
print(a, i, f)
print(type(a), type(i), type(f))

print("===============")

# По умолчанию print выводит в конце символ новой строки. Но можно попросить его так не делать:
print("One ", end='')
print("Two ", end='')
print("Three")