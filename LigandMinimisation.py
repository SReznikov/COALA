import sys
import os
import subprocess

import time
import logging

import ProgramData as data
import AcrylamideFunctions as function
from FileLoading import cwd as cwd
# from LigandProcess import input_molecule as input_molecule

class Minimization():
	
	# sections = {}

	# atom_list_new = {}
	# bond_list_new = {}

	# range_of_atoms_new = None
	# range_of_bonds_new = None
	# starting_range_of_atoms_new = None
	# starting_range_of_bonds_new = None

	# section_num_gaff = 0
	# H_to_remove = None


	def __init__(self):
		super(Minimization, self).__init__()

		logging.info("Preparing the ligand molecule")


	# def charge_calc(atom_list_new_in, range_of_atoms_new):

	# 	negative_charges = []
	# 	positive_charges = []

	# 	data.atom_list_new = atom_list_new_in
	# 	range_of_atoms_new = range_of_atoms_new

	# 	for c in range(range_of_atoms_new):
	# 		c += 1

	# 		for item in data.atom_list_new["atom_%s" % c]["charge"]:

	# 			if float(item) < 0:
	# 				for i in data.atom_list_new["atom_%s" % c]["charge"]:
	# 					negative_charges.append(float(i))

	# 			if float(item) > 0:
	# 				for i in data.atom_list_new["atom_%s" % c]["charge"]:
	# 					positive_charges.append(float(i))

	# 	return round(sum(negative_charges), 4), round(sum(positive_charges), 4)

	def acpype(file, signal):

		if signal == 0:
			return

		if signal == 1:
			logging.info("ACPYPE running..... have some patience")
			cmd = ['acpype', '-i' '%s' % file]
			p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
			for line in p.stdout:
			    logging.info(line)
			p.wait()
			logging.info(p.returncode)

		if signal == 2:
			logging.info("ACPYPE running")
			logging.info(file)
			
			cmd = ['acpype', '-i' '%s' % file , '-cuser']
			p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
			for line in p.stdout:
			    logging.info(line)
			p.wait()
			logging.info(p.returncode)

	def deprotonation(signal): #ligand deprotonation??

		logging.info(signal)
		data.MinSection()

		# for n in range(5):
		# 	self.sections["section_%s" %n] = {}
		# 	self.sections["section_%s" %n]["name"] = []
		# 	self.sections["section_%s" %n]["lines"] = []


		def loading():
			print(data.MinSection.sections.keys())
			for line in new_mol2:
				if line.startswith('@'):
					data.MinSection.section_num_gaff += 1
					print(data.MinSection.section_num_gaff)
					data.MinSection.sections["section_%s" % data.MinSection.section_num_gaff]["name"].append(line)

				elif not line.startswith('@'):
					if len(line) > 1:	
						data.MinSection.sections["section_%s" % data.MinSection.section_num_gaff]["lines"].append(line)

			data.range_of_atoms_new = len(data.MinSection.sections["section_%s" %2]["lines"])
			data.range_of_bonds_new = len(data.MinSection.sections["section_%s" %3]["lines"]) 
			data.starting_range_of_atoms_new = len(data.MinSection.sections["section_%s" %2]["lines"]) 
			data.starting_range_of_bonds_new = len(data.MinSection.sections["section_%s" %3]["lines"]) 

		if signal == 0:
			logging.info("loading file")
			with open(cwd+"/new_coords_temp.mol2") as new_mol2:
				loading()

		if signal == 1:
			logging.info("loading file from acpype")


			with open(cwd+"/new_coords_temp.acpype/new_coords_temp_bcc_gaff.mol2") as new_mol2:
				loading()

		for i in range(data.range_of_atoms_new):
			i += 1
			data.atom_list_new["atom_%s" % i] = {}
			data.bond_list_new["bond_%s" % i] = {}

			data.atom_list_new["atom_%s" % i]["atom_id"] = []
			data.atom_list_new["atom_%s" % i]["atom_name"] = []
			data.atom_list_new["atom_%s" % i]["x_coord"] = []
			data.atom_list_new["atom_%s" % i]["y_coord"] = []
			data.atom_list_new["atom_%s" % i]["z_coord"] = []
			data.atom_list_new["atom_%s" % i]["atom_type"] = []
			data.atom_list_new["atom_%s" % i]["lig_name"] = []
			data.atom_list_new["atom_%s" % i]["charge"] = []

		for b in range(data.range_of_bonds_new):
			b += 1

			data.bond_list_new["bond_%s" % b]["bond_id"] = []
			data.bond_list_new["bond_%s" % b]["a1"] = []
			data.bond_list_new["bond_%s" % b]["a2"] = []
			data.bond_list_new["bond_%s" % b]["type"] = []


		for n in range(5):

			short_name = (str(data.MinSection.sections["section_%s" % n]["name"]).strip('[' + '\'' + '@' + '<' + '\\' + 'n' + '\'' + ']'))

			if short_name == "TRIPOS>ATOM":

				for line in data.MinSection.sections["section_%s" %n]["lines"]:
	
					col = line.split()

					if len(col):
						atom = col[0]
						data.atom_list_new["atom_%s" % atom]["atom_id"].append(col[0])
						data.atom_list_new["atom_%s" % atom]["atom_name"].append(col[1])
						data.atom_list_new["atom_%s" % atom]["x_coord"].append(col[2])
						data.atom_list_new["atom_%s" % atom]["y_coord"].append(col[3])
						data.atom_list_new["atom_%s" % atom]["z_coord"].append(col[4])
						data.atom_list_new["atom_%s" % atom]["atom_type"].append(col[5])
						data.atom_list_new["atom_%s" % atom]["lig_name"].append(col[7])
						data.atom_list_new["atom_%s" % atom]["charge"].append(col[8])

			if short_name == "TRIPOS>BOND":
				for line in data.MinSection.sections["section_%s" %n]["lines"]:

					col = line.split()

					if len(col):
						bond = col[0]
						data.bond_list_new["bond_%s" % bond]["bond_id"] = col[0]
						data.bond_list_new["bond_%s" % bond]["a1"] = col[1]
						data.bond_list_new["bond_%s" % bond]["a2"] = col[2]
						data.bond_list_new["bond_%s" % bond]["type"] = col[3]

		

		atom_list_new_in = data.atom_list_new
		charges_sum = function.charge_calc(atom_list_new_in, data.range_of_atoms_new)

		for e in range(data.range_of_atoms_new):
			e += 1

			if data.atom_list_new["atom_%s" % e]["atom_name"] == ['Hr']:
				data.H_to_remove = data.atom_list_new["atom_%s" % e]["atom_id"]
				for h in data.H_to_remove:
					data.H_to_remove = h
				
				del data.atom_list_new["atom_%s" % e]
				data.range_of_atoms_new -= 1

		atom_list_new_in = data.atom_list_new
		charges_sum = function.charge_calc(atom_list_new_in, data.range_of_atoms_new)
		overall_charge = sum(charges_sum)

		for f in range(data.range_of_bonds_new):
			f += 1

			if data.H_to_remove == data.bond_list_new["bond_%s" % f]["a1"] or data.H_to_remove == data.bond_list_new["bond_%s" % f]["a2"]:

				if data.H_to_remove == data.bond_list_new["bond_%s" % f]["a1"]:
					carbon_to_charge = data.bond_list_new["bond_%s" % f]["a2"]

				elif data.H_to_remove == data.bond_list_new["bond_%s" % f]["a2"]:
					carbon_to_charge = data.bond_list_new["bond_%s" % f]["a1"]

				del data.bond_list_new["bond_%s" % f]
				data.range_of_bonds_new -= 1

		for a in range(data.range_of_atoms_new):
			a += 1

			for x in data.atom_list_new["atom_%s" % a]["atom_id"]:
				current_carbon = x

			if current_carbon == carbon_to_charge:
				for c in data.atom_list_new["atom_%s" % a]["charge"]:
					carbon_charge = float(c)

				needed_charge = (1 - (overall_charge)) + (carbon_charge)

				data.atom_list_new["atom_%s" % carbon_to_charge]["charge"] = []
				data.atom_list_new["atom_%s" % carbon_to_charge]["charge"].append(needed_charge)

		atom_list_new_in = data.atom_list_new
		charges_sum = function.charge_calc(atom_list_new_in, data.range_of_atoms_new)
		overall_charge = sum(charges_sum)

	def write_mol2_gaff(input_molecule):
		logging.info("Writing the 2nd mol2 file")

		with open(input_molecule+"_charge.mol2", "w") as mol2:
			for i in range(5):
				short_name = (str(data.MinSection.sections["section_%s" %i]["name"]).strip('[' + ']' + '\'' + '\\' + 'n'))

				if short_name == "@<TRIPOS>MOLECULE":
					num_of_new_atoms = data.range_of_atoms_new - data.starting_range_of_atoms_new
					num_of_new_bonds = data.range_of_bonds_new - data.starting_range_of_bonds_new

					col = data.MinSection.sections["section_%s" %1]["lines"][1].split()

					if len(col):

						col[0] = int(col[0])
						col[0] += num_of_new_atoms
						atom = col[0]

						col[1] = int(col[1])
						col[1] += num_of_new_bonds
						bond = col[1]

					data.MinSection.sections["section_%s" %1]["lines"][1] = (str(atom) + ' ' + str(bond) + ' ' + str(col[2]) + ' ' + str(col[3]) + ' ' + str(col[4] + '\n'))

					mol2.write(short_name + '\n')
					for line in data.MinSection.sections["section_%s" %1]["lines"]:

						mol2.write(str(line))

				if short_name == "@<TRIPOS>ATOM":
					mol2.write(short_name + '\n')
					for atom in range(data.range_of_atoms_new):
						atom += 1

						for c in data.atom_list_new["atom_%s" % atom]["x_coord"]:
							x_coord_n = c
						for c in data.atom_list_new["atom_%s" % atom]["y_coord"]:
							y_coord_n = c
						for c in data.atom_list_new["atom_%s" % atom]["z_coord"]:
							z_coord_n = c
						for c in data.atom_list_new["atom_%s" % atom]["charge"]:
							charge_n = c

						atom_name = str(data.atom_list_new["atom_%s" % atom]["atom_name"]).strip('[' + ']' + '\'')
						atom_type = str(data.atom_list_new["atom_%s" % atom]["atom_type"]).strip('[' + ']' + '\'')
						ligand_name = str(data.atom_list_new["atom_%s" % atom]["lig_name"]).strip('[' + ']' + '\'')

						if len(str(atom)) == 1:
							space_1a = '      '
						elif len(str(atom)) == 2:
							space_1a = '     '

						if len(atom_name) == 2:
							space_3a = '          '
						elif len(atom_name) == 3:
							space_3a = '         '
						elif len(atom_name) == 4:
							space_3a = '        '

						if '-' in x_coord_n:
							neg_space = ''
						else:
							neg_space = ' '

						if '-' in y_coord_n:
							space_4a = '    '
						else:
							space_4a = '     '

						if '-' in z_coord_n:
							space_5a = '    '
						else:
							space_5a = '     '

						if len(atom_type) == 1:
							space_6a =  '          '
						elif len(atom_type) >= 2:
							space_6a =  '         '

						if '-' in str(charge_n):
							space_7a = '      '
						else:
							space_7a = '       '

						mol2.write(space_1a + str(atom) + ' ' + atom_name + space_3a + neg_space + str("%.4f" % float(x_coord_n)) + space_4a + str("%.4f" % float(y_coord_n)) + space_5a + str("%.4f" % float(z_coord_n)) + ' ' + atom_type + space_6a + "1 " + ligand_name + space_7a + str("%.6f" % float(charge_n)) + '\n')

				if short_name == "@<TRIPOS>BOND":
					mol2.write(short_name + '\n')

					for c in range(data.range_of_bonds_new):
						c += 1

						a1 = data.bond_list_new["bond_%s" % c]["a1"]
						a2 = data.bond_list_new["bond_%s" % c]["a2"]
						b_typ = data.bond_list_new["bond_%s" % c]["type"]

						if len(str(c)) == 1:
							space_1b = '     '
						elif len(str(c)) == 2:
							space_1b = '    '

						if len(str(a1)) == 1:
							space_2b = '     '
						elif len(str(a1)) == 2:
							space_2b = '    '

						if len(str(a2)) == 1:
							space_3b = '     '
						elif len(str(a2)) == 2:
							space_3b = '    '
							
						mol2.write(space_1b + str(c) + space_2b + str(a1) + space_3b + str(a2) + ' ' + str(b_typ) + '\n')

				if short_name == "@<TRIPOS>SUBSTRUCTURE":
					mol2.write(short_name + '\n')
					for line in data.MinSection.sections["section_%s" %4]["lines"]:
						mol2.write(str(line))
