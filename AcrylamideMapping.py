import time
import logging
import math

import ProgramData as data
import AcrylamideFunctions as function


# processing
class AcrylamideMapping():
	logging.info("Mapping...")
	print("Mapping...")
	#extract atom and bond data
	def __init__(self):
		super(AcrylamideMapping, self).__init__()


	# mapping and translating procedure - maybe put into a function. #
		self.Sectioning()
		# print(data.SectionTemplate.atom_list["atom_%s" % 15].values())
		self.AtomMap()
		self.AcrylamideTransformation()
		tanslate_x = data.C1t_x
		tanslate_y = data.C1t_y
		tanslate_z = data.C1t_z
		function.Origin(tanslate_x, tanslate_y, tanslate_z)

		logging.info("Rotating...")
		self.AcrylamideRotationOXY()
		self.AcrylamideRotationOYZ()
		function.AngleCalc()
		self.AcrylamideRotationCXY()
		function.AngleCalc()
		self.AcrylamideRotationCYZ()
		function.AngleCalc2()
		self.AcrylamideRotationCXY()

	def Sectioning(self):
		print(data.range_of_bonds)
		data.i = data.range_of_bonds
		for n in range(5):

			short_name = (str(data.Section.sections["section_%s" % n]["name"]).strip('[' + '\'' + '@' + '<' + '\\' + 'n' + '\'' + ']'))

			if short_name == "TRIPOS>ATOM":

				for line in data.Section.sections["section_%s" %n]["lines"]:

					col = line.split()
					# print(line)


					if len(col) == 9:
						# print("charge column present")
						atom = col[0]
						# print(atom)
						# print(data.SectionTemplate.atom_list["atom_%s" % atom].values())
						data.SectionTemplate.atom_list["atom_%s" % atom]["atom_id"].append(col[0])
						data.SectionTemplate.atom_list["atom_%s" % atom]["atom_name"].append(col[1])
						data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"].append(col[2])
						data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"].append(col[3])
						data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"].append(col[4])
						data.SectionTemplate.atom_list["atom_%s" % atom]["atom_type"].append(col[5])
						data.SectionTemplate.atom_list["atom_%s" % atom]["lig_name"].append(col[7])
						data.SectionTemplate.atom_list["atom_%s" % atom]["charge"].append(col[8])

					elif len(col) == 8:
						# print("no charge column")
						atom = col[0]
						data.SectionTemplate.atom_list["atom_%s" % atom]["atom_id"].append(col[0])
						data.SectionTemplate.atom_list["atom_%s" % atom]["atom_name"].append(col[1])
						data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"].append(col[2])
						data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"].append(col[3])
						data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"].append(col[4])
						data.SectionTemplate.atom_list["atom_%s" % atom]["atom_type"].append(col[5])
						data.SectionTemplate.atom_list["atom_%s" % atom]["lig_name"].append(col[7])
						
			if short_name == "TRIPOS>BOND":
				for line in data.Section.sections["section_%s" %n]["lines"]:

					col = line.split()

					if len(col):
						bond = col[0]
						data.SectionTemplate.bond_list["bond_%s" % bond]["bond_id"] = col[0]
						data.SectionTemplate.bond_list["bond_%s" % bond]["a1"] = col[1]
						data.SectionTemplate.bond_list["bond_%s" % bond]["a2"] = col[2]
						data.SectionTemplate.bond_list["bond_%s" % bond]["bond_type"] = col[3]


	# find the acrylamide group in the input mol2 file
	def AtomMap(self):
		# a way of replicas will need to be put in
		bond_atoms_temp = []
		bond_atoms = []
		carbon_number = []

		# data.C1i
		# data.C2i
		# data.oi_atom
		# data.C3i

		# assign atoms
		# make a list of sp2 carbons
		for n in range(data.range_of_atoms):
			n = n + 1

			if "C" in str(data.SectionTemplate.atom_list["atom_%s" % n]["atom_name"]) and "C.2" in str(data.SectionTemplate.atom_list["atom_%s" % n]["atom_type"]):

				data.atom = (str(data.SectionTemplate.atom_list["atom_%s" % n]["atom_id"]).strip('[' + '\'' + '\'' + ']'))
				carbon_number.append(data.atom)

		
		# append sp2 carbon atom numbers to a list
		for b in range(data.range_of_atoms):
			b = b + 1
			for c in carbon_number:

				if c == data.SectionTemplate.bond_list["bond_%s" % b]["a1"] or c == data.SectionTemplate.bond_list["bond_%s" % b]["a2"]:

					bond_atoms_temp.append(data.SectionTemplate.bond_list["bond_%s" % b]["a1"])
					bond_atoms_temp.append(data.SectionTemplate.bond_list["bond_%s" % b]["a2"])

					[bond_atoms.append(x) for x in bond_atoms_temp if x not in bond_atoms]

				
		# find a double bonded oxygen to carbon from the previous list
		for a in range(data.range_of_atoms):
			a = a + 1
			for atoms in bond_atoms:
			
				atom_bond_check_num = (str(data.SectionTemplate.atom_list["atom_%s" % a]["atom_id"]).strip('[' + '\'' + '\'' + ']'))
				atom_bond_check_typ = (str(data.SectionTemplate.atom_list["atom_%s" % a]["atom_type"]).strip('[' + '\'' + '\'' + ']'))

				if atom_bond_check_num == atoms:

					if str(atom_bond_check_typ) == "O.2":

						data.oi_atom = atom_bond_check_num
						logging.debug(data.oi_atom)


		# assign the carbon to which the oxygen is bound to
		for d in range(data.range_of_atoms):
			d = d + 1
			for c in carbon_number:
				if c == data.SectionTemplate.bond_list["bond_%s" % d]["a1"] or c == data.SectionTemplate.bond_list["bond_%s" % d]["a2"]:
					if data.oi_atom == data.SectionTemplate.bond_list["bond_%s" % d]["a1"] or data.oi_atom == data.SectionTemplate.bond_list["bond_%s" % d]["a2"]:
						
						if data.SectionTemplate.bond_list["bond_%s" % d]["a1"] != data.oi_atom :
							data.C1i = data.SectionTemplate.bond_list["bond_%s" % d]["a1"]

						elif data.SectionTemplate.bond_list["bond_%s" % d]["a2"] != data.oi_atom:
							data.C1i = data.SectionTemplate.bond_list["bond_%s" % d]["a2"]
		logging.debug(data.C1i)					


		# assign sp2 carbon bound to C1
		for e in range(data.range_of_atoms):
			e = e + 1
			for c in carbon_number:
				if c == data.SectionTemplate.bond_list["bond_%s" % e]["a1"] or c == data.SectionTemplate.bond_list["bond_%s" % e]["a2"]:
					if data.C1i == data.SectionTemplate.bond_list["bond_%s" % e]["a1"] or data.C1i == data.SectionTemplate.bond_list["bond_%s" % e]["a2"]:
						
						if data.SectionTemplate.bond_list["bond_%s" % e]["a1"] in carbon_number and data.SectionTemplate.bond_list["bond_%s" % e]["a2"] in carbon_number:

							if data.SectionTemplate.bond_list["bond_%s" % e]["a1"] != data.C1i:
								data.C2i = data.SectionTemplate.bond_list["bond_%s" % e]["a1"]

							elif data.SectionTemplate.bond_list["bond_%s" % e]["a2"] != data.C1i:
								data.C2i = data.SectionTemplate.bond_list["bond_%s" % e]["a2"]
		logging.debug(data.C2i)	

		# assign sp2 carbon bound to C2
		for f in range(data.range_of_atoms):
			f = f + 1
			for c in carbon_number:
				if c == data.SectionTemplate.bond_list["bond_%s" % f]["a1"] or c == data.SectionTemplate.bond_list["bond_%s" % f]["a2"]:
					if data.C2i == data.SectionTemplate.bond_list["bond_%s" % f]["a1"] or data.C2i == data.SectionTemplate.bond_list["bond_%s" % f]["a2"]:
						
						if data.SectionTemplate.bond_list["bond_%s" % f]["a1"] in carbon_number and data.SectionTemplate.bond_list["bond_%s" % f]["a2"] in carbon_number:

							if data.SectionTemplate.bond_list["bond_%s" % f]["a1"] == data.C2i and data.SectionTemplate.bond_list["bond_%s" % f]["a2"] != data.C1i:
								data.C3i = data.SectionTemplate.bond_list["bond_%s" % f]["a2"]

							elif data.SectionTemplate.bond_list["bond_%s" % f]["a2"] == data.C2i and data.SectionTemplate.bond_list["bond_%s" % f]["a1"] != data.C1i:
								data.C3i = data.SectionTemplate.bond_list["bond_%s" % f]["a1"]
		logging.debug(data.C3i)	


	# translate and rotate into place.
	def AcrylamideTransformation(self):
		
		# data.C1i

		x_trans_factor = 0
		y_trans_factor = 0
		z_trans_factor = 0

		C1i_x = 0
		C1i_y = 0
		C1i_z = 0

		### align C1i to C1t (translation matrix) ###
		if int(data.C1i) > 0:
			C1i_x = [float(i) for i in data.SectionTemplate.atom_list["atom_%s" % data.C1i]["x_coord"]]
			C1i_y = [float(i) for i in data.SectionTemplate.atom_list["atom_%s" % data.C1i]["y_coord"]]
			C1i_z = [float(i) for i in data.SectionTemplate.atom_list["atom_%s" % data.C1i]["z_coord"]]

			for x in C1i_x:
				C1i_x = x
			for y in C1i_y:
				C1i_y = y
			for z in C1i_z:
				C1i_z = z

		x_trans_factor = data.C1t_x - C1i_x
		y_trans_factor = data.C1t_y - C1i_y
		z_trans_factor = data.C1t_z - C1i_z

		# assign new, translated coordinates
		for atom in range(data.range_of_atoms):
			atom += 1
			for x in data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]:
				data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] = float(x) + x_trans_factor
				logging.debug(data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"])	

			for y in data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]:
				data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"] = float(y) + y_trans_factor
				logging.debug(data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"])
	
			for z in data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]:
				data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"] = float(z) + z_trans_factor	
				logging.debug(data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"])		

	
	# rotations
	def AcrylamideRotationOXY(self):

		for atom in range(data.range_of_atoms):
			atom += 1
			if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:
				x = data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]
				y = data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]
				z = data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]
			
				A = [  [math.cos(data.angle_xy), math.sin(data.angle_xy), 0], [-(math.sin(data.angle_xy)), math.cos(data.angle_xy), 0], [0, 0, 1]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)

	def AcrylamideRotationOYZ(self):

		for atom in range(data.range_of_atoms):
			atom += 1
			if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:
				x = data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]
				y = data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]
				z = data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]
			
				A = [  [1, 0, 0], [0, math.cos(data.angle_yz), math.sin(data.angle_yz)], [0, -(math.sin(data.angle_yz)), math.cos(data.angle_yz)]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)

	def AcrylamideRotationCXY(self):

		for atom in range(data.range_of_atoms):
			atom += 1
			if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:
				x = data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]
				y = data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]
				z = data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]
				
				A = [  [math.cos(data.angle_xy_C), math.sin(data.angle_xy_C), 0], [-(math.sin(data.angle_xy_C)), math.cos(data.angle_xy_C), 0], [0, 0, 1]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)


	def AcrylamideRotationCYZ(self):

		for atom in range(data.range_of_atoms):
			atom += 1
			if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:
				x = data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]
				y = data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]
				z = data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]
				
				A = [  [1, 0, 0], [0, math.cos(data.angle_yz_C), math.sin(data.angle_yz_C)], [0, -(math.sin(data.angle_yz_C)), math.cos(data.angle_yz_C)]    ]
				B = [  [x], [y], [z]   ]

				function.MatrixMultiplication(A, B, atom)


	def ReNormalise(self):

		for atom in range(data.range_of_atoms):
			atom += 1
			if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:
				data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] = float(data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]) + data.C1t_x			
				data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"] = float(data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]) + data.C1t_y			
				data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"] = float(data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]) + data.C1t_z



	# if round(data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["z_coord"], 1)  < 0.0:
	# 	for atom in range(data.range_of_atoms):
	# 		atom += 1
	# 		if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:
	# 			x = data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]
	# 			y = data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]
	# 			z = data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]
				
	# 			A = [  [-1, 0, 0], [0, 1, 0], [0, 0, -1]    ]
	# 			B = [  [x], [y], [z]   ]

	# 			data.MatrixMultiplication(A, B, atom)

	# if round(data.SectionTemplate.atom_list["atom_%s" % data.C3i]["y_coord"], 1) < 0.0:
	# 	for atom in range(data.range_of_atoms):
	# 		atom += 1
	# 		if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:
	# 			x = data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]
	# 			y = data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]
	# 			z = data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]
				
	# 			A = [  [-1, 0, 0], [0, -1, 0], [0, 0, 1]    ]
	# 			B = [  [x], [y], [z]   ]

	# 			data.MatrixMultiplication(A, B, atom)
	###
