import os
import sys

lib_dir = os.path.join(os.path.dirname(__file__), "..", "..")
abs_path = os.path.abspath(lib_dir)

sys.path.extend([abs_path])