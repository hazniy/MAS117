import math

def infinite_limit_table(f, n):
    """
    Tabulates the values of a function f(x) for x = 10^i, i = 1 to n.

    Parameters:
        f (function): A function to evaluate.
        n (int): The number of rows in the table, with x = 10^i for i = 1 to n.
    """
    horizontal_line = "-" * 35
    print(horizontal_line)
    print(f"{'x':>12} {'f(x)':>22}")
    print(horizontal_line)

    for i in range(1, n + 1):
        x = 10**i
        value = f(x)
        print(f"{x:>12} {value:>22.9f}")

    print(horizontal_line)


# Define the functions g(x) and h(x)
def g(x):
    """Calculates g(x) = x^(1/x)."""
    return x**(1/x)

def h(x):
    """Calculates h(x) = (1 + 1/x)^x."""
    return (1 + 1/x)**x


# Main program
if __name__ == "__main__":
    n = 10  # Number of rows in the table

    print("\ng(x) = x^(1/x)")
    infinite_limit_table(g, n)

    print("\nh(x) = (1 + 1/x)^x")
    infinite_limit_table(h, n)
