###############################
######## PART 1 ###############
###############################
# import AcrylamideReaction
import os
import time
import logging
import re
import ProgramData as data
from AcrylamideReaction import AcrylamideReaction
from FileLoading import cwd as cwd
from FileLoading import args as args
from LigandMinimisation import Minimization as minim

# if args.mol2_filename:

# input mol2 of the ligand
with open(data.mol2Input) as input_mol2:
	input_file = " ".join(re.split("[^a-zA-Z_]*", str(data.mol2Input)))
	print(input_file)
	input_file = input_file[:-5]
	print(input_file, "input file")

	with open(input_file+"_temp.mol2", "w") as temp:

		# data.mol_id = 0
	
		for line in input_mol2:

			if line.startswith('@<TRIPOS>MOLECULE'):
				data.mol_id += 1
				logging.info(data.mol_id)
				temp.write(str(data.mol_id) + ' ' + line)

			if line.startswith('@<TRIPOS>ATOM'):
				temp.write(str(data.mol_id) + ' ' +  line )

			if line.startswith('@<TRIPOS>BOND'):
				temp.write(str(data.mol_id) + ' ' +  line )

			if line.startswith('@<TRIPOS>SUBSTRUCTURE'):
				temp.write(str(data.mol_id) + ' ' +  line )
				
			if not line.startswith('@'):
				temp.write(str(data.mol_id) + ' ' + line)
	
# separate ligands 
for molecule in range(data.mol_id):
	molecule += 1

	molecule = str(molecule)

	data.Section()
	# sections = {}
	# for n in range(5):
	# 	sections["section_%s" %n] = {}
	# 	sections["section_%s" %n]["name"] = []
	# 	sections["section_%s" %n]["lines"] = []

	data.section_num = 0
	# data.SectionTemplate()

	with open(input_file+"_temp.mol2") as input_temp_mol2:
	
		for line in input_temp_mol2:

			if line.startswith(molecule):
				line = line[2:]

				if line.startswith('@'):

					data.section_num = data.section_num + 1
					data.Section.sections["section_%s" %data.section_num]["name"].append(line)

				elif not line.startswith('@'):
					if len(line) > 1:
					
						data.Section.sections["section_%s" %data.section_num]["lines"].append(line)

	data.range_of_atoms = len(data.Section.sections["section_%s" %2]["lines"]) 
	data.range_of_bonds = len(data.Section.sections["section_%s" %3]["lines"]) 
	data.starting_range_of_atoms = len(data.Section.sections["section_%s" %2]["lines"]) 
	data.starting_range_of_bonds = len(data.Section.sections["section_%s" %3]["lines"]) 

	input_molecule = "mol_" + molecule + "_" + args.mol2_filename[:-5]
	


	





	# atom_list = {}
	# bond_list = {}
	# atom and bond list definitions
	# for i in range(data.range_of_atoms):
	# 	i = i + 1
	# 	data.i = i
	# 	atom_list["atom_%s" % i] = {}
	# 	bond_list["bond_%s" % i] = {}

	# 	atom_list["atom_%s" % i]["atom_id"] = []
	# 	atom_list["atom_%s" % i]["atom_name"] = []
	# 	atom_list["atom_%s" % i]["x_coord"] = []
	# 	atom_list["atom_%s" % i]["y_coord"] = []
	# 	atom_list["atom_%s" % i]["z_coord"] = []
	# 	atom_list["atom_%s" % i]["atom_type"] = []
	# 	atom_list["atom_%s" % i]["lig_name"] = []
	# 	atom_list["atom_%s" % i]["charge"] = []

	# 	bond_list["bond_%s" % i]["bond_id"] = []
	# 	bond_list["bond_%s" % i]["a1"] = [] # origin arom
	# 	bond_list["bond_%s" % i]["a2"] = [] # target atom
	# 	bond_list["bond_%s" % i]["bond_type"] = []


	# resetTemplate()
	# functions.reaction()
	data.SectionTemplate()
	print("called reaction func")
	# print(data.atom_list.values())
	AcrylamideReaction()

	# cwd = os.getcwd()
	file_path = cwd+"/new_coords_temp.mol2"
	logging.info(file_path)
	# minim = Minimization()

	while not os.path.exists(file_path):
	    time.sleep(1)



	if os.path.isfile(file_path):
	    # read file
	    minim()
	    if data.SectionTemplate.atom_list["atom_%s" % 1]["charge"] != []:
	    	signal = 0
	    	logging.info("charge present")
	    	logging.info(data.SectionTemplate.atom_list["atom_%s" % 1]["charge"])
	    	file = None
	    	minim.acpype(file, signal)

	    elif data.SectionTemplate.atom_list["atom_%s" % 1]["charge"] == []:
	    	signal = 1
	    	logging.info("no charges")
	    	file = 'new_coords_temp.mol2'
	    	minim.acpype(file, signal)


	    minim.deprotonation(signal)
	    minim.write_mol2_gaff(input_molecule)
	    file = (input_molecule+"_charge.mol2")
	    logging.info(file)
	    signal = 2
	    minim.acpype(file, signal)
	else:
	    raise ValueError("%s isn't a file!" % file_path)

	#remove new_coords_temp.mol2
	# print("Removing temp files...")
	# os.remove(file_path)
	# shutil.rmtree(cwd+"/new_coords_temp.acpype")

	logging.info("I guess that's a success. ciao")

		# for item in range(data.mol_id):
# reaction()





# def reaction():
			
			
# 	AcrylamideReaction()

	# # cwd = os.getcwd()
	# file_path = cwd+"/new_coords_temp.mol2"
	# logging.info(file_path)
	# minim = Minimization()

	# while not os.path.exists(file_path):
	#     time.sleep(1)

	# if os.path.isfile(file_path):
	#     # read file
	#     if atom_list["atom_%s" % 1]["charge"] != []:
	#     	signal = 0
	#     	logging.info("charge present")
	#     	logging.info(atom_list["atom_%s" % 1]["charge"])
	#     	file = None
	#     	minim.acpype(file, signal)

	#     elif atom_list["atom_%s" % 1]["charge"] == []:
	#     	signal = 1
	#     	logging.info("no charges")
	#     	file = 'new_coords_temp.mol2'
	#     	minim.acpype(file, signal)


	#     minim.deprotonation(signal)
	#     minim.write_mol2_gaff()
	#     file = (input_molecule+"_charge.mol2")
	#     logging.info(file)
	#     signal = 2
	#     minim.acpype(file, signal)
	# else:
	#     raise ValueError("%s isn't a file!" % file_path)

	# #remove new_coords_temp.mol2
	# # print("Removing temp files...")
	# # os.remove(file_path)
	# # shutil.rmtree(cwd+"/new_coords_temp.acpype")

	# logging.info("I guess that's a success. ciao")

		# for item in range(data.mol_id):
# reaction()