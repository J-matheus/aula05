num = int(input(f"informe o numero: "))
if num>=1:
    print("os numeros são: ", end=" ")
    for i in range(1, num + 1, 1):
        print(i, end=" ")
else:
    print("o numero é menor que 1.")