import math


def accu_geometric(y,p,k,steps):
    answer = 0
    for x in range(y,k+1):
        new_answer = single_geometric(x,p)
        if steps:
            print(f'Probability of Y = {x}: {new_answer:.5f}')
        answer += new_answer
    return answer
def single_geometric(y,p):
    answer = pow((1-p), (y-1))*p
    return answer
    
# Probability
p = 0.07692307692
# From
y = 0
# To
k = 13
steps = True

my = 1/p
var = (1-p)/(pow(p,2))
std = math.sqrt(var)

print('\n')
print('---------------Geometric---------------')
print(f'Expected value (µ): {my:.5f} --- Variance (σ2): {var:.5f} --- Standard deviation (σ): {std:.5f}')
print(f'Probability of X where {y} ≤ Y ≤ {k}: {accu_geometric(y,p,k,steps)}')
print('---------------------------------------')
