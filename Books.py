def main():
    n, t = map(int, input().split())
    books = [int(number) for number in input().split()]
    maximum = 0
    for i in range(n):
        index, curr, time = i, 0, 0
        while index < n and (time + books[index]) < t:
            time += books[index]
            index += 1
            curr += 1
        if curr > maximum:
            maximum = curr
    print(maximum)


main()
