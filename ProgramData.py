import time
import logging


mol2Input = ''
mol2File = ''

mol_id = 0
section_num = 0
range_of_atoms = 0
range_of_bonds = 0
starting_range_of_atoms = 0
starting_range_of_bonds = 0

def Section():
	Section.sections = {}
	for n in range(5):
		Section.sections["section_%s" %n] = {}
		Section.sections["section_%s" %n]["name"] = []
		Section.sections["section_%s" %n]["lines"] = []


i = 0
atom_list = {}
bond_list = {}
# atom and bond list definitions
if range_of_atoms > 0:
	print(range_of_atoms, "range ")
	for i in range(range_of_atoms):
		# print(range_of_atoms, "data range")
		# print(i)
		i = i + 1
		atom_list["atom_%s" % i] = {}
		bond_list["bond_%s" % i] = {}

		atom_list["atom_%s" % i]["atom_id"] = []
		atom_list["atom_%s" % i]["atom_name"] = []
		atom_list["atom_%s" % i]["x_coord"] = []
		atom_list["atom_%s" % i]["y_coord"] = []
		atom_list["atom_%s" % i]["z_coord"] = []
		atom_list["atom_%s" % i]["atom_type"] = []
		atom_list["atom_%s" % i]["lig_name"] = []
		atom_list["atom_%s" % i]["charge"] = []

		bond_list["bond_%s" % i]["bond_id"] = []
		bond_list["bond_%s" % i]["a1"] = [] # origin arom
		bond_list["bond_%s" % i]["a2"] = [] # target atom
		bond_list["bond_%s" % i]["bond_type"] = []

def SectionTemplate():
	# Ligand preparation templates and data
	i = 0
	SectionTemplate.atom_list = {}
	SectionTemplate.bond_list = {}
	# atom and bond list definitions

	for i in range(range_of_atoms):
		print(range_of_atoms, "data range")
		# print(i)
		i += 1
		SectionTemplate.atom_list["atom_%s" % i] = {}
		SectionTemplate.bond_list["bond_%s" % i] = {}

		SectionTemplate.atom_list["atom_%s" % i]["atom_id"] = []
		SectionTemplate.atom_list["atom_%s" % i]["atom_name"] = []
		SectionTemplate.atom_list["atom_%s" % i]["x_coord"] = []
		SectionTemplate.atom_list["atom_%s" % i]["y_coord"] = []
		SectionTemplate.atom_list["atom_%s" % i]["z_coord"] = []
		SectionTemplate.atom_list["atom_%s" % i]["atom_type"] = []
		SectionTemplate.atom_list["atom_%s" % i]["lig_name"] = []
		SectionTemplate.atom_list["atom_%s" % i]["charge"] = []

		SectionTemplate.bond_list["bond_%s" % i]["bond_id"] = []
		SectionTemplate.bond_list["bond_%s" % i]["a1"] = [] # origin arom
		SectionTemplate.bond_list["bond_%s" % i]["a2"] = [] # target atom
		SectionTemplate.bond_list["bond_%s" % i]["bond_type"] = []

		# print(atom_list.values())

H3_num = 0
H4_num = []
H7_num = []
# H4_num = range_of_atoms + 1
H5_num = 0
H6_num = 0
# H7_num = range_of_atoms + 2

