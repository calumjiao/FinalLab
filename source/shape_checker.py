# pylint: disable= invalid-name
# It is invalid name for sure but not bad for the program
# pylint: disable= too-many-boolean-expression
# program working fine so I did not want to change the code.
# pylint: disable= too-many-arguments
# It was alright required for function.
# pylint: disable= too-many-return-statment
# It is fine because system performance is not affecting
# pylint: disable= bad-option-value
# I already catch the specific exception before the generic one.
# pylint: disable= no-member
# it is providing me false worning
# pylint: disable= too-many-return-statments
# I do not know how to eliminate this
# pylint: disable= trailing-whitespace
# it is not affecting program.
"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or
iscoceles
"""




def get_triangle_type(a=0, b=0, c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 3:
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        print a
        print b
        print c

    if not(isinstance(a, (int, float))
           and isinstance(b, (int, float))
           and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def get_rectangle_type(a=0, b=0, c=0, d=0):
    """
    Determine if the given shape  is  rectangle or square

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :param c: line d
    :type d: float

    :return: "rectangle", "square" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 4:
        c = a[2]
        b = a[1]
        d = a[3]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 4:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        c = values[1]
        b = values[2]
        d = values[3]
        print a
        print b
        print c
        print d
    if not (isinstance(a, (int, float))
            and isinstance(b, (int, float))
            and isinstance(c, (int, float))
            and isinstance(d, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == b and b == c and c == d:
        return "square"

    elif a == c and b == d:
        return "rectangle"
    else:
        return "invalid"


def get_quadrilateral_type(a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0):
    """
    Determine if the given shape  is  rectangle or square, rhombus, or disconnected.


    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :param c: line d
    :type d: float

    :param d: line e
    :type e: float

    :param e: line f
    :type f: float

    :param f: line g
    :type g: float

    :param g: line h
    :type h: float

    :return: "rectangle", "square" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 8:
        c = a[2]
        b = a[1]
        d = a[3]
        e = a[4]
        f = a[5]
        g = a[6]
        h = a[7]
        a = a[0]
    if isinstance(a, dict) and len(a.keys()) == 8:
        b = a['sidetwo']
        c = a['sidethree']
        d = a['sidefour']
        e = a['corner1']
        f = a['corner2']
        g = a['corner3']
        h = a['corner4']
        a = a['sideone']

    if not (isinstance(a, (int, float)) 
            and isinstance(b, (int, float)) 
            and isinstance(c, (int, float)) 
            and isinstance(d, (int, float)) 
            and isinstance(e, (int, float))
            and isinstance(f, (int, float))
            and isinstance(g, (int, float))
            and isinstance(h, (int, float))):
        return "invalid"
    if (e + f + g + h) != 360:
        return "disconnected"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == b and b == c and c == d:
        if e == 90 and f == 90 and g == 90 and h == 90:
            return "square"
        else:
            return "rhombus"

    elif a == c and b == d and e == 90 and f == 90 and g == 90 and h == 90:

        return "rectangle"
    else:
        return "invalid"
