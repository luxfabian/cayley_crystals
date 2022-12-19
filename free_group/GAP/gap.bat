@echo off 
set dir=%~p0
set fname=%1
set gap_dir=C:\Users\flux\AppData\Local\GAP-4.12.1\runtime\bin\

%gap_dir%bash --login /run-gap-local-vars.sh %dir% %fname%

