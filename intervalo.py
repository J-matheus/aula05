dentro = 0
fora = 0
for n in range (3):
    num = int(input(f"Digite 10 valores: "))
    if num>=10 and num<=20:
        dentro= dentro + 1
    else:
        fora = fora + 1
print(f"os numeros de dentro {dentro}, os numeros de fora {fora}.")
