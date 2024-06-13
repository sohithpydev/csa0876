def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append the remaining elements from both lists
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

def main():
    try:
        list1 = [int(x) for x in input("Enter the first sorted list of numbers separated by space: ").split()]
        list2 = [int(x) for x in input("Enter the second sorted list of numbers separated by space: ").split()]

        merged_list = merge_sorted_lists(list1, list2)

        print("Merged and sorted list:", merged_list)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
