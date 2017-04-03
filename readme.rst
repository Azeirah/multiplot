A convenient way to lay out matplotlib figures
The first argument is a multiline string which diagrammatically describes
the desired layout of your plot

@return (figure, mpt)

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
