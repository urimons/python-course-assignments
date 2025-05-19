# Insert list of numbers
numbers = [1203, 1256, 312456, 98]

def count_digits(nums):
    # Initialize counts for digits 0–9
    counts = {str(d): 0 for d in range(10)}
    # Tally every digit in every number
    for num in nums:
        for ch in str(num):
            if ch.isdigit():
                counts[ch] += 1
    return counts

def main():
    counts = count_digits(numbers)
    # Print counts for 0 through 9
    for digit in map(str, range(10)):
        print(f"{digit}  {counts[digit]}")

if __name__ == "__main__":
    main()
