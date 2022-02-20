from setuptools import setup

setup(name='spew',
      version=1.0,
      description='Spectra with Webb (SPEW): Quicklook tool for JWST 1D spectra',
      author='Klaus Pontoppidan (STScI)',
      author_email='pontoppi@stsci.edu',
      url='http://jwst.stsci.edu/',
      download_url = '',
      packages=['spew'],
      install_requires=['docopt>=0.6.2'],
      entry_points = {'console_scripts': ['spew=spew.cli:main']}
      )
