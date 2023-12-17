def main():
    file = open("day1input.txt")
    sum = 0
    for line in file:
        for i in range(len(line)):
            if line[i].isnumeric():
                cur = 10 * int(line[i])
                break
        for i in range(len(line) - 1, -1, -1):
            if line[i].isnumeric():
                cur += int(line[i])
                break
        sum += cur

    print(sum)

if __name__ == '__main__':
    main()