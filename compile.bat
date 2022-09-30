@echo off
title Compile
rem --enable-plugin=numpy  --onefile  --enable-plugin=tk-inter
rem set /P file="which file would you like to compile? "
py -m nuitka "1-2-3 sound effects.py" --standalone --windows-icon-from-ico=icon.ico --enable-plugin=numpy

pause