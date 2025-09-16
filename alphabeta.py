MAX, MIN = 1000, -1000

def minimax(depth, idx, maxP, vals, alpha, beta):
    # Base case: leaf node reached
    if depth == 3:
        return vals[idx]

    if maxP:  # Maximizer's move
        best = MIN
        for i in range(2):  # Each node has 2 children
            val = minimax(depth + 1, idx * 2 + i, False, vals, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                print("Pruned at MAX node with value:", best)
                break
        return best

    else:  # Minimizer's move
        best = MAX
        for i in range(2):
            val = minimax(depth + 1, idx * 2 + i, True, vals, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                print("Pruned at MIN node with value:", best)
                break
        return best


if __name__ == "__main__":
    vals = [3, 5, 6, 9, 1, 2, 0, -1]  # Leaf node values
    print("The optimal value is:", minimax(0, 0, True, vals, MIN, MAX))