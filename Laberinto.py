laberinto = [
    ['F', 1, 3, 4, 1, 0, 1, 3, 4],
    [1,  0, 4, 0, 3, 1, 4, 0, 1],
    [3,  1, 3, 1, 4, 0, 3, 1, 4],
    [4,  0, 1, 0, 1, 3, 1, 0, 3],
    [1,  3, 4, 3, 1, 4, 3, 4, 1],
    [3,  0, 1, 0, 3, 0, 1, 0, 3],
    [4,  1, 3, 4, 1, 3, 4, 1, 4],
    [1,  0, 0, 0, 0, 0, 0, 0, 1],
    ['I', 3, 4, 3, 4, 3, 4, 3, 4]
]

PUNTOS_MINIMOS = 23
N = 9

def imprimir_laberinto(mat):
    print("\n--- MATRIZ DEL LABERINTO ---")
    for fila in mat:
        print(" ".join(str(val) for val in fila))

def resolver_laberinto():
    visitados = [[False] * N for _ in range(N)]
    mejor_camino = []
    camino_encontrado = False

    def es_valido(r, c):
        return 0 <= r < N and 0 <= c < N and laberinto[r][c] != 0 and not visitados[r][c]

    def backtracking(r, c, puntos_actuales, camino_actual):
        nonlocal camino_encontrado, mejor_camino

        if laberinto[r][c] == 'F':
            if puntos_actuales >= PUNTOS_MINIMOS:
                camino_encontrado = True
                mejor_camino = list(camino_actual) + [(r, c)]
                return True
            return False

        movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for dr, dc in movimientos:
            nr, nc = r + dr, c + dc
            if es_valido(nr, nc):
                visitados[nr][nc] = True
                camino_actual.append((r, c))

                val = laberinto[nr][nc]
                puntos_extra = val if isinstance(val, int) and val in (3, 4) else 0

                if backtracking(nr, nc, puntos_actuales + puntos_extra, camino_actual):
                    return True

                camino_actual.pop()
                visitados[nr][nc] = False

        return False

    inicio_r, inicio_c = 8, 0
    visitados[inicio_r][inicio_c] = True

    exito = backtracking(inicio_r, inicio_c, 0, [])

    if exito:
        print("\n[ÉXITO] Se encontró un camino válido hacia la salida con 23 o más puntos!")
        mat_sol = [row[:] for row in laberinto]
        for r, c in mejor_camino:
            if mat_sol[r][c] not in ['I', 'F']:
                mat_sol[r][c] = '*'
        imprimir_laberinto(mat_sol)
        print("\n Coordenadas del camino:", mejor_camino)
    else:
        print("\n[AVISO] No se encontró ningún camino viable que cumpla con los 23 puntos mínimos.")

imprimir_laberinto(laberinto)
resolver_laberinto()