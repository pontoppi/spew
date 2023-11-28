"""
Usage:
    spew <pattern> [--aspect=<ratio> --nozero --ylog --ext=<ext>]
    spew <pattern> ...

Options:
    -h, --help                    Show this help
    --aspect=<ratio>              Set initial aspect ratio of plot [default: 2]
    --nozero                      If the spectra are padded with 0s, this removes them. 
    --ylog                        Set the y axis to log scale
    --ext=<ext>                   Extension to read (some data files have multiple extensions, such as MSA data) [default: 1]
"""

from spew import spew
from docopt import docopt

def main():
    
    """Main CLI entrypoint."""
    arguments = docopt(__doc__, options_first=False)
    spew.spew(arguments)