#!/usr/bin/python3


def add(a, b):
    """
    Custom addition
    :param a: int, left operand
    :param b: int, right operand
    :return: int, the sum
    """
    return a + b

def sub(a, b):
    """
    Custom substraction
    :param a: int, left operand
    :param b: int, right operand
    :return: int, the difference
    """
    return add(a, -b)

def mult(a, b):
    """
    Custom multiplication
    :param a: int, left operand
    :param b: int, right operand
    :return: int, the product
    """
    def multHelper(a, b):
        """
        Does multiplication ONLY if b >= 0
        """
        result = 0
        for i in range(b):
            result = add(a, result)
        return result

    if b < 0:
        # multiplies 'a' and absolute value of 'b'; changes the singn of the result
        return -(multHelper(a, abs(b)))
    else:
        return multHelper(a, b)

def div(a, b):
    """
    Custom division
    :param a: int, left operand
    :param b: int, right operand
    :return: int, the quotient
    """
    def divHelper(a, b):
        """
        Does division ONLY if a > 0 and b > 0
        """
        quotient = 0
        while a >= b:
            a = a - b
            quotient += 1
        return quotient

    if b == 0:
        return None

    elif (a < 0) != (b < 0):
        # divides absolute value of 'a' on absolute value of 'b'; changes the singn of the result
        return -(divHelper(abs(a), abs(b)))
    
    else:
        return divHelper(abs(a), abs(b))


def mod(a, b):
    """
    Custom modulo
    :param a: int, left operand
    :param b: int, right operand
    :return: int, the remainder
    """
    if b == 0:
        return None

    b_is_negative = (b < 0)

    a = abs(a)
    b = abs(b)

    while a >= b:
        a = a - b

    # according to Donald Knuth, floored division remainder would always have the same sign as the divisor (the right operand)

    if b_is_negative:
        return -a
    else:
        return a






	





























