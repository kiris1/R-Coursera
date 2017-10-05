# Uses python3
import sys

def get_fibo(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def get_fibonacci_huge_eff(n, m):
    
    cycle = [0, 1]
    if  n < m:
        return get_fibo(n)
    
    i = 2
    
    while True:
        cycle.append(get_fibo(i) % m)
        if (cycle[i - 1], cycle[i]) == (0, 1):
            break
        i += 1
    
    cycle_len = len(cycle)
    
    return cycle[n % cycle_len]
    

    
    
    
    

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_eff(n, m))
