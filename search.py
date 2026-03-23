import os
import sys


#would just say "python3", but modules are in conda environment
for i in range(5):
    os.system(f"{sys.executable} generate.py")
    os.system(f"{sys.executable} simulate.py")