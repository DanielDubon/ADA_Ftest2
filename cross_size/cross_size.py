def max_cross_size(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # Inicializamos las matrices auxis
    left = [[0] * cols for i in range(rows)]
    right = [[0] * cols for i in range(rows)]
    top = [[0] * cols for i in range(rows)]
    bottom = [[0] * cols for i in range(rows)]

    # Llenamos la matriz left
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                left[i][j] = left[i][j - 1] + 1 if j > 0 else 1

    # Llenar la matriz right
    for i in range(rows):
        for j in range(cols - 1, -1, -1):
            if grid[i][j] == 1:
                right[i][j] = right[i][j + 1] + 1 if j < cols - 1 else 1

    # Llenar la matriz top
    for j in range(cols):
        for i in range(rows):
            if grid[i][j] == 1:
                top[i][j] = top[i - 1][j] + 1 if i > 0 else 1

    # Llenar la matriz bottom
    for j in range(cols):
        for i in range(rows - 1, -1, -1):
            if grid[i][j] == 1:
                bottom[i][j] = bottom[i + 1][j] + 1 if i < rows - 1 else 1

    # DEBUG: Imprimir las matrices auxiliares
    print("Matriz left:", left)
    print("Matriz right:", right)
    print("Matriz top:", top)
    print("Matriz bottom:", bottom)

    # Encontrar el tamaño máximo de la cruz
    max_cross_size = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # El tamaño de la cruz se determina por el mínimo de los cuatro valores
                cross_size = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
                # Solo consideramos el tamaño de la cruz si hay al menos un 1 en cada dirección
                if cross_size > 1:  # Debe ser mayor que 1 para formar una cruz
                    total_size = (cross_size * 4) - 3  # 4 brazos menos 3 porque el centro se cuenta 4 veces
                    max_cross_size = max(max_cross_size, total_size)
                print(f"Posición ({i}, {j}): left={left[i][j]}, right={right[i][j]}, top={top[i][j]}, bottom={bottom[i][j]}, cross_size={cross_size}, total_size={total_size if cross_size > 1 else 0}")  # Debug

    return max_cross_size

# Ejemplo de uso
grid1 = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1,1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [ 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
]

grid2 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0]
]

grid3 = [
    [1, 1, 1],
    [1, 1, 1],
    [0, 1, 0]
]

grid4 = [
    [1, 1, 1, 0,0],
    [1, 1, 1,0,0],
    [1, 1, 1,1,1],
    [0, 1, 1,0,0],
    [0, 1, 1,0,0],
]


grid5 = [

    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


print(max_cross_size(grid5))