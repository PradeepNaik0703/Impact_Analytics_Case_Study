from itertools import product
import sys

def count_consecutive_zeros(sequence):
    max_consecutive_zeros = 0
    current_consecutive_zeros = 0

    for digit in sequence:
        if digit == '0':
            current_consecutive_zeros += 1
            max_consecutive_zeros = max(max_consecutive_zeros, current_consecutive_zeros)
        else:
            current_consecutive_zeros = 0

    return max_consecutive_zeros

def calculate_attendance_stats(n):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError("Number of days (N) should be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    total_combinations = 0
    count_consecutive_zeros_4_or_more = 0
    count_last_digit_zero_after_removal = 0

    for combo in product("01", repeat=n):
        total_combinations += 1
        sequence = "".join(combo)
        
        # Check for consecutive zeros
        consecutive_zeros = count_consecutive_zeros(sequence)
        if consecutive_zeros >= 4:
            count_consecutive_zeros_4_or_more += 1
        else:
            # Check if the last digit is zero
            if sequence[-1] == '0':
                count_last_digit_zero_after_removal += 1

    ways_to_attend = total_combinations - count_consecutive_zeros_4_or_more

    return ways_to_attend, count_last_digit_zero_after_removal


def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <number_of_days>")
        sys.exit(1)

    n = sys.argv[1]
    ways_to_attend, probability_to_miss = calculate_attendance_stats(n)

    print(f"for {n} days: {probability_to_miss}/{ways_to_attend}")
    
if __name__ == "__main__":
    main()
