#!/bin/bash
# Bash wrapper around python script - to convert mib to pysnmp format



#python3  ../lib/mibdump.py --generate-mib-texts --destination-format pysnmp MOXA-IO-E1242-MIB


python3 ../lib/mibdump.py --generate-mib-texts --destination-format=pysnmp  ./moxa-e1242-v1.2.mib