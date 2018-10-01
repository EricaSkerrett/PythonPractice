def main():
    bat = add_three(3, 5, 4)

    ans = divide_sum(bat)
    print('this is the output of divide_sum():', format(ans))

def add_three(v1, v2, v3):
    """do something
    """
    p = v1 + v2 + v3
    print(p)
    return(p)


def divide_sum(v1):
    """doc strings
    """
    p = v1 / 3
    print(p)
    return(p)
    """multiply 2 numbers
    :param v1: number one
    :param v2: number two
    :returns: product number
    """


if __name__ == "__main__":
    main()