# adding bonds and changing hybridisation
def NewBonds():
	logging.info("Hybridising...")

	global range_of_atoms
	global H4_num
	global H7_num
	# global range_of_bonds

	# H3_num = 0
	# NewBonds.H4_num = []
	# H7_num = []
	H4_num = range_of_atoms + 1
	# H5_num = 0
	# H6_num = 0
	H7_num = range_of_atoms + 2

	SectionTemplate.atom_list["atom_%s" % H4_num] = {}
	SectionTemplate.atom_list["atom_%s" % H4_num]["atom_id"] = []
	SectionTemplate.atom_list["atom_%s" % H4_num]["atom_name"] = []
	SectionTemplate.atom_list["atom_%s" % H4_num]["x_coord"] = []
	SectionTemplate.atom_list["atom_%s" % H4_num]["y_coord"] = []
	SectionTemplate.atom_list["atom_%s" % H4_num]["z_coord"] = []
	SectionTemplate.atom_list["atom_%s" % H4_num]["atom_type"] = []
	SectionTemplate.atom_list["atom_%s" % H4_num]["atom_id"].append(str(H4_num))
	SectionTemplate.atom_list["atom_%s" % H4_num]["atom_name"].append('Hx')
	SectionTemplate.atom_list["atom_%s" % H4_num]["atom_type"].append('H')
	SectionTemplate.atom_list["atom_%s" % H4_num]["lig_name"] = SectionTemplate.atom_list["atom_%s" % C2i]["lig_name"]
	SectionTemplate.atom_list["atom_%s" % H4_num]["charge"] = []
	SectionTemplate.atom_list["atom_%s" % H4_num]["charge"] = 0.0000

	SectionTemplate.atom_list["atom_%s" % H7_num] = {}
	SectionTemplate.atom_list["atom_%s" % H7_num]["atom_id"] = []
	SectionTemplate.atom_list["atom_%s" % H7_num]["atom_name"] = []
	SectionTemplate.atom_list["atom_%s" % H7_num]["x_coord"] = []
	SectionTemplate.atom_list["atom_%s" % H7_num]["y_coord"] = []
	SectionTemplate.atom_list["atom_%s" % H7_num]["z_coord"] = []
	SectionTemplate.atom_list["atom_%s" % H7_num]["atom_type"] = []
	SectionTemplate.atom_list["atom_%s" % H7_num]["atom_id"].append(str(H7_num))
	SectionTemplate.atom_list["atom_%s" % H7_num]["atom_name"].append('Hr')
	SectionTemplate.atom_list["atom_%s" % H7_num]["atom_type"].append('H')
	SectionTemplate.atom_list["atom_%s" % H7_num]["lig_name"] = SectionTemplate.atom_list["atom_%s" % C2i]["lig_name"]
	SectionTemplate.atom_list["atom_%s" % H7_num]["charge"] = []
	SectionTemplate.atom_list["atom_%s" % H7_num]["charge"] = 0.0000


def NewAtom(atom_number, x, y, z, a1):
	global range_of_atoms
	global range_of_bonds
	print(SectionTemplate.atom_list.keys())
	print(H4_num, H7_num, "h4 h7")

	for atom in range(range_of_atoms+1):
		
		# print(atom, "atom")
		atom += 1
		print(atom, "atom", range_of_atoms)
		# if atom <= range_of_atoms:
		print(atom_number, "atom number")
		b = atom_number

		stripped_atom_number = (str(SectionTemplate.atom_list["atom_%s" % atom]["atom_id"]).strip('[' + '\'' + '\'' + ']'))
		print(stripped_atom_number, "stripped atm num")
		if len(stripped_atom_number) > 0:
			if b == int(stripped_atom_number):

				SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] = x
				SectionTemplate.atom_list["atom_%s" % atom]["y_coord"] = y
				SectionTemplate.atom_list["atom_%s" % atom]["z_coord"] = z
				
				range_of_atoms += 1
				print(range_of_atoms, "range from newatom")
				range_of_bonds += 1

				SectionTemplate.bond_list["bond_%s" % range_of_bonds] = {}
				SectionTemplate.bond_list["bond_%s" % range_of_bonds]["bond_id"] = []
				SectionTemplate.bond_list["bond_%s" % range_of_bonds]["a1"] = []
				SectionTemplate.bond_list["bond_%s" % range_of_bonds]["a2"] = []
				SectionTemplate.bond_list["bond_%s" % range_of_bonds]["bond_id"].append(str(range_of_bonds))
				SectionTemplate.bond_list["bond_%s" % range_of_bonds]["a1"] = a1
				SectionTemplate.bond_list["bond_%s" % range_of_bonds]["a2"] = atom_number
				SectionTemplate.bond_list["bond_%s" % range_of_bonds]["bond_type"] = 1

				Section.sections["section_%s" %3]["lines"].append('    ' + str(range_of_bonds) + '   ' + str(SectionTemplate.bond_list["bond_%s" % range_of_bonds]["a1"]) + '   ' + str(SectionTemplate.bond_list["bond_%s" % range_of_bonds]["a2"]) + ' ' + str(SectionTemplate.bond_list["bond_%s" % range_of_bonds]["bond_type"]) + '\n')

