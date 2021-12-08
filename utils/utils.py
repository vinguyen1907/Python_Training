def compare(a: int = 5, b: int = 9) -> None:
    """
    compare a and b
    :param a:
    :param b:
    :return: not return anything
    """
    if a == b:
        print('Bang nhau')
    elif a > b:
        print(f'{a} lon hon {b}')
    else:
        print(f'{a} be hon {b}')


def checkEvenNumber(a):
    if a % 2 == 0:
        return 1
    return 0


if __name__ == "__main__":
    compare(7, 10)
    a = 7
    if checkEvenNumber(a):
        print(f'{a} la so chan')
    else:
        print(f'{a} la so le')
