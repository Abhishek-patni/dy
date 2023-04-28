def bankers_algorithm(available, maximum, allocation):
    n = len(available)
    need = [[maximum[i][j] - allocation[i][j] for j in range(n)] for i in range(n)]
    finish = [False] * n
    safe_sequence = []

    while False in finish:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= available[j] for j in range(n)):
                available = [available[j] + allocation[i][j] for j in range(n)]
                finish[i] = True
                safe_sequence.append(i)
                found = True

        if not found:
            return None

    return safe_sequence
