def coverage(a, b, c, r):
    if c + r <= b and c - r >= a:
        return 2 * r
    if c - r >= b or c + r <= a:
        return 0
    if c >= 



def main():
    n = int(input())
    for i in range(n):
        a, b, c, r = map(int, input().split())
        print(b - a - coverage(a, b, c, r))



main()
