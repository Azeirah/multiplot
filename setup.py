from setuptools import setup

with open('readme.rst', 'r') as f:
    long_description = f.read()

setup(name="mpt-multiplot",
      description="Convenient matplotlib subplot grids",
      long_description=long_description,
      version="0.0.1",
      url="https://github.com/Azeirah/multiplot.git",
      author="M. Brekelmans",
      author_email="tijntje_7@msn.com",
      license="MIT",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 3.4',
          'License :: OSI Approved :: MIT License'
      ],
      keywords="matplotlib grid convenience jupyter",
      install_requires="matplotlib"
)
