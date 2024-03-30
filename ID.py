import random

def generate_id():
    # Generate four random digits for the ID
    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(4))
    return f'M230{random_digits}'

def main():
    # Get user's name as input
    name = input("Enter your name: ")

    # Generate ID
    generated_id = generate_id()

    # Display the result
    print(f"Hello, {name}! Your generated ID is: {generated_id}")

if __name__ == "__main__":
    main()
