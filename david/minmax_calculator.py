def main():
    try:
        input_str = input("Enter numbers separated by spaces: ")
        tokens = input_str.strip().split()

        numbers = []
        for token in tokens:
            number = float(token)
            numbers.append(number)

        if not numbers:
            print("Invalid input.")
            return

        min_value = numbers[0]
        max_value = numbers[0]

        for num in numbers[1:]:
            if num < min_value:
                min_value = num
            if num > max_value:
                max_value = num

        print(f"Min: {min_value}, Max: {max_value}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
