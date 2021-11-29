num = iter(range(int(input("Input count of numbers: "))))

while True:
    try:
        print(next(num)**2)
    except StopIteration:
        break