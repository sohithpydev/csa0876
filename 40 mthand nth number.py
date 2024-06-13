def find_mth_maximum_nth_minimum(arr, m, n):
    sorted_arr = sorted(set(arr), reverse=True)

    if 1 <= m <= len(sorted_arr) and 1 <= n <= len(sorted_arr):
        mth_max = sorted_arr[m - 1]
        nth_min = sorted_arr[n - 1]
        return mth_max, nth_min
    else:
        return None, None

def main():
    try:
        arr = [int(x) for x in input("Enter an array of numbers separated by space: ").split()]
        m = int(input("Enter the value of M for Mth maximum number: "))
        n = int(input("Enter the value of N for Nth minimum number: "))

        mth_max, nth_min = find_mth_maximum_nth_minimum(arr, m, n)

        if mth_max is not None and nth_min is not None:
            sum_result = mth_max + nth_min
            diff_result = mth_max - nth_min

            print(f"\nMth maximum number: {mth_max}")
            print(f"Nth minimum number: {nth_min}")
            print(f"Sum of Mth maximum and Nth minimum: {sum_result}")
            print(f"Difference of Mth maximum and Nth minimum: {diff_result}")
        else:
            print("Invalid values of M and/or N. Please enter valid positive integers.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
