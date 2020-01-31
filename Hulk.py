from sys import stdin, stdout

n = int(stdin.readline())
prob = ['I'] * (n+1)
for i in range(n-1):
    if i % 2:
        prob[i+1] = 'love that'
    else:
        prob[i+1] = 'hate that'
if n % 2:
    prob[-1] = 'hate it'
else:
    prob[-1] = 'love it'
stdout.write(' '.join(prob))
