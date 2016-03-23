This is the pyunit test framework to exclusively test an application, in our case the application is "Alarm Application".

Framework structure:
=================
Framework
    -application
    -scripts
    -results
    -lib
    -harness
    -docs

How to run:
=========
./harness --pythonpath=<pythonpath to import modules> --testscript=<script to execute, under scripts/>  [--debug]

Eg:
./harness --pythonpath=/Users/pgovindr/Documents/workspace/AllPython/calm.io/framework/final_check_framework/framework --testscript=scripts/load_testing.py
./harness --pythonpath=/Users/pgovindr/Documents/workspace/AllPython/calm.io/framework/final_check_framework/framework --testscript=scripts/load_testing.py --debug


Help
=====
blr-mpshv:framework pgovindr$ ./harness -h
usage: harness [-h] --pythonpath PYTHONPATH --testscript TESTSCRIPT [--debug]

optional arguments:
  -h, --help            show this help message and exit
  --pythonpath PYTHONPATH
                        Provide a python path , --pythonpath
  --testscript TESTSCRIPT
                        Provide a script location , --testscript
  --debug               to display debug logs
blr-mpshv:framework pgovindr$

