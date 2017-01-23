import cx_Freeze

executables = [cx_Freeze.Executable('slither.py')]

cx_Freeze.setup(
    name='slither',
	version='1.1',
    options={'build_exe':{'packages':['pygame'],'include_files': \
            ['apple2.png','snakehead.png']}},
    description='Slither game tutorial',
    executables=executables
    )
