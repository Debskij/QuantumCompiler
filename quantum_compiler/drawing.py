import matplotlib.pyplot
import typing


def draw_axes() -> None:
    """Draw axes on the plane."""
    points = [[1.2, 0], [0, 1.2], [-1.2, 0], [0, -1.2]]  # dummy points for zooming out
    arrows = [[1.1, 0], [0, 1.1], [-1.1, 0], [0, -1.1]]  # coordinates for the axes
    for p in points:
        matplotlib.pyplot.plot(p[0], p[1] + 0.1)  # drawing dummy points
    for a in arrows:
        matplotlib.pyplot.arrow(0, 0, a[0], a[1], head_width=0.04, head_length=0.08)  # drawing the axes


def draw_unit_circle() -> None:
    """Draw unit circle on the plane."""
    unit_circle = matplotlib.pyplot.Circle((0, 0), 1, color="black", fill=False)
    matplotlib.pyplot.gca().add_patch(unit_circle)


def draw_quantum_state(coords: typing.List[int], name: str, color: str = "blue") -> None:
    """
    Draw quantum state of qbit.

    :param coords: coordinates of quantum state on the plane.
    :param name: name of the quantum state to plot
    :param color: color of drawn arrow
    :return: None
    """
    x, y = list(coords)
    x1 = 0.92 * x
    y1 = 0.92 * y
    matplotlib.pyplot.arrow(0, 0, x1, y1, head_width=0.04, head_length=0.08, color=color)
    x2 = 1.15 * x
    y2 = 1.15 * y
    matplotlib.pyplot.text(x2, y2, name)


def draw_qbit() -> None:
    """Draw sample qbits on the plane."""
    matplotlib.pyplot.figure(figsize=(6, 6), dpi=60)  # draw a figure

    # draw the origin
    matplotlib.pyplot.plot(0, 0, "ro")  # a point in red color
    draw_axes()  # drawing the axes by using one of our predefined function
    draw_unit_circle()  # drawing the unit circle by using one of our predefined function

    # drawing |0>
    matplotlib.pyplot.plot(1, 0, "o")
    matplotlib.pyplot.text(1.05, 0.05, "|0>")
    # drawing |1>
    matplotlib.pyplot.plot(0, 1, "o")
    matplotlib.pyplot.text(0.05, 1.05, "|1>")
    # drawing -|0>
    matplotlib.pyplot.plot(-1, 0, "o")
    matplotlib.pyplot.text(-1.2, -0.1, "-|0>")
    # drawing -|1>
    matplotlib.pyplot.plot(0, -1, "o")
    matplotlib.pyplot.text(-0.2, -1.1, "-|1>")
