valuecount = 0

for value in range(3,101):
    if (value % 3 == 0):
        valuecount += 1
        print(f'Valor {valuecount}: {value}')