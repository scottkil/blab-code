# basic script to that new users can run to install the dcimg package for later use through MATLAB
# dcimg is a package used to work with .dcimg files that are created when imaging with Hamamatsu cameras
# More info on dcimg found here: https://lens-biophotonics.github.io/dcimg/

import sys
import subprocess

# implement pip as a subprocess and install dcimg package
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'dcimg'])
