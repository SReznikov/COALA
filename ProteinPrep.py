import time
import logging
# from FileLoading import args as args
import re

import ProgramData as data

class ProteinPreparation():
	print("protein prep")

	# __init__
	# def init():

	# logging.info("Preparing the protein")
	# print("Preparing the protein")

	# protein_load()
	# protein_deprotonation()
	
	# write_mol2_protein()



		# sections_protein = {}

		# atom_list_prot = {}
		# bond_list_prot = {}
		# substructure = {}

		# range_of_atoms_prot = None
		# range_of_bonds_prot = None
		# substructure_range = None
		# starting_range_of_atoms_prot = None
		# starting_range_of_bonds_prot = None
		# starting_substructure_range = None

		# section_num = 0

		# cysteine_atoms = []


	def __init__(self):
		super(ProteinPreparation, self).__init__()

	# 	logging.info("Preparing the protein")
		print("Preparing the protein")

	# 	self.protein_load()
		self.protein_deprotonation()
		
		self.write_mol2_protein()

	def charge_calc(self, atom_list_prot_in, range_of_atoms_prot):

		negative_charges = []
		positive_charges = []

		data.atom_list_prot = atom_list_prot_in
		range_of_atoms_prot = range_of_atoms_prot

		for c in range(range_of_atoms_prot):
			c += 1

			for item in data.atom_list_prot["atom_%s" % c]["charge"]:

				if float(item) < 0:
					for i in data.atom_list_prot["atom_%s" % c]["charge"]:
						negative_charges.append(float(i))

				if float(item) > 0:
					for i in data.atom_list_prot["atom_%s" % c]["charge"]:
						positive_charges.append(float(i))

		logging.info("charges")
		logging.info(round(sum(negative_charges), 4))
		logging.info(round(sum(positive_charges), 4))
		return round(sum(negative_charges), 4), round(sum(positive_charges), 4)

	


	# def protein_load(self):

	# 	with open(args.protein_mol2) as protein:

	# 		for line in protein:

	# 			if line.startswith('@'):

	# 				data.section_num_protein += 1
	# 				data.ProteinSection.sections_protein["section_%s" % data.section_num_protein]["name"].append(line)

	# 			elif not line.startswith('@'):
	# 				if len(line) > 1:	
	# 					data.ProteinSection.sections_protein["section_%s" % data.section_num_protein]["lines"].append(line)

	# 		data.range_of_atoms_prot = len(data.ProteinSection.sections_protein["section_%s" %2]["lines"])
	# 		data.range_of_bonds_prot = len(data.ProteinSection.sections_protein["section_%s" %3]["lines"])
	# 		data.substructure_range = len(data.ProteinSection.sections_protein["section_%s" %4]["lines"])
	# 		data.starting_range_of_atoms_prot = len(data.ProteinSection.sections_protein["section_%s" %2]["lines"]) 
	# 		data.starting_range_of_bonds_prot = len(data.ProteinSection.sections_protein["section_%s" %3]["lines"]) 
	# 		data.starting_substructure_range = len(data.ProteinSection.sections_protein["section_%s" %4]["lines"]) 


	# protein_load()




	def protein_deprotonation(self):
		# res_number = []
		# protein_charge = []
		data.ProteinLists()

		# for n in range(5):
		# 	self.sections_protein["section_%s" %n] = {}
		# 	self.sections_protein["section_%s" %n]["name"] = []
		# 	self.sections_protein["section_%s" %n]["lines"] = []

		# def protein_load():

		# 	with open(args.protein_mol2) as protein:

		# 		for line in protein:

		# 			if line.startswith('@'):

		# 				self.section_num += 1
		# 				self.sections_protein["section_%s" % self.section_num]["name"].append(line)

		# 			elif not line.startswith('@'):
		# 				if len(line) > 1:	
		# 					self.sections_protein["section_%s" % self.section_num]["lines"].append(line)

		# 		self.range_of_atoms_prot = len(self.sections_protein["section_%s" %2]["lines"])
		# 		self.range_of_bonds_prot = len(self.sections_protein["section_%s" %3]["lines"])
		# 		self.substructure_range = len(self.sections_protein["section_%s" %4]["lines"])
		# 		self.starting_range_of_atoms_prot = len(self.sections_protein["section_%s" %2]["lines"]) 
		# 		self.starting_range_of_bonds_prot = len(self.sections_protein["section_%s" %3]["lines"]) 
		# 		self.starting_substructure_range = len(self.sections_protein["section_%s" %4]["lines"]) 


		# protein_load()

		# for i in range(self.range_of_atoms_prot):
		# 	i += 1
		# 	self.atom_list_prot["atom_%s" % i] = {}

		# 	self.atom_list_prot["atom_%s" % i]["atom_id"] = []
		# 	self.atom_list_prot["atom_%s" % i]["atom_name"] = []
		# 	self.atom_list_prot["atom_%s" % i]["x_coord"] = []
		# 	self.atom_list_prot["atom_%s" % i]["y_coord"] = []
		# 	self.atom_list_prot["atom_%s" % i]["z_coord"] = []
		# 	self.atom_list_prot["atom_%s" % i]["atom_type"] = []
		# 	self.atom_list_prot["atom_%s" % i]["res_num"] = []
		# 	self.atom_list_prot["atom_%s" % i]["res_name"] = []
		# 	self.atom_list_prot["atom_%s" % i]["charge"] = []

		# for b in range(self.range_of_bonds_prot):
		# 	b += 1
		# 	self.bond_list_prot["bond_%s" % b] = {}

		# 	self.bond_list_prot["bond_%s" % b]["bond_id"] = []
		# 	self.bond_list_prot["bond_%s" % b]["a1"] = []
		# 	self.bond_list_prot["bond_%s" % b]["a2"] = []
		# 	self.bond_list_prot["bond_%s" % b]["type"] = []

		# for s in range(self.substructure_range):
		# 	s += 1
		# 	self.substructure["sub_%s" % s] = {}

		# 	self.substructure["sub_%s" % s]["id"] = []
		# 	self.substructure["sub_%s" % s]["resname"] = []
		# 	self.substructure["sub_%s" % s]["atmnum"] = []
		# 	self.substructure["sub_%s" % s]["type"] = []
		# 	self.substructure["sub_%s" % s]["num_1"] = []
		# 	self.substructure["sub_%s" % s]["chain"] = []
		# 	self.substructure["sub_%s" % s]["resname_2"] = []
		# 	self.substructure["sub_%s" % s]["num_2"] = []
		# 	self.substructure["sub_%s" % s]["comment"] = []


		for n in range(5):

			short_name = (str(data.ProteinSection.sections_protein["section_%s" % n]["name"]).strip('[' + '\'' + '@' + '<' + '\\' + 'n' + '\'' + ']'))

			if short_name == "TRIPOS>ATOM":

				for line in data.ProteinSection.sections_protein["section_%s" %n]["lines"]:
		
					col = line.split()

					if len(col):
						atom = col[0]
						data.ProteinLists.atom_list_prot["atom_%s" % atom]["atom_id"].append(col[0])
						data.ProteinLists.atom_list_prot["atom_%s" % atom]["atom_name"].append(col[1])
						data.ProteinLists.atom_list_prot["atom_%s" % atom]["x_coord"].append(col[2])
						data.ProteinLists.atom_list_prot["atom_%s" % atom]["y_coord"].append(col[3])
						data.ProteinLists.atom_list_prot["atom_%s" % atom]["z_coord"].append(col[4])
						data.ProteinLists.atom_list_prot["atom_%s" % atom]["atom_type"].append(col[5])
						data.ProteinLists.atom_list_prot["atom_%s" % atom]["res_num"].append(col[6])
						data.ProteinLists.atom_list_prot["atom_%s" % atom]["res_name"].append(col[7])
						data.ProteinLists.atom_list_prot["atom_%s" % atom]["charge"].append(col[8])

			if short_name == "TRIPOS>BOND":
				for line in data.ProteinSection.sections_protein["section_%s" %n]["lines"]:

					col = line.split()

					if len(col):
						bond = col[0]
						data.ProteinLists.bond_list_prot["bond_%s" % bond]["bond_id"] = col[0]
						data.ProteinLists.bond_list_prot["bond_%s" % bond]["a1"] = col[1]
						data.ProteinLists.bond_list_prot["bond_%s" % bond]["a2"] = col[2]
						data.ProteinLists.bond_list_prot["bond_%s" % bond]["type"] = col[3]

			if short_name == "TRIPOS>SUBSTRUCTURE":
				for line in data.ProteinSection.sections_protein["section_%s" %n]["lines"]:
					# print(line)

					col = line.split()

					if len(col) == 9:
						sub = col[0]
						data.ProteinLists.substructure["sub_%s" % sub]["id"] = col[0]
						data.ProteinLists.substructure["sub_%s" % sub]["resname"] = col[1]
						data.ProteinLists.substructure["sub_%s" % sub]["atmnum"] = col[2]
						data.ProteinLists.substructure["sub_%s" % sub]["type"] = col[3]
						data.ProteinLists.substructure["sub_%s" % sub]["num_1"] = col[4]
						data.ProteinLists.substructure["sub_%s" % sub]["chain"] = col[5]
						data.ProteinLists.substructure["sub_%s" % sub]["resname_2"] = col[6]
						data.ProteinLists.substructure["sub_%s" % sub]["num_2"] = col[7]
						data.ProteinLists.substructure["sub_%s" % sub]["comment"] = col[8]
					elif len(col) == 8:
						sub = col[0]
						data.ProteinLists.substructure["sub_%s" % sub]["id"] = col[0]
						data.ProteinLists.substructure["sub_%s" % sub]["resname"] = col[1]
						data.ProteinLists.substructure["sub_%s" % sub]["atmnum"] = col[2]
						data.ProteinLists.substructure["sub_%s" % sub]["type"] = col[3]
						data.ProteinLists.substructure["sub_%s" % sub]["num_1"] = col[4]
						data.ProteinLists.substructure["sub_%s" % sub]["chain"] = col[5]
						data.ProteinLists.substructure["sub_%s" % sub]["resname_2"] = col[6]
						data.ProteinLists.substructure["sub_%s" % sub]["num_2"] = col[7]



		# user input of what cysteine to deprotonate
		cys_to_load = int(input("Cysteine to deprotonate: "))

		logging.info("loading CYS " + str(cys_to_load))

		loaded_cys = cys_to_load

		for i in range(data.range_of_atoms_prot):
			i += 1
			for item in data.ProteinLists.atom_list_prot["atom_%s" % i]["res_num"]:

				if int(item) == loaded_cys:
					data.cysteine_atoms.append(i)

		logging.info(data.cysteine_atoms)

		# remove H from sulfur of that CYS
		atom_to_delete = None
		sulfur_to_charge = None
		renum_list = []

		for atom in data.cysteine_atoms:
			logging.info(data.ProteinLists.atom_list_prot["atom_%s" % atom]["atom_name"])
			if data.ProteinLists.atom_list_prot["atom_%s" % atom]["atom_name"] == ['HG']:
				logging.info(atom)
				atom_to_delete = data.ProteinLists.atom_list_prot["atom_%s" % atom]["atom_id"]

				for h in atom_to_delete:
					atom_to_delete = h
				
				logging.info("cysteine deprotonated")
				del data.ProteinLists.atom_list_prot["atom_%s" % atom]

		for item in list(data.ProteinLists.atom_list_prot):
			

			key_num = re.findall(r'\d+', item)
			for k in key_num:

				if float(k) > float(atom_to_delete):
					renum_list.append(k)
					

		renum_list.sort(key = int)
		
		for key in renum_list:
			for item in list(data.ProteinLists.atom_list_prot):
				key_num = re.findall(r'\d+', item)
				for k in key_num:	
					if key == k:
						# print(item)
						old_key = int(key)
						new_key = int(key)-1

						data.ProteinLists.atom_list_prot["atom_%s" % new_key] = data.ProteinLists.atom_list_prot["atom_%s" % old_key]

		logging.info(data.ProteinLists.atom_list_prot["atom_808"].values())
		logging.info("atom numbers re-written")
		data.range_of_atoms_prot -= 1


		for f in range(data.range_of_bonds_prot):
			f += 1

			if atom_to_delete == data.ProteinLists.bond_list_prot["bond_%s" % f]["a1"] or atom_to_delete == data.ProteinLists.bond_list_prot["bond_%s" % f]["a2"]:

				if atom_to_delete == data.ProteinLists.bond_list_prot["bond_%s" % f]["a1"]:
					sulfur_to_charge = data.ProteinLists.bond_list_prot["bond_%s" % f]["a2"]

				elif atom_to_delete == data.ProteinLists.bond_list_prot["bond_%s" % f]["a2"]:
					sulfur_to_charge = data.ProteinLists.bond_list_prot["bond_%s" % f]["a1"]

				logging.info(data.ProteinLists.bond_list_prot["bond_%s" % f])
				del_bond_key = data.ProteinLists.bond_list_prot["bond_%s" % f]["bond_id"]
				del data.ProteinLists.bond_list_prot["bond_%s" % f]

				logging.info(sulfur_to_charge)
				# ensure that the sulfur number matches after renumbering of the atoms

				if sulfur_to_charge > atom_to_delete:
					logging.info("sulfur needs to be renumbered")
				elif sulfur_to_charge < atom_to_delete:
					logging.info("sulfur atom num is lower than of the h")
					logging.info("bond deleted" + del_bond_key)

		bond_renum = []
		# change bond keys 
		for bond in list(data.ProteinLists.bond_list_prot):
			# print(bond)

			bond_num = re.findall(r'\d+', bond)
			# print(bond_num)

			for k in bond_num:
				# print(k)

				if float(k) > float(del_bond_key):
					bond_renum.append(k)
					# print(bond_renum)

		bond_renum.sort(key = int)
		# print(bond_renum)
		
		for key in bond_renum:
			for item in list(data.ProteinLists.bond_list_prot):
				key_num = re.findall(r'\d+', item)
				for k in key_num:	
					if key == k:
						# print(item)
						old_key = int(key)
						new_key = int(key)-1

						data.ProteinLists.bond_list_prot["bond_%s" % new_key] = data.ProteinLists.bond_list_prot["bond_%s" % old_key]


					# old_key = k
					# new_key = float(k)-1
					# new_key = int(new_key)

					# self.bond_list_prot["bond_%s" % new_key] = self.bond_list_prot["bond_%s" % old_key]
		
						logging.info(data.ProteinLists.bond_list_prot["bond_%s" % new_key])
		logging.info("bond numbers re-written")
		data.range_of_bonds_prot -= 1

		# change bond ids

		# atom numbers bigger than HG need to be reduced by 1. 
		for b in range(data.range_of_bonds_prot):
			b += 1

			if float(data.ProteinLists.bond_list_prot["bond_%s" % b]["a1"]) > float(atom_to_delete):
				old_atom = data.ProteinLists.bond_list_prot["bond_%s" % b]["a1"]
				new_atom = float(old_atom) - 1
				new_atom = int(new_atom)
				data.ProteinLists.bond_list_prot["bond_%s" % b]["a1"] = new_atom

			if float(data.ProteinLists.bond_list_prot["bond_%s" % b]["a2"]) > float(atom_to_delete):
				old_atom = data.ProteinLists.bond_list_prot["bond_%s" % b]["a2"]
				new_atom = float(old_atom) - 1
				new_atom = int(new_atom)
				data.ProteinLists.bond_list_prot["bond_%s" % b]["a2"] = new_atom

		logging.info(data.ProteinLists.bond_list_prot["bond_1889"])


		for a in range(data.range_of_atoms_prot):
			a += 1

			for x in data.ProteinLists.atom_list_prot["atom_%s" % a]["atom_id"]:
				current_atom = x
		
			if current_atom == sulfur_to_charge:
				for s in data.ProteinLists.atom_list_prot["atom_%s" % a]["charge"]:
					sulfur_charge = float(s)
		
				needed_charge = -0.881 + (sulfur_charge)
				# needed_charge = -1
				# print("needed charhe" , needed_charge)
				data.ProteinLists.atom_list_prot["atom_%s" % sulfur_to_charge]["charge"] = []
				data.ProteinLists.atom_list_prot["atom_%s" % sulfur_to_charge]["charge"].append(needed_charge)


		# change atom numbers in the substructure section 
		for s in range(data.substructure_range):
			s += 1

			if float(data.ProteinLists.substructure["sub_%s" % s]["atmnum"]) > float(atom_to_delete):
				# print(data.ProteinLists.substructure["sub_%s" % s])
				old_atom = data.ProteinLists.substructure["sub_%s" % s]["atmnum"]
				new_atom = float(old_atom) - 1
				new_atom = int(new_atom)
				data.ProteinLists.substructure["sub_%s" % s]["atmnum"] = new_atom


	# write a deprotonated protein file 

	def write_mol2_protein(self):
		logging.info("Writing the protein mol2 file")
		protein_input = data.proteinFile[:-5]

		with open("temp/" + str(protein_input) +"_charge.mol2", "w") as mol2, open("temp/cys_residue_temp.mol2", 'w') as cys_res:
			cys_res_list = []

			for i in range(5):
				short_name = (str(data.ProteinSection.sections_protein["section_%s" %i]["name"]).strip('[' + ']' + '\'' + '\\' + 'n'))

				if short_name == "@<TRIPOS>MOLECULE":
					num_of_new_atoms = data.range_of_atoms_prot - data.starting_range_of_atoms_prot
					num_of_new_bonds = data.range_of_bonds_prot - data.starting_range_of_bonds_prot

					col = data.ProteinSection.sections_protein["section_%s" %1]["lines"][1].split()

					if len(col):

						col[0] = int(col[0])
						col[0] += num_of_new_atoms
						atom = col[0]

						col[1] = int(col[1])
						col[1] += num_of_new_bonds
						bond = col[1]

					data.ProteinSection.sections_protein["section_%s" %1]["lines"][1] = (str(atom) + ' ' + str(bond) + ' ' + str(col[2]) + ' ' + str(col[3]) + ' ' + str(col[4] + '\n'))

					mol2.write(short_name + '\n')
					cys_res.write(short_name + '\n')

					for line in data.ProteinSection.sections_protein["section_%s" %1]["lines"]:

						mol2.write(str(line))
						cys_res.write(str(line))

				if short_name == "@<TRIPOS>ATOM":
					mol2.write(short_name + '\n')
					cys_res.write(short_name + '\n')
					for atom in range(data.range_of_atoms_prot):
						atom += 1

						for c in data.ProteinLists.atom_list_prot["atom_%s" % atom]["x_coord"]:
							x_coord_n = c
						for c in data.ProteinLists.atom_list_prot["atom_%s" % atom]["y_coord"]:
							y_coord_n = c
						for c in data.ProteinLists.atom_list_prot["atom_%s" % atom]["z_coord"]:
							z_coord_n = c
						for c in data.ProteinLists.atom_list_prot["atom_%s" % atom]["charge"]:
							charge_n = c

						atom_name = str(data.ProteinLists.atom_list_prot["atom_%s" % atom]["atom_name"]).strip('[' + ']' + '\'')
						atom_type = str(data.ProteinLists.atom_list_prot["atom_%s" % atom]["atom_type"]).strip('[' + ']' + '\'')
						res_num = str(data.ProteinLists.atom_list_prot["atom_%s" % atom]["res_num"]).strip('[' + ']' + '\'')
						res_name = str(data.ProteinLists.atom_list_prot["atom_%s" % atom]["res_name"]).strip('[' + ']' + '\'')


						if len(str(atom)) == 1:
							space_1a = '      '
							space_3a = '  '
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

						mol2.write(space_1a + str(atom) + ' ' + atom_name + space_3a + neg_space + str("%.4f" % float(x_coord_n)) + space_4a + str("%.4f" % float(y_coord_n)) + space_5a + str("%.4f" % float(z_coord_n)) + ' ' + atom_type + space_6a + res_num + '    ' + res_name + space_7a + str("%.6f" % float(charge_n)) + '\n')

						if res_num == '51':
							cys_res_list.append(atom)
							corr = min(cys_res_list) - 1
							atom_cys = int(atom) - int(corr)
							cys_res.write(space_1a + str(atom_cys) + ' ' + atom_name + space_3a + neg_space + str("%.4f" % float(x_coord_n)) + space_4a + str("%.4f" % float(y_coord_n)) + space_5a + str("%.4f" % float(z_coord_n)) + ' ' + atom_type + space_6a + res_num + '    ' + res_name + space_7a + str("%.6f" % float(charge_n)) + '\n')
							logging.info(cys_res_list)


				if short_name == "@<TRIPOS>BOND":
					bond = 0
					mol2.write(short_name + '\n')
					cys_res.write(short_name + '\n')

					for c in range(data.range_of_bonds_prot):
						c += 1

						a1 = data.ProteinLists.bond_list_prot["bond_%s" % c]["a1"]
						a2 = data.ProteinLists.bond_list_prot["bond_%s" % c]["a2"]
						b_typ = data.ProteinLists.bond_list_prot["bond_%s" % c]["type"]

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

						for a in cys_res_list:
							corr = min(cys_res_list) - 1
							if str(a1) == str(a) or str(a2) == str(a):
								
								a1 = int(a1) - corr
								a2 = int(a2) - corr

								if int(a1) >= 0 and int(a2) >= 0:
									bond += 1	

									cys_res.write(space_1b + str(bond) + space_2b + str(a1) + space_3b + str(a2) + ' ' + str(b_typ) + '\n')
						

				if short_name == "@<TRIPOS>SUBSTRUCTURE":
					mol2.write(short_name + '\n')
					for sub in range(data.substructure_range):
						sub += 1

						sid = data.ProteinLists.substructure["sub_%s" % sub]["id"]
						resname = data.ProteinLists.substructure["sub_%s" % sub]["resname"]
						atmnum = data.ProteinLists.substructure["sub_%s" % sub]["atmnum"]
						stype = data.ProteinLists.substructure["sub_%s" % sub]["type"]
						num1 = data.ProteinLists.substructure["sub_%s" % sub]["num_1"]
						chain = data.ProteinLists.substructure["sub_%s" % sub]["chain"]
						resn2 = data.ProteinLists.substructure["sub_%s" % sub]["resname_2"]
						num2 = data.ProteinLists.substructure["sub_%s" % sub]["num_2"]
						if data.ProteinLists.substructure["sub_%s" % sub]["comment"] == []:
							comment = ' '
						else:
							comment = data.ProteinLists.substructure["sub_%s" % sub]["comment"]


						mol2.write(str(sid) + '     ' + str(resname) + '     ' + str(atmnum) + '     ' + str(stype) + '     ' + str(num1) + '     ' + str(chain) + '     ' + str(resn2) + '     ' + str(num2) + '     ' + str(comment) + '\n' )				
		

		with open("temp/cys_residue_temp.mol2") as cys_res, open("temp/cys_residue.mol2", 'w') as cys_res_new:
			for line in cys_res:
				# print(line)
				col = line.split()
				if len(col) == 5:
					logging.info(line)
					col[0] = len(cys_res_list)
					col[1] = bond
					cys_res_new.write(str(col[0]) + '  ' + str(col[1]) + '  ' + str(col[2]) + '  ' + str(col[3]) + '  ' + str(col[4]) + '\n')

				else :
					cys_res_new.write(line)

# ProteinPreparation()
	# init()