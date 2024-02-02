def find_index(n, numbers, x):
    for i in range(n):
        if numbers[i] == x:
            return i + 1
    return -1

def main():
    n = int(input("Enter the value of N (positive integer): "))

    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Input X
    x = int(input("Enter the value of X (integer): "))

    # Find and output the index of X
    result = find_index(n, numbers, x)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
