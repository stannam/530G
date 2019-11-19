# -*- mode: python ; coding: utf-8 -*-
import os
import sys

block_cipher = None

lg_path = os.getcwd()

a = Analysis([os.path.join(lg_path, 'interface.py')],
             pathex=[lg_path],
             binaries=[],
             datas=[('data', 'data')],
             hiddenimports=['PyQt5', 'editdistance', 'regex', 'igraph', 'igraph.vendor.texttable'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='LanguageGuessing',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False)
		  
if sys.platform == 'darwin':
   app = BUNDLE(exe, name='LanguageGuessing.app')