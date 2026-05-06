print("=" * 65)
print(" ANALISADOR DE ANO BISSEXTO COM CÁLCULO DE DIAS")
print("=" * 65)

def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

ano = int(input("\nDigite um ano (exemplo: 2024): "))

if eh_bissexto(ano):
    dias = 366
    resultado = "É BISSEXTO"
else:
    dias = 365
    resultado = "NÃO é bissexto"

print(f"\n O ano {ano} {resultado}!")
print(f" Portanto, ele tem {dias} dias.")

print("\n" + "=" * 65)
print("REGRA DO ANO BISSEXTO EXPLICADA:")
print("=" * 65)
print("Um ano é bissexto quando:")
print("• É divisível por 4, E")
print("• Não é divisível por 100, OU")
print("• É divisível por 400.")
print("\nFórmula utilizada no código:")
print(" (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)")
print("=" * 65)

print("\nExemplos de teste:")
testes = [2024, 2025, 2000, 1900, 2028, 2100]

for a in testes:
    status = "Bissexto" if eh_bissexto(a) else "Não bissexto"
    d = 366 if eh_bissexto(a) else 365
    print(f" {a} → {status} → {d} dias")
