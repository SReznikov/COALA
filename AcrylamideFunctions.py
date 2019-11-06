import numpy as np
import math

import ProgramData as data



# def reaction():
			
# 	print("called reaction func")
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




# set the common origin
def Origin(tanslate_x, tanslate_y, tanslate_z):
	# assign new, translated coordinates
	for atom in range(data.range_of_atoms):
		atom += 1

		# if atom < data.range_of_atoms:

		if data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] != []:

			data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] = float(data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"]) - tanslate_x
			data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"] = float(data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"]) - tanslate_y
			data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"] = float(data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"]) - tanslate_z


def MatrixMultiplication(A, B, atom):

	x_conv = []
	y_conv = []
	z_conv = []
	
	a = np.array(A)
	b = np.array(B)

	result = [  [0], [0], [0]  ]

	result = (a.dot(b))

	x_conv = str(result[0])
	y_conv = str(result[1])
	z_conv = str(result[2])


	data.SectionTemplate.atom_list["atom_%s" % atom]["x_coord"] = float(x_conv.strip('[' + ']'))
	data.SectionTemplate.atom_list["atom_%s" % atom]["y_coord"] = float(y_conv.strip('[' + ']'))
	data.SectionTemplate.atom_list["atom_%s" % atom]["z_coord"] = float(z_conv.strip('[' + ']'))

	return


def AngleCalc():
	# calculation of angles using the default setting
	# self.angle_xy_C = 0
	# self.angle_yz_C = 0

	if int(data.oi_atom) > 0:

		if data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["x_coord"] < 0:

			vec_x_to_y = ( data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["y_coord"]) / ( math.sqrt( (data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["x_coord"] ** 2) + (data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["y_coord"] ** 2) ) )
			data.angle_xy_C = math.acos( vec_x_to_y )

		if data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["x_coord"] >= 0:

			vec_x_to_y = (- data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["y_coord"]) / ( math.sqrt( (data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["x_coord"] ** 2) + (data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["y_coord"] ** 2) ) )
			data.angle_xy_C = math.acos( vec_x_to_y )

		if data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["y_coord"] < 0:
			vec_y_to_z = ( data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["z_coord"]) / ( math.sqrt( (data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["z_coord"] ** 2) + (data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["y_coord"] ** 2) ) )
			data.angle_yz_C = math.acos(vec_y_to_z)

		if data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["y_coord"] >= 0:	

			vec_y_to_z = (- data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["z_coord"]) / ( math.sqrt( (data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["z_coord"] ** 2) + (data.SectionTemplate.atom_list["atom_%s" % data.oi_atom]["y_coord"] ** 2) ) )
			data.angle_yz_C = math.acos(vec_y_to_z)

		return

def AngleCalc2():
	# angle calculation after recalculation of coordinates

	# self.angle_xy_C = 0
	# self.angle_yz_C = 0

	if data.C2i == 0:
		logging.error("Error: no adjecent sp2 carbon")


	if data.C2i != 0:

		if data.SectionTemplate.atom_list["atom_%s" % data.C2i]["x_coord"] < 0:

			vec_x_to_y = ( data.SectionTemplate.atom_list["atom_%s" % data.C2i]["y_coord"]) / ( math.sqrt( (data.SectionTemplate.atom_list["atom_%s" % data.C2i]["x_coord"] ** 2) + (data.SectionTemplate.atom_list["atom_%s" % data.C2i]["y_coord"] ** 2) ) )
			data.angle_xy_C = math.acos( vec_x_to_y )

		if data.SectionTemplate.atom_list["atom_%s" % data.C2i]["x_coord"] >= 0:

			vec_x_to_y = (- data.SectionTemplate.atom_list["atom_%s" % data.C2i]["y_coord"]) / ( math.sqrt( (data.SectionTemplate.atom_list["atom_%s" % data.C2i]["x_coord"] ** 2) + (data.SectionTemplate.atom_list["atom_%s" % data.C2i]["y_coord"] ** 2) ) )
			data.angle_xy_C = math.acos( vec_x_to_y )

		if data.SectionTemplate.atom_list["atom_%s" % data.C2i]["y_coord"] < 0:
			vec_y_to_z = ( data.SectionTemplate.atom_list["atom_%s" % data.C2i]["z_coord"]) / ( math.sqrt( (data.SectionTemplate.atom_list["atom_%s" % data.C2i]["z_coord"] ** 2) + (data.SectionTemplate.atom_list["atom_%s" % data.C2i]["y_coord"] ** 2) ) )
			data.angle_yz_C = math.acos(vec_y_to_z)

		if data.SectionTemplate.atom_list["atom_%s" % data.C2i]["y_coord"] >= 0:	

			vec_y_to_z = (- data.SectionTemplate.atom_list["atom_%s" % data.C2i]["z_coord"]) / ( math.sqrt( (data.SectionTemplate.atom_list["atom_%s" % data.C2i]["z_coord"] ** 2) + (data.SectionTemplate.atom_list["atom_%s" % data.C2i]["y_coord"] ** 2) ) )
			data.angle_yz_C = math.acos(vec_y_to_z)

	return

def charge_calc(atom_list_new_in, range_of_atoms_new):

		negative_charges = []
		positive_charges = []

		data.atom_list_new = atom_list_new_in
		range_of_atoms_new = range_of_atoms_new

		for c in range(range_of_atoms_new):
			c += 1

			for item in data.atom_list_new["atom_%s" % c]["charge"]:

				if float(item) < 0:
					for i in data.atom_list_new["atom_%s" % c]["charge"]:
						negative_charges.append(float(i))

				if float(item) > 0:
					for i in data.atom_list_new["atom_%s" % c]["charge"]:
						positive_charges.append(float(i))

		return round(sum(negative_charges), 4), round(sum(positive_charges), 4)
