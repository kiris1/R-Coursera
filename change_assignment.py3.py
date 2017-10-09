# Uses python3
import sys

def get_change(m):
   
    coins = [5, 2, 1]
    iteration = 0
    amount = m
    coin = 0
    
    while True:
        if amount == 0:
            return iteration
        for i in range(3):
            if coins[i] <= amount:
                coin = coins[i]
                break
        iteration, amount = iteration + divmod(amount, coin)[0], divmod(amount, coin)[1]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
