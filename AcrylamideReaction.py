import time
import logging
import math


import ProgramData as data
from AcrylamideMapping import AcrylamideMapping
import AcrylamideFunctions as function

class AcrylamideReaction():
	# Xi = input atom ; Xt = template atom
	logging.info("Well hello there :)")
	print("Well hello there :)")

	def __init__(self):
		super(AcrylamideReaction, self).__init__()

		AcrylamideMapping()
		data.NewBonds()
		# data.NewAtom()
		self.Hybridisation()
		self.WriteOutput()

	
	# adding bonds and changing hybridisation
	# def NewBonds(self):
	# 	logging.info("Hybridising...")

	# 	global range_of_atoms
	# 	global range_of_bonds

	# 	H3_num = 0
	# 	H4_num = []
	# 	H7_num = []
	# 	H4_num = range_of_atoms + 1
	# 	H5_num = 0
	# 	H6_num = 0
	# 	H7_num = range_of_atoms + 2

	# 	atom_list["atom_%s" % H4_num] = {}
	# 	atom_list["atom_%s" % H4_num]["atom_id"] = []
	# 	atom_list["atom_%s" % H4_num]["atom_name"] = []
	# 	atom_list["atom_%s" % H4_num]["x_coord"] = []
	# 	atom_list["atom_%s" % H4_num]["y_coord"] = []
	# 	atom_list["atom_%s" % H4_num]["z_coord"] = []
	# 	atom_list["atom_%s" % H4_num]["atom_type"] = []
	# 	atom_list["atom_%s" % H4_num]["atom_id"].append(str(H4_num))
	# 	atom_list["atom_%s" % H4_num]["atom_name"].append('Hx')
	# 	atom_list["atom_%s" % H4_num]["atom_type"].append('H')
	# 	atom_list["atom_%s" % H4_num]["lig_name"] = atom_list["atom_%s" % self.C2i]["lig_name"]
	# 	atom_list["atom_%s" % H4_num]["charge"] = []
	# 	atom_list["atom_%s" % H4_num]["charge"] = 0.0000

	# 	atom_list["atom_%s" % H7_num] = {}
	# 	atom_list["atom_%s" % H7_num]["atom_id"] = []
	# 	atom_list["atom_%s" % H7_num]["atom_name"] = []
	# 	atom_list["atom_%s" % H7_num]["x_coord"] = []
	# 	atom_list["atom_%s" % H7_num]["y_coord"] = []
	# 	atom_list["atom_%s" % H7_num]["z_coord"] = []
	# 	atom_list["atom_%s" % H7_num]["atom_type"] = []
	# 	atom_list["atom_%s" % H7_num]["atom_id"].append(str(H7_num))
	# 	atom_list["atom_%s" % H7_num]["atom_name"].append('Hr')
	# 	atom_list["atom_%s" % H7_num]["atom_type"].append('H')
	# 	atom_list["atom_%s" % H7_num]["lig_name"] = atom_list["atom_%s" % self.C2i]["lig_name"]
	# 	atom_list["atom_%s" % H7_num]["charge"] = []
	# 	atom_list["atom_%s" % H7_num]["charge"] = 0.0000


	# def NewAtom(atom_number, x, y, z, a1):
	# 	global range_of_atoms
	# 	global range_of_bonds

	# 	for atom in range(range_of_atoms+1):
	# 		atom += 1

	# 		b = atom_number

	# 		stripped_atom_number = (str(atom_list["atom_%s" % atom]["atom_id"]).strip('[' + '\'' + '\'' + ']'))
		
	# 		if len(stripped_atom_number) > 0:
	# 			if b == int(stripped_atom_number):

	# 				atom_list["atom_%s" % atom]["x_coord"] = x
	# 				atom_list["atom_%s" % atom]["y_coord"] = y
	# 				atom_list["atom_%s" % atom]["z_coord"] = z
					
	# 				range_of_atoms += 1
	# 				range_of_bonds += 1

	# 				bond_list["bond_%s" % range_of_bonds] = {}
	# 				bond_list["bond_%s" % range_of_bonds]["bond_id"] = []
	# 				bond_list["bond_%s" % range_of_bonds]["a1"] = []
	# 				bond_list["bond_%s" % range_of_bonds]["a2"] = []
	# 				bond_list["bond_%s" % range_of_bonds]["bond_id"].append(str(range_of_bonds))
	# 				bond_list["bond_%s" % range_of_bonds]["a1"] = a1
	# 				bond_list["bond_%s" % range_of_bonds]["a2"] = atom_number
	# 				bond_list["bond_%s" % range_of_bonds]["bond_type"] = 1

	# 				sections["section_%s" %3]["lines"].append('    ' + str(range_of_bonds) + '   ' + str(bond_list["bond_%s" % range_of_bonds]["a1"]) + '   ' + str(bond_list["bond_%s" % range_of_bonds]["a2"]) + ' ' + str(bond_list["bond_%s" % range_of_bonds]["bond_type"]) + '\n')

	def Hybridisation(self):

		print(data.H7_num, data.H4_num, data.range_of_atoms)
		
		C2_hydrogens = []
		for atom in range(data.range_of_bonds):
			atom += 1
			
			c = data.C2i

			if c == data.SectionTemplate.bond_list["bond_%s" % atom]["a1"] or c == data.SectionTemplate.bond_list["bond_%s" % atom]["a2"]:
				if data.SectionTemplate.bond_list["bond_%s" % atom]["a1"] != data.C2i:
					if data.SectionTemplate.bond_list["bond_%s" % atom]["a1"] != data.C1i:
						if data.SectionTemplate.bond_list["bond_%s" % atom]["a1"] != data.C3i:
							atom_n = data.SectionTemplate.bond_list["bond_%s" % atom]["a1"]
							if data.SectionTemplate.atom_list["atom_%s" % atom_n]["atom_type"] == ['H']:
								C2_hydrogens.append(data.SectionTemplate.bond_list["bond_%s" % atom]["a1"])

				elif data.SectionTemplate.bond_list["bond_%s" % atom]["a2"] != data.C2i:
					if data.SectionTemplate.bond_list["bond_%s" % atom]["a2"] != data.C1i:
						if data.SectionTemplate.bond_list["bond_%s" % atom]["a2"] != data.C3i:
							atom_n = data.SectionTemplate.bond_list["bond_%s" % atom]["a2"]
							if data.SectionTemplate.atom_list["atom_%s" % atom_n]["atom_type"] == ['H']:
								C2_hydrogens.append(data.SectionTemplate.bond_list["bond_%s" % atom]["a2"])

		tanslate_x = data.SectionTemplate.atom_list["atom_%s" % data.C2i]["x_coord"]
		tanslate_y = data.SectionTemplate.atom_list["atom_%s" % data.C2i]["y_coord"]
		tanslate_z = data.SectionTemplate.atom_list["atom_%s" % data.C2i]["z_coord"]

		function.Origin(tanslate_x, tanslate_y, tanslate_z)


		if len(C2_hydrogens) == 1:
			data.H3_num = C2_hydrogens[0]

			H3_x = data.SectionTemplate.atom_list["atom_%s" % data.H3_num]["x_coord"]
			H3_y = data.SectionTemplate.atom_list["atom_%s" % data.H3_num]["y_coord"]
			H3_z = data.SectionTemplate.atom_list["atom_%s" % data.H3_num]["z_coord"]

			atom = data.H3_num
			if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:
				x = data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]
				y = data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]
				z = data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]
				

				A = [  [(math.cos(45)), 0, -(math.sin(45))], [0, 1, 0], [(math.sin(45)), 0, (math.cos(45))]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)

			H4_x = -(data.SectionTemplate.atom_list["atom_%s" % data.H3_num]["x_coord"] )
			H4_y = data.SectionTemplate.atom_list["atom_%s" % data.H3_num]["y_coord"] 
			H4_z = data.SectionTemplate.atom_list["atom_%s" % data.H3_num]["z_coord"]

			data.NewAtom(data.H4_num, H4_x, H4_y, H4_z, data.C2i)
			print(data.H4_num, "h4")
			# data.range_of_atoms = data.H4_num

		if len(C2_hydrogens) == 0:
			logging.info("no free hydrogens")

			data.NewAtom(data.H4_num, H4_x, H4_y, H4_z, data.C2i)
			print(data.H4_num, "h4")
			# data.range_of_atoms = data.H4_num


		C3_hydrogens = []
		for atom in range(data.range_of_bonds):
			atom += 1
			
			c = data.C3i

			if c == data.SectionTemplate.bond_list["bond_%s" % atom]["a1"] or c == data.SectionTemplate.bond_list["bond_%s" % atom]["a2"]:
				if data.SectionTemplate.bond_list["bond_%s" % atom]["a1"] != data.C3i:
					if data.SectionTemplate.bond_list["bond_%s" % atom]["a1"] != data.C2i:
						atom_n =  data.SectionTemplate.bond_list["bond_%s" % atom]["a1"]
						if data.SectionTemplate.atom_list["atom_%s" % atom_n]["atom_type"] == ['H']:
							C3_hydrogens.append(data.SectionTemplate.bond_list["bond_%s" % atom]["a1"])

				elif data.SectionTemplate.bond_list["bond_%s" % atom]["a2"] != data.C3i:
					if data.SectionTemplate.bond_list["bond_%s" % atom]["a2"] != data.C2i:

						atom_n = data.SectionTemplate.bond_list["bond_%s" % atom]["a2"]
						if data.SectionTemplate.atom_list["atom_%s" % atom_n]["atom_type"] == ['H']:
							C3_hydrogens.append(data.SectionTemplate.bond_list["bond_%s" % atom]["a2"])

		
		tanslate_x = data.SectionTemplate.atom_list["atom_%s" % data.C3i]["x_coord"]
		tanslate_y = data.SectionTemplate.atom_list["atom_%s" % data.C3i]["y_coord"]
		tanslate_z = data.SectionTemplate.atom_list["atom_%s" % data.C3i]["z_coord"]


		function.Origin(tanslate_x, tanslate_y, tanslate_z)


		if len(C3_hydrogens) == 2:
			data.H5_num = C3_hydrogens[0]
			data.H6_num = C3_hydrogens[1]

			H5_x = data.SectionTemplate.atom_list["atom_%s" % data.H5_num]["x_coord"]
			H5_y = data.SectionTemplate.atom_list["atom_%s" % data.H5_num]["y_coord"]
			H5_z = data.SectionTemplate.atom_list["atom_%s" % data.H5_num]["z_coord"]

			atom = data.H5_num
			if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:
				x = data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]
				y = data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]
				z = (data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"])
				
				A = [  [1, 0, 0], [0, (math.cos(90)), -(math.sin(90))], [0, -(math.sin(90)), (math.cos(90))]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)

				A = [  [(math.cos(90)), (math.sin(90)), 0], [-(math.sin(90)), (math.cos(90)), 0], [0, 0, 1]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)


				A = [  [(math.cos(45)), 0, -(math.sin(45))], [0, 1, 0], [(math.sin(45)), 0, (math.cos(45))]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)


				H6_x = -(data.SectionTemplate.atom_list["atom_%s" % data.H5_num]["x_coord"])
				H6_y = (data.SectionTemplate.atom_list["atom_%s" % data.H5_num]["y_coord"])
				H6_z = (data.SectionTemplate.atom_list["atom_%s" % data.H5_num]["z_coord"])

				data.SectionTemplate.atom_list["atom_%s" % data.H6_num]["x_coord"] = H6_x
				data.SectionTemplate.atom_list["atom_%s" % data.H6_num]["y_coord"] = H6_y
				data.SectionTemplate.atom_list["atom_%s" % data.H6_num]["z_coord"] = H6_z		


				H7_x = data.SectionTemplate.atom_list["atom_%s" % data.C3i]["x_coord"]
				H7_y = data.SectionTemplate.atom_list["atom_%s" % data.C3i]["y_coord"] + data.H7_y_trans
				H7_z = data.SectionTemplate.atom_list["atom_%s" % data.C3i]["z_coord"]

				data.SectionTemplate.atom_list["atom_%s" % data.H7_num]["x_coord"] = H7_x
				data.SectionTemplate.atom_list["atom_%s" % data.H7_num]["y_coord"] = H7_y
				data.SectionTemplate.atom_list["atom_%s" % data.H7_num]["z_coord"] = H7_z


			# add new atom
				data.NewAtom(data.H7_num, H7_x, H7_y, H7_z, data.C3i)
				print(data.H7_num, "h7")
				# data.range_of_atoms = data.H7_num

		if len(C3_hydrogens) == 1:
			data.H5_num = C3_hydrogens[0]


			H5_x = data.SectionTemplate.atom_list["atom_%s" % data.H5_num]["x_coord"]
			H5_y = data.SectionTemplate.atom_list["atom_%s" % data.H5_num]["y_coord"]
			H5_z = data.SectionTemplate.atom_list["atom_%s" % data.H5_num]["z_coord"]


			atom = data.H5_num
			if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:
				x = data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]
				y = data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]
				z = (data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"])

				
				A = [  [1, 0, 0], [0, (math.cos(90)), -(math.sin(90))], [0, -(math.sin(90)), (math.cos(90))]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)

				A = [  [(math.cos(90)), (math.sin(90)), 0], [-(math.sin(90)), (math.cos(90)), 0], [0, 0, 1]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)


				A = [  [(math.cos(45)), 0, -(math.sin(45))], [0, 1, 0], [(math.sin(45)), 0, (math.cos(45))]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)

				H7_x = data.SectionTemplate.atom_list["atom_%s" % data.C3i]["x_coord"]
				H7_y = data.SectionTemplate.atom_list["atom_%s" % data.C3i]["y_coord"] + data.H7_y_trans
				H7_z = data.SectionTemplate.atom_list["atom_%s" % data.C3i]["z_coord"]

				data.SectionTemplate.atom_list["atom_%s" % data.H7_num]["x_coord"] = H7_x
				data.SectionTemplate.atom_list["atom_%s" % data.H7_num]["y_coord"] = H7_y
				data.SectionTemplate.atom_list["atom_%s" % data.H7_num]["z_coord"] = H7_z


				data.NewAtom(data.H7_num, H7_x, H7_y, H7_z, data.C3i)
				print(data.H7_num, "h7")
				# data.range_of_atoms = data.H7_num

		if len(C3_hydrogens) == 0:
			logging.info("no free hydrogens")

			data.NewAtom(data.H7_num, H7_x, H7_y, H7_z, data.C3i)
			print(data.H7_num, "h7")
			# data.range_of_atoms = data.H7_num

		data.SectionTemplate.atom_list["atom_%s" % data.C1i]["atom_type"] = ['C.3']
		data.SectionTemplate.atom_list["atom_%s" % data.C2i]["atom_type"] = ['C.3']
		data.SectionTemplate.atom_list["atom_%s" % data.C3i]["atom_type"] = ['C.3']


	def WriteOutput(self):
		logging.info("Writing first mol2 output")

		with open("temp/new_coords_temp.mol2", "w") as mol2:
			for i in range(5):
				short_name = (str(data.Section.sections["section_%s" %i]["name"]).strip('[' + ']' + '\'' + '\\' + 'n'))

				if short_name == "@<TRIPOS>MOLECULE":
					print(data.range_of_atoms, data.starting_range_of_atoms)
					num_of_new_atoms = data.range_of_atoms - data.starting_range_of_atoms
					num_of_new_bonds = data.range_of_bonds - data.starting_range_of_bonds

					col = data.Section.sections["section_%s" %1]["lines"][1].split()

					if len(col):

						col[0] = int(col[0])
						col[0] += num_of_new_atoms
						atom = col[0]

						col[1] = int(col[1])
						col[1] += num_of_new_bonds
						bond = col[1]

					data.Section.sections["section_%s" %1]["lines"][1] = (str(atom) + ' ' + str(bond) + ' ' + str(col[2]) + ' ' + str(col[3]) + ' ' + str(col[4] + '\n'))

					mol2.write(short_name + '\n')
					for line in data.Section.sections["section_%s" %1]["lines"]:

						mol2.write(str(line))

				if short_name == "@<TRIPOS>ATOM":
					mol2.write(short_name + '\n')
					print(data.range_of_atoms)
					for atom in range(data.range_of_atoms):
						atom += 1
						if atom <= data.range_of_atoms:
							print(atom, "tom")
							atom_name = str(data.SectionTemplate.atom_list["atom_%s" % atom]["atom_name"]).strip('[' + ']' + '\'')
							atom_type = str(data.SectionTemplate.atom_list["atom_%s" % atom]["atom_type"]).strip('[' + ']' + '\'')
							ligand_name = str(data.SectionTemplate.atom_list["atom_%s" % atom]["lig_name"]).strip('[' + ']' + '\'')
							charge = str(data.SectionTemplate.atom_list["atom_%s" % atom]["charge"]).strip('[' + ']' + '\'')
							mol2.write('      ' + str(atom) + ' ' + atom_name + '         ' + str("%.4f" % data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]) + '   ' + str("%.4f" % data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]) + '   ' + str("%.4f" % data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]) + ' ' + atom_type + '    ' + "1 " + ligand_name + '   ' + charge + '\n')

				if short_name == "@<TRIPOS>BOND":
					mol2.write(short_name + '\n')

					for c in range(data.range_of_bonds):
						c += 1

						a1 = data.SectionTemplate.bond_list["bond_%s" % c]["a1"]
						a2 = data.SectionTemplate.bond_list["bond_%s" % c]["a2"]
						b_typ = data.SectionTemplate.bond_list["bond_%s" % c]["bond_type"]

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
					for line in data.Section.sections["section_%s" %4]["lines"]:
						mol2.write(str(line))
