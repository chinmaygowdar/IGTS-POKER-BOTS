def solve_psne(p1_matrix, p2_matrix):
    n = len(p1_matrix)
    m = len(p1_matrix[0])

    psne = []
    p1_best = [[False] * m for _ in range(n)]

    for col in range(m):
        max_payoff = max(p1_matrix[row][col] for row in range(n))

        for row in range(n):
            if p1_matrix[row][col] == max_payoff:
                p1_best[row][col] = True

    p2_best = [[False] * m for _ in range(n)]

    for row in range(n):
        max_payoff = max(p2_matrix[row][col] for col in range(m))

        for col in range(m):
            if p2_matrix[row][col] == max_payoff:
                p2_best[row][col] = True

    for row in range(n):
        for col in range(m):
            if p1_best[row][col] and p2_best[row][col]:
                psne.append((row, col))

    return psne