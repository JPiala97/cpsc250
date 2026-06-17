def f(x):
    return -4.0*x + 3.0


def find_root(a, b):

    epsilon = 1.0E-16      # tolerance for finding the root

    fa = f(a)
    fb = f(b)

    print(a, b, fa, fb)

    # Termination condition #1:
    # interval is sufficiently small
    if abs(b - a) < epsilon:
        return (a + b) / 2.0

    c = (a + b) / 2.0
    fc = f(c)

    # Termination condition #2:
    # exact root found
    if fc == 0.0:
        return c

    # Recursive step
    if fa * fc < 0.0:
        return find_root(a, c)
    else:
        return find_root(c, b)


if __name__ == "__main__":

    a = 0.0
    b = 5.0

    fa = f(a)
    fb = f(b)

    # Pre-checks
    if fa * fb > 0:
        print("No root on this interval!!")

    elif fa == 0:
        print("Root found at x =", a)

    elif fb == 0:
        print("Root found at x =", b)

    else:
        root = find_root(a, b)
        print("Root found at x =", root)
