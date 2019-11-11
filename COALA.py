#!/usr/bin/env python3

# COALA
# Copyright (C) 2018  Sylvia Reznikov
# email contact: s.reznikov@newcastle.ac.uk

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
import os
import shutil
import argparse
import subprocess
from pathlib import Path

import time
import logging

import re
import math
import numpy as np

import ProgramData as data
import FileLoading
import LigandProcess 
import ProteinProcess
import DockingProcess
import ScoringProcess

# FileLoading()
# LigandProcess()
# ProteinPreparation().protein_load()
# ProteinPreparation().protein_deprotonation()
# ProteinPreparation().write_mol2_protein()


# protein_load()
# 		protein_deprotonation()
		
# 		write_mol2_protein()
# import AcrylamideMapping
# import AcrylamideReaction
# import AcrylamideFunctions
# import LigandMinimisation


# # Set up logging
# log = "coala.log"
# logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# # console handler  
# console = logging.StreamHandler()  
# console.setLevel(logging.INFO)  
# logging.getLogger("").addHandler(console)

# # check if the file has an accepted extension
# def CheckExt(choices):
#     class Act(argparse.Action):
#         def __call__(self,parser,namespace,fname,option_string=None):
#             ext = os.path.splitext(fname)[1][1:]
#             if ext not in choices:
#                 option_string = '({})'.format(option_string) if option_string else ''
#                 parser.error("file doesn't end with one of {}{}".format(choices,option_string))
#             else:
#                 setattr(namespace,self.dest,fname)

#     return Act

# # with open ('args.txt', 'w') as fp:
# # 	fp.write('-f\nbar')

# parser = argparse.ArgumentParser()

# parser.add_argument("-c", "--mol", dest = 'mol2_filename', help="input of a list of mol2 ligands", action=CheckExt({'mol2'}))
# parser.add_argument("-p", "--prot", dest = 'protein_mol2', help="protein mol2 file with charges", action=CheckExt({'mol2'}))
# parser.add_argument("-i", "--in", dest = 'in_file', help="docking input file", action=CheckExt({'in'}))
# parser.add_argument("-d", "--dms", dest = 'dms_file', help="surface file", action=CheckExt({'dms'}))

# args = parser.parse_args()
# # args.Namespace(f='bar')

# cwd = os.getcwd()
# logging.debug(args)
# print(type(args.mol2_filename))

# print(args)
# data.mol2Input = args.mol2_filename
# print(data.mol2Input)

# LigandProcess()
# ProteinProcess()

# DockingProcess()
# ScoringProcess()