import sys

# Function to factorize a number n
def factorize(n):
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            for line in file:
                n = int(line.strip())
                factors = factorize(n)
                print(f"{n}={'*'.join(map(str, factors))}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print(f"Invalid number in the file '{filename}'.")

if __name__ == '__main__':
    main()
