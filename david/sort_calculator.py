def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    try:
        input_str = input("Enter numbers separated by spaces: ").strip()
        if not input_str:
            raise ValueError("Invalid input.")
        
        tokens = input_str.split()
        numbers = []

        for token in tokens:
            num = float(token)
            numbers.append(num)

        bubble_sort(numbers)

        sorted_str = ' '.join(str(float(num)) for num in numbers)
        print(f"Sorted: {sorted_str}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
