def custom_print(a, *values, sep=" ", end="\n", file=None):
    if a > 10:
        print("greater than 10", sep=sep, end=end, file=file)
    elif a < 10:  # Added condition here
        print("less than 10", sep=sep, end=end, file=file)

# Example usage:
custom_print(9)

