import matplotlib.pyplot as plt


def multiplot(plots, *args, **kwargs):
    """A convenient way to lay out matplotlib figures
    The first argument is a multiline string which diagrammatically describes
    the desired layout of your plot

    @return (figure, grid)

    e.g., a simple single plot looks like
    grid1 = '''
    A
    '''

    If you want complicated grid layouts, you can do that as well

    grid2 = '''
    AA
    AA
    BB
    CC
    CC
    '''

    grid3 = '''
    AAABB
    CCCBB
    '''

    Make sure that your subfigures have a rectangular shape
    e.g.
    '''
    AA
    BB
    A'''
    Will not work at all.

    multiplot takes care of creating the layout using matplotlib's gridspec
    You can access each individual subplot by dictionary key access.
    The figure is exposed as well

    fig, mpt = multiplot(grid3)
    mpt["A"].plot(...)
    mpt["B"].set_title(...)

    Any arguments you want to pass to plt.figure, you can pass to multiplot right after the grid
    eg
    fig, mpt = multiplot(grid3, figsize=(10, 10), ...)

    Easily layout complicated grids
    Easily change its layout
    Complete access to axes and figure
    """
    chars = {}
    lines = plots.split("\n")
    if len(lines[0]) < len(lines[1]):
        lines.pop(0)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in chars:
                chars[char][1] = (x, y)
            else:
                chars[char] = [(x, y), (x, y)]

    plots = {}

    columns = len(lines[0])
    rows = len(lines)
    gridSize = (rows, columns)

    grid = {}

    fig = plt.figure(*args, **kwargs)
    for char in chars.keys():
        points = chars[char]
        leftTop = points[0]
        bottomRight = points[1]

        width = 1 + bottomRight[0] - leftTop[0]
        height = 1 + bottomRight[1] - leftTop[1]

        grid[char] = plt.subplot2grid(
            gridSize, [leftTop[1], leftTop[0]], colspan=width, rowspan=height)
        grid[char].set_title(char +
            "(w={width}, h={height})".format(height=height, width=width))

    return fig, grid


# example

# mtp = multiplot(
# """
# AABBB
# AABBB
# AACCC""")

# mtp["A"].plot(numpy.arange(0, 100, 1))
# mtp["A"].set_title("")
# mtp["B"].plot(numpy.arange(0, 50, 1))
# mtp["B"].set_title("")
# mtp["C"].plot(numpy.arange(0, 25, 0.5))
# mtp["C"].set_title("")
# plt.show()