##### Minimisation data ################

def MinSection():
	MinSection.section_num_gaff = 0
	MinSection.sections = {}
	for n in range(5):
		MinSection.sections["section_%s" %n] = {}
		MinSection.sections["section_%s" %n]["name"] = []
		MinSection.sections["section_%s" %n]["lines"] = []


atom_list_new = {}
bond_list_new = {}

range_of_atoms_new = None
range_of_bonds_new = None
starting_range_of_atoms_new = None
starting_range_of_bonds_new = None


H_to_remove = None

####################################
# AcrylamideReaction data

# Xi = input atom ; Xt = template atom 

C1t_x = 26.5183
C1t_y = -0.3786
C1t_z = -8.1671

Ot_x = 25.9041
Ot_y = 0.6272
Ot_z = -8.4238

Ot_x_o = -0.6142
Ot_y_o = 1.0058
Ot_z_o = -0.2567

C2t_x = 27.7041
C2t_y = -0.4772
C2t_z = -7.2337

C3t_x = 28.3334
C3t_y = 0.8967
C3t_z = -6.8656

C3t_x_o = C3t_x - C1t_x
C3t_y_o = C3t_y - C1t_y
C3t_z_o = C3t_z - C1t_z

H3_x_trans = -0.7308
H3_y_trans = -0.1512
H3_z_trans = 0.8124

H4_x_trans = 0.9862
H4_y_trans = 0.1013
H4_z_trans = 0.4509

H5_x_trans = 0.2369
H5_y_trans = -0.0663
H5_z_trans = 1.0786

H6_x_trans = -0.7727
H6_y_trans = 0.857
H6_z_trans = 0.694

H7_x_trans = 0
H7_y_trans = 0.9
H7_z_trans = 0.8

atom = 0
bond = 0
a1 = 0
a2 = 0

oi_atom = 0
C1i = 0
C2i = 0
C3i = 0

angle_xy = 0.5482195632792037
angle_yz = 1.3563280100804826
angle_xy_C = 0
angle_yz_C = 0



# reacted acrylamide mol2 data 

	# #@<TRIPOS>ATOM
	     #  1 H1         25.4897   -1.3653   -9.5354 H         1 ACR    0.3095
	     #  2 N1         26.1670   -1.4904   -8.7999 N.pl3     1 ACR   -0.6820
	     #  3 C1         26.5183   -0.3786   -8.1671 C.2       1 ACR    0.6551
	     #  4 O1         25.9041    0.6272   -8.4238 O.2       1 ACR   -0.6131
	     #  5 C2         27.7041   -0.4772   -7.2337 C.3       1 ACR   -0.1474
	     #  6 C3         28.3334    0.8967   -6.8656 C.3       1 ACR   -0.0881
	     #  7 H2         26.6211   -2.3620   -8.6159 H         1 ACR    0.3095
	     #  8 H3         28.4686   -1.1035   -7.6998 H         1 ACR    0.0587
	     #  9 H5         27.5981    1.7186   -6.9541 H         1 ACR    0.0470
	     # 10 H6         29.1932    1.1263   -7.5190 H         1 ACR    0.0470
	     # 11 H7         28.6833    0.8725   -5.8214 H         1 ACR    0.0470
	     # 12 H4         27.3854   -0.9797   -6.3215 H         1 ACR    0.0587

	      # 1 H1         25.8868   -2.2508   -8.1749 H    1 COV
	      # 2 N1         26.2127   -1.5144   -8.7807 N.pl3    1 COV
	      # 3 C1         26.5183   -0.3786   -8.1671 C.2    1 COV
	      # 4 O1         26.5183   -0.3786   -6.961 O.2    1 COV
	      # 5 C2         26.7708   0.8217   -9.0518 C.3    1 COV
	      # 6 C3         26.6928   2.1837   -8.3049 C.3    1 COV
	      # 7 H2         26.2167   -1.587   -9.7779 H    1 COV
	      # 8 H3         26.04   0.8208   -9.8642 H    1 COV
	      # 9 H5         26.911   2.0701   -7.2263 H    1 COV
	      # 10 H6         25.6921   2.6376   -8.4122 H    1 COV
	      # 11 H7         27.4388   2.8765   -8.7255 H    1 COV
	      # 12 H4         27.7567   0.7177   -9.5027 H    1 COV
	# #@<TRIPOS>BOND
	#      1    1    2 1
	#      2    2    3 2
	#      3    2    7 1
	#      4    3    5 2
	#      5    3    4 1
	#      6    5    6 1
	#      7    5    8 1
	#      8    6    9 1
	#      9   10    6 1
	#     10   11    6 1
	#     11   12    5 1

	# '''

	#          CH3     C3  H5,6,7
	#         /  
	#      H2C         C2  H3,4
	#         \
	#          C=O     C1  O1
	#         /
	#        NH2       N1  H1,2
	# '''


	############Protein Processing##############

