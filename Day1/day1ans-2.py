def main():
    file = open("day1input.txt")
    sum = 0
    nums = [
            "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"
        ]
    for line in file:
        while not any(line.startswith(num) for num in nums) and not line[0].isdigit():
            line = line[1:]
        while not any(line.endswith(num) for num in nums) and not line[-1].isdigit():
            line = line[:-1]

        a = 0
        b = 0
        for x, num in enumerate(nums):
            if line.startswith(num):
                a = x + 1
            if line.endswith(num):
                b = x + 1

        if line[0].isdigit():
            a = int(line[0])
        if line[-1].isdigit():
            b = int(line[-1])

        sum += a * 10 + b

    print(sum)

if __name__ == '__main__':
    main()