def add_everything_up(a, b):
    try:
        c = a + b

    except TypeError:
        return str(a) + str(b)

    else:
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return round((a + b), 3)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


