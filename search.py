import os
import sys
from hillclimber import HILL_CLIMBER

#would just say "python3", but modules are in conda environment
#for i in range(5):
#    os.system(f"{sys.executable} generate.py")
#    os.system(f"{sys.executable} simulate.py")
hc = HILL_CLIMBER()
print("Initial random solution:")
hc.parent.Evaluate("GUI")
hc.Evolve("DIRECT")
hc.Show_Best()