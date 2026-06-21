def float_to_ieee754(n):
    if n == 0.0:
        return "0", "00000000", "0" * 23

    sinal = "1" if n < 0 else "0"
    n = abs(n)

    parte_inteira = int(n)
    parte_fracionaria = n - parte_inteira

    bin_inteiro = bin(parte_inteira)[2:] if parte_inteira > 0 else ""

    bin_fracionario = ""
    while parte_fracionaria > 0 and len(bin_fracionario) <= 30:
        parte_fracionaria *= 2
        bit = int(parte_fracionaria)
        bin_fracionario += str(bit)
        parte_fracionaria -= bit

    if parte_inteira == 0:
        primeiro_um = bin_fracionario.find('1')
        if primeiro_um == -1:
            return sinal, "00000000", "0" * 23
        expoente = - (primeiro_um + 1)
        mantissa = bin_fracionario[primeiro_um + 1:]
    else:
        expoente = len(bin_inteiro) - 1
        mantissa = bin_inteiro[1:] + bin_fracionario

    expoente_com_vies = expoente + 127
    bin_expoente = bin(expoente_com_vies)[2:].zfill(8)

    mantissa = (mantissa + "0" * 23)[:23]

    return sinal, bin_expoente, mantissa

print("=== Calculadora IEEE 754 ===")
num1 = float(input("Digite o primeiro número decimal (a): "))
num2 = float(input("Digite o segundo número decimal (b): "))

s1, e1, m1 = float_to_ieee754(num1)
s2, e2, m2 = float_to_ieee754(num2)

print(f"\nRepresentação de (a) {num1}:")
print(f"Sinal: {s1} | Expoente: {e1} | Mantissa: {m1}")

print(f"\nRepresentação de (b) {num2}:")
print(f"Sinal: {s2} | Expoente: {e2} | Mantissa: {m2}")

soma = num1 + num2
ss, es, ms = float_to_ieee754(soma)

print(f"\nResultado da operação normal (a + b): {soma}")
print(f"Representação da soma (IEEE 754):")
print(f"Sinal: {ss} | Expoente: {es} | Mantissa: {ms}")