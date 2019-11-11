import sys
import os
import shutil
import argparse
import subprocess
from pathlib import Path

import time
import logging

import ProgramData as data

# Set up logging
log = "coala.log"
logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# console handler  
console = logging.StreamHandler()  
console.setLevel(logging.INFO)  
logging.getLogger("").addHandler(console)

# check if the file has an accepted extension
def CheckExt(choices):
    class Act(argparse.Action):
        def __call__(self,parser,namespace,fname,option_string=None):
            ext = os.path.splitext(fname)[1][1:]
            if ext not in choices:
                option_string = '({})'.format(option_string) if option_string else ''
                parser.error("file doesn't end with one of {}{}".format(choices,option_string))
            else:
                setattr(namespace,self.dest,fname)

    return Act

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--mol", dest = 'mol2_filename', help="input of a list of mol2 ligands", action=CheckExt({'mol2'}))
parser.add_argument("-p", "--prot", dest = 'protein_mol2', help="protein mol2 file with charges", action=CheckExt({'mol2'}))
parser.add_argument("-i", "--in", dest = 'in_file', help="docking input file", action=CheckExt({'in'}))
parser.add_argument("-d", "--dms", dest = 'dms_file', help="surface file", action=CheckExt({'dms'}))

args = parser.parse_args()
cwd = os.getcwd()
logging.debug(args)

print(args)
data.mol2Input = args.mol2_filename

line = []
for char in data.mol2Input[::-1]:
	if char != '/':
		line.append(char)
	elif char == '/':
		break

for i in line[::-1]:
	data.mol2File += i

