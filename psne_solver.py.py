def solve_psne(p1_matrix, p2_matrix):
    rows = len(p1_matrix)
    cols = len(p1_matrix[0])
    equilibria = []

    player1_br = [[False] * cols for _ in range(rows)]
    for c in range(cols):
        best = max(p1_matrix[r][c] for r in range(rows))
        for r in range(rows):
            if p1_matrix[r][c] == best:
                player1_br[r][c] = True

    player2_br = [[False] * cols for _ in range(rows)]
    for r in range(rows):
        best = max(p2_matrix[r][c] for c in range(cols))
        for c in range(cols):
            if p2_matrix[r][c] == best:
                player2_br[r][c] = True

    for r in range(rows):
        for c in range(cols):
            if player1_br[r][c] and player2_br[r][c]:
                equilibria.append((r, c))

    return equilibria