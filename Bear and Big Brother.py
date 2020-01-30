prob = [int(weight) for weight in input().split()]
output = 0
while prob[0] <= prob[1]:
    prob[0], prob[1] = prob[0] * 3, prob[1] * 2
    output += 1
print(output)
