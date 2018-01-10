#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import getopt, sys

from modules import initialize_lcd, onError, usage

try:
    myopts, args = getopt.getopt(sys.argv[1:],
                                 'vh',
                                 ['verbose', 'help'])

except getopt.GetoptError as e:
    onError(1, str(e))
    
if len(sys.argv) == 1:  # no options passed
    onError(2, 2)
    
for option, argument in myopts:
    if option in ('-v', '--verbose'):  # verbose output
        verbose = True
    elif option in ('-h', '--help'):  # display help text
        usage(0)
    

lcd = initialize_lcd()

print lcd







