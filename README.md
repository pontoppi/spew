spew is a simple command-line tool to quickly visualize JWST 1D spectra as created by the JWST Calibration Pipeline. Spew can display one or more spectra in the same basic matplotlib window. 

This software is provided as-is, with no warranty.

  
INSTALLATION

using setup.py:
----------
python setup.py install

Using pip:
----------
To be uploaded to pypi

Basic command line usage:
------------------------
spew "<1d spectrum>"
   
example:

spew fztau_1d_v3.0.fits

spew "det_image_*extract1dstep.fits"

