#
# Uses py2exe to perform the build process when running 'setup_TL.py'.
#
# If everything works well, you should find a subdirectory named 'dist'
# containing some files, with TravLITE.exe being amoung them.


from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

opts = {'py2exe': {'includes': [],
                   'excludes': ['_gtkagg', '_tkagg', '_agg2', 'bsddb', 'curses',
                                'email', 'pywin.debugger', 'pywin.debugger.dbgcon',
                                'pywin.dialogs', '_cairo', '_cocoaagg', '_fltkagg',
                                '_gtk', '_gtkcairo', 'tcl', 'Tkconstants', 'Tkinter'],
                   'packages': [],
                   'dll_excludes': ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll',
                                    'tcl84.dll', 'tk84.dll']
                  }
        }
 
data_files = [
                  (r'.', [r'C:\windows\system32\MSVCP71.dll']),
                  (r'.', [r'C:\windows\system32\MSVCR71.dll']),
                  (r'.', [r'C:\Python25\MSVCP90.dll']),
                  (r'.', [r'C:\Python25\MSVCR90.dll'])
              ]

setup(
    
# for console program use "console = [{'script': 'TravLITE.py'}]"
# for windows program use "windows = [{'script': 'TravLITE.pyw'}]"
      
    console = [{'script': 'TravLITE.py'}],

    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = '1.0.0',
    description = 'LITE Traveller CharGen',
    name = 'TravLITE',
    options = opts,
    data_files = data_files,    
)
