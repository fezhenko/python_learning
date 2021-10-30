def foo(temperature):
    if temperature>25:
        return "Hot"
    elif temperature >= 15 and temperature <=25:
        return "Warm"
    return "Cold"

print(foo(-1))