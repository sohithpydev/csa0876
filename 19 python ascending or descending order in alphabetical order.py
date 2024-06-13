def sort_names(names, ascending=True):
    return sorted(names, reverse=not ascending)

# Get input from the user
names = input("Enter a list of names separated by spaces: ").split()
sorting_order = input("Enter 'A' for Ascending or 'D' for Descending: ").upper()

# Check user's choice and perform sorting accordingly
if sorting_order == 'A':
    sorted_names = sort_names(names, ascending=True)
    print("Names in Ascending Order:", sorted_names)
elif sorting_order == 'D':
    sorted_names = sort_names(names, ascending=False)
    print("Names in Descending Order:", sorted_names)
else:
    print("Invalid choice. Please enter 'A' or 'D' for sorting order.")
