def main():
    m, s = map(int, input().split())
    if s < m or s > 9*m:
        print('-1 -1')
    else:
        prob = [0]*m
        for i in range(m-1):
            if s > 10 + m - i:
                prob[i] = 9
            else:
                prob[i] = 1
        prob[-1] = s - sum(prob)
        prob.sort()
        print("".join([str(number) for number in prob]), "".join([str(number) for number in prob][::-1]))


main()
