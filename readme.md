# Multiplot

## Conveniently lay out matplotlib figures

If you're spending a lot of fighting with subplots, and the cold, symbolic syntax required to set-up grids, this is for you!

Multiplot lets you 'draw' the layout you want using a string, which makes it super simple to edit a layout. For example, you can super easily add or remove, hide, or resize the grid layout.

## Usage

Multiplot exposes one function, `multiplot`

The first argument is a multiline string which diagrammatically describes
the desired layout of your plot

The simplest grid would look like


```
multiplot('''
A
''')
```

If you want complicated grid layouts, you can do that as well

```
multiplot('''
AA
AA
BB
CC
CC
''')
```

Or for example this

```
multiplot('''
AAABB
CCCBB
''')

```
Note, make sure that your subfigures have a rectangular shape
e.g.

```
multiplot('''
AA
BB
A''')
```

Won't work.

multiplot takes care of creating the layout using matplotlib's gridspec
You can access each the matplotlib subplot objects by dictionary key access.
The figure is exposed as well

```py
fig, mpt = multiplot('''
AAABB
CCCBB
''')
mpt["A"].plot(...)
mpt["B"].set_title(...)
```

Any arguments you would normally pass to plt.figure, you can pass to multiplot

```py
fig, mpt = multiplot(grid3, figsize=(10, 10), ...)
```
