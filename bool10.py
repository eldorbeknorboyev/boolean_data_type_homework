def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    from math import sqrt
    return sqrt(a)%1==0
print(main(9))
print(main(15))
print(main(121))