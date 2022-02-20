"""
Usage:
    spew <pattern> [--aspect=<ratio> --nozero]
    spew <pattern> ...

Options:
    -h, --help                    Show this help
    --aspect=<ratio>              Set initial aspect ratio of plot [default: 2]
    --nozero                      If the spectra are padded with 0s, this removes them. 
"""

from spew import spew
from docopt import docopt

def main():
    
    """Main CLI entrypoint."""
    arguments = docopt(__doc__, options_first=False)
    spew.spew(arguments)