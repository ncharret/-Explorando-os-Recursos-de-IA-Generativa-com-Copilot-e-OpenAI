def fatorial(n):
    """Calcula o fatorial de um número usando recursão"""
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

# Exemplo de uso
print(fatorial(5))  # Saída: 120
