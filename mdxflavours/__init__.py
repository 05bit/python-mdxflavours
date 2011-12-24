import os
import sys
dir = os.path.realpath(os.path.dirname(__file__))
if not dir in sys.path:
    sys.path.append(dir)