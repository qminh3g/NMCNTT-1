import os
import sys
from cx_Freeze import setup, Executable


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
files = {"include_files": ["CharacterSelection.py", "ImageAssets.py", "PlayGame.py", "ResultScreen.py", "StartRacing.py" ], "packages": []}




syspath = r"C:\Users\Surface Pro 6\AppData\Local\Programs\Python\Python38-32\DLLs"

buildOptions = dict(
    packages=[],
    excludes=[],
    include_files=[syspath + '/tcl86t.dll', syspath + '/tk86t.dll', "StartRacing.py"]
)

executables = [
    Executable('PJ-HorseBetRacingGame.py', base="Win32GUI")
]

setup(name='Pet Racing',
      version='0.0.1',
      options=dict(build_exe=buildOptions),
      description='Project NMCNTT 1',
      executables=executables
      )