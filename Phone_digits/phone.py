def count_combinations(n):
    # Definimos el teclado y las teclas adyacentes
    adjacents = {
        '0': ['0','8'],
        '1': ['1','2','4'],
        '2': ['2','1','5','3'],
        '3': ['3','2','6'],
        '4': ['4','1','5','7'],
        '5': ['5','2','4','6','8'],
        '6': ['6','3','5','9'],
        '7': ['7','4','8'],
        '8': ['8','5','7','9','0'],
        '9': ['9','6','8']
    }

    # Memoización
    memo = {}

    def count(digit, length):
        # Si la longitud es 1, hay una combinación para cada dígito
        if length == 1:
            return 1

        # Si ya hemos calculado este subproblema, lo devolvemos
        if (digit, length) in memo:
            return memo[(digit, length)]

        # Sumar las combinaciones de longitud (length - 1) para los dígitos adyacentes
        total_combinations = 0
        for adj in adjacents[digit]:
            total_combinations += count(adj, length - 1)

        # Guardar el resultado en la memoria
        memo[(digit, length)] = total_combinations
        return total_combinations

    # Sumar las combinaciones para todos los dígitos del 0 al 9
    total = 0
    for digit in map(str, range(10)):  # Convertimos a string para que coincida con las claves del diccionario
        total += count(digit, n)

    return total


n = 10
print(f"Total de combinaciones de longitud {n}: {count_combinations(n)}")