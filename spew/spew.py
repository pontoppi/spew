import os
import glob
import numpy as np
import matplotlib.pylab as plt
#from jwst import datamodels
from astropy.io import fits

class spew():

#    def __init__(self,pattern,help=False,aspect=2,nozero=False):
    def __init__(self,arguments):

        # Store attributes
        pattern = arguments['<pattern>']
        self.aspect = float(arguments['--aspect'])
        self.nozero = arguments['--nozero']

        # Identify all relevant files
        files = self.find_files(pattern)

        # load data from
        specs,hdrs = self.read_specs(files)

        # Plot all data interactively
        self.create_plot(specs,files)

    def find_files(self,pattern):

        if len(pattern)>1:
            # Is it a list of files
            files = pattern
        else:
            # Or a single file or pattern
            files = glob.glob(pattern[0],recursive=False)
        return files

    def read_specs(self,files):

        specs = []
        hdrs = []
        for ff in files:
            spec = fits.getdata(ff)
            hdr  = fits.getheader(ff)
            specs.append(spec)
            hdrs.append(hdr)

        return specs,hdrs

    def create_plot(self,specs,files):

        plt.figure(figsize=(9,9/self.aspect))
        for spec,ff in zip(specs,files):
            try:
                wave  = spec['WAVELENGTH']
                fdens = spec['FLUX']
            except:
                wave  = spec['wavelength']
                fdens = spec['fluxdensity']                
            if self.nozero:
                fdens[fdens==0.0] = np.nan

            plt.step(wave,fdens,where='mid')

        plt.xlabel('Wavelength [$\mu$m]')
        plt.ylabel('Flux density [Jy]')
        plt.title(ff)

        plt.show()
