# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    used_weights = [0] * len(weights)
    
    while True:
        if capacity == 0:
            return value
        max_ratio = 0
        max_it = 0
        for i in range(len(weights)):
            if weights[i] > 0:
                ratio = values[i] / weights[i]
                if ratio > max_ratio:
                    max_ratio = ratio
                    max_it = i
        a = min(capacity, weights[max_it])
        weights[max_it] -= a
        capacity -= a
        used_weights[max_it] += a
        value += a * max_ratio

                
            
    # write your code here

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
