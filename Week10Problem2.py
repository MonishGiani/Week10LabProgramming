def smallest_beautiful_number(x):
    current_number = x

    while True:
        digits = set(str(current_number))
        if len(digits) == 1 and '0' not in digits:
            return current_number
        current_number += x

def main():
    try:
        x = int(input("Enter a number: "))
        if x % 2 != 0 and x % 5 != 0:
            result = smallest_beautiful_number(x)
            print(f"The smallest beautiful number divisible by {x} is: {result}")
        else:
            print("Please enter a number that is not divisible by 2 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
