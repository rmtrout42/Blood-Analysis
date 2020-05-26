def linearfunction(p1, p2, x):
    slope = (p1[1] - p2[1])/(p1[0] - p2[0])
    yintercept = p1[1]-slope*p1[0]
    return x*slope+yintercept


def point_on_line(p1, p2, p3):
    y = linearfunction(p1, p2, p3[0])
    return y == p3[1]


print(linearfunction((0, 0), (1, 1), 5))
