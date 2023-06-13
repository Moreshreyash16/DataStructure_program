'''
@Author: Shreyash More

@Date: 2023-06-10 18:30:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-10 18:32:30

@Title : Write a Python program to print all unique values in a dictionary.


'''
def print_unique_values(data):
    """
    Prints all unique values in a dictionary.

    Description:
        This function takes a list of dictionaries as input and prints
        all the unique values present in the dictionaries.

    Parameters:
        - data (list): A list of dictionaries containing key-value pairs.

    Returns:
        None
    """

    unique_values = set()

    for item in data:
        for value in item.values():
            unique_values.add(value)

    print("Unique Values:", unique_values)


def main():
    data = [
        {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}
    ]

    print_unique_values(data)


if __name__ == "__main__":
    main()