# sections_protein = {}

# atom_list_prot = {}
# bond_list_prot = {}
# substructure = {}

range_of_atoms_prot = None
range_of_bonds_prot = None
substructure_range = None
starting_range_of_atoms_prot = None
starting_range_of_bonds_prot = None
starting_substructure_range = None

section_num_protein = 0

cysteine_atoms = []			

#################
def ProteinSection():

	ProteinSection.sections_protein = {}
	ProteinSection.res_number = []
	ProteinSection.protein_charge = []

	for n in range(5):
		ProteinSection.sections_protein["section_%s" %n] = {}
		ProteinSection.sections_protein["section_%s" %n]["name"] = []
		ProteinSection.sections_protein["section_%s" %n]["lines"] = []

##############
def ProteinLists():
	ProteinLists.atom_list_prot = {}
	ProteinLists.bond_list_prot = {}
	ProteinLists.substructure = {}

	for i in range(range_of_atoms_prot):
		i += 1
		ProteinLists.atom_list_prot["atom_%s" % i] = {}

		ProteinLists.atom_list_prot["atom_%s" % i]["atom_id"] = []
		ProteinLists.atom_list_prot["atom_%s" % i]["atom_name"] = []
		ProteinLists.atom_list_prot["atom_%s" % i]["x_coord"] = []
		ProteinLists.atom_list_prot["atom_%s" % i]["y_coord"] = []
		ProteinLists.atom_list_prot["atom_%s" % i]["z_coord"] = []
		ProteinLists.atom_list_prot["atom_%s" % i]["atom_type"] = []
		ProteinLists.atom_list_prot["atom_%s" % i]["res_num"] = []
		ProteinLists.atom_list_prot["atom_%s" % i]["res_name"] = []
		ProteinLists.atom_list_prot["atom_%s" % i]["charge"] = []

	for b in range(range_of_bonds_prot):
		b += 1
		ProteinLists.bond_list_prot["bond_%s" % b] = {}

		ProteinLists.bond_list_prot["bond_%s" % b]["bond_id"] = []
		ProteinLists.bond_list_prot["bond_%s" % b]["a1"] = []
		ProteinLists.bond_list_prot["bond_%s" % b]["a2"] = []
		ProteinLists.bond_list_prot["bond_%s" % b]["type"] = []

	for s in range(substructure_range):
		s += 1
		ProteinLists.substructure["sub_%s" % s] = {}

		ProteinLists.substructure["sub_%s" % s]["id"] = []
		ProteinLists.substructure["sub_%s" % s]["resname"] = []
		ProteinLists.substructure["sub_%s" % s]["atmnum"] = []
		ProteinLists.substructure["sub_%s" % s]["type"] = []
		ProteinLists.substructure["sub_%s" % s]["num_1"] = []
		ProteinLists.substructure["sub_%s" % s]["chain"] = []
		ProteinLists.substructure["sub_%s" % s]["resname_2"] = []
		ProteinLists.substructure["sub_%s" % s]["num_2"] = []
		ProteinLists.substructure["sub_%s" % s]["comment"] = []