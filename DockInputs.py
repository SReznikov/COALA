import time
import logging

from FileLoading import args as args
# from DockingProcess import new_lib_file as new_lib_file


new_lib_file = None

def InsphPrep():
	# prepare the INSPH file
	with open(args.dms_file) as dms_file:
		logging.info("opening")

		with open("INSPH", "w") as insph:
				logging.info("creating INSPH file")

				insph.write(args.dms_file + '\n')
				insph.write("R" + '\n')
				insph.write("X" + '\n')
				insph.write("0.0" + '\n')
				insph.write("4.0" + '\n')
				insph.write("1.4" + '\n')
				insph.write("spheres.sph" + '\n')




def ShowBox():

	logging.info("creating grid file")

	with open("selected_spheres.sph") as sph:
		x_coords = []
		y_coords = []
		z_coords = []
		box_buffer = 8

		lines = sph.readlines()[2:]

		for line in lines:
			# if not line.startswith(str):
			# print(line)

			col = line.split()
			# if len(col) == 8:
			# 	print(line)
			# 	x = col[1]
			# 	y = col[2]
			# 	z = col[3]

			# 	if isinstance(x, float) == True and isinstance(y, float) == True and isinstance(z, float) == True:
					
			# 		print(x, y, z, "floats")
					# if x
			x_coords.append(float(col[1]))
			y_coords.append(float(col[2]))
			z_coords.append(float(col[3]))

		# print(x_coords)

		x_center = sum(x_coords)/float(len(x_coords))
		y_center = sum(y_coords)/float(len(y_coords))
		z_center = sum(z_coords)/float(len(z_coords))
		print(x_center, y_center, z_center)


		x_dimension = (max(x_coords) - min(x_coords)) + 2*box_buffer
		y_dimension = (max(y_coords) - min(y_coords)) + 2*box_buffer
		z_dimension = (max(z_coords) - min(z_coords)) + 2*box_buffer

		print(x_dimension, y_dimension, z_dimension)

		node_1_x = x_center - 0.5*x_dimension
		node_1_y = y_center - 0.5*y_dimension
		node_1_z = z_center - 0.5*z_dimension

		print(node_1_x,node_1_y, node_1_z, "nodes")

		node_2_x = node_1_x + x_dimension
		node_2_y = node_1_y
		node_2_z = node_1_z

		node_3_x = node_2_x
		node_3_y = node_1_y
		node_3_z = node_1_z + z_dimension

		node_4_x = node_1_x
		node_4_y = node_1_y
		node_4_z = node_1_z + z_dimension

		node_5_x = node_1_x
		node_5_y = node_1_y + y_dimension
		node_5_z = node_1_z

		node_6_x = node_2_x
		node_6_y = node_5_y
		node_6_z = node_1_z

		node_7_x = node_2_x
		node_7_y = node_5_y
		node_7_z = node_3_z

		node_8_x = node_1_x
		node_8_y = node_5_y
		node_8_z = node_4_z

	with open("box.pdb", "w") as showbox:
		space1 = "      "
		space2 = "  "
		space3 = " "
		showbox.write("HEADER" + "    " + "CORNERS OF BOX" + '\n')
		showbox.write("REMARK" + "    " + "CENTER (X Y Z)" + "   " + str("%.3f" % x_center) + space2 + str("%.3f" % y_center) + space3 + str("%.3f" % z_center) + '\n')
		showbox.write("REMARK" + "    " + "DIMENSIONS (X Y Z)" + "   " + str("%.3f" % x_dimension) + space2 + str("%.3f" % y_dimension) + space3 + str("%.3f" % z_dimension) + '\n')
		showbox.write("ATOM" + "      " + "1" + "  " + "DUA" + " " + "BOX" + "     " + "1" + space1 + str("%.3f" % node_1_x) + space2 + str("%.3f" % node_1_y) + space3 + str("%.3f" % node_1_z) + '\n')
		showbox.write("ATOM" + "      " + "2" + "  " + "DUB" + " " + "BOX" + "     " + "1" + space1 + str("%.3f" % node_2_x) + space2 + str("%.3f" % node_2_y) + space3 + str("%.3f" % node_2_z) + '\n')
		showbox.write("ATOM" + "      " + "3" + "  " + "DUC" + " " + "BOX" + "     " + "1" + space1 + str("%.3f" % node_3_x) + space2 + str("%.3f" % node_3_y) + space3 + str("%.3f" % node_3_z) + '\n')
		showbox.write("ATOM" + "      " + "4" + "  " + "DUD" + " " + "BOX" + "     " + "1" + space1 + str("%.3f" % node_4_x) + space2 + str("%.3f" % node_4_y) + space3 + str("%.3f" % node_4_z) + '\n')
		showbox.write("ATOM" + "      " + "5" + "  " + "DUE" + " " + "BOX" + "     " + "1" + space1 + str("%.3f" % node_5_x) + space2 + str("%.3f" % node_5_y) + space3 + str("%.3f" % node_5_z) + '\n')
		showbox.write("ATOM" + "      " + "6" + "  " + "DUF" + " " + "BOX" + "     " + "1" + space1 + str("%.3f" % node_6_x) + space2 + str("%.3f" % node_6_y) + space3 + str("%.3f" % node_6_z) + '\n')
		showbox.write("ATOM" + "      " + "7" + "  " + "DUG" + " " + "BOX" + "     " + "1" + space1 + str("%.3f" % node_7_x) + space2 + str("%.3f" % node_7_y) + space3 + str("%.3f" % node_7_z) + '\n')
		showbox.write("ATOM" + "      " + "8" + "  " + "DUH" + " " + "BOX" + "     " + "1" + space1 + str("%.3f" % node_8_x) + space2 + str("%.3f" % node_8_y) + space3 + str("%.3f" % node_8_z) + '\n')
		showbox.write("CONECT" + "    " + "1" + "    " + "2" + "    " + "4" + "    " + "5" + '\n')
		showbox.write("CONECT" + "    " + "2" + "    " + "1" + "    " + "3" + "    " + "6" + '\n')
		showbox.write("CONECT" + "    " + "3" + "    " + "2" + "    " + "4" + "    " + "7" + '\n')
		showbox.write("CONECT" + "    " + "4" + "    " + "1" + "    " + "3" + "    " + "8" + '\n')
		showbox.write("CONECT" + "    " + "5" + "    " + "1" + "    " + "6" + "    " + "8" + '\n')
		showbox.write("CONECT" + "    " + "6" + "    " + "2" + "    " + "5" + "    " + "7" + '\n')
		showbox.write("CONECT" + "    " + "7" + "    " + "3" + "    " + "6" + "    " + "8" + '\n')
		showbox.write("CONECT" + "    " + "8" + "    " + "4" + "    " + "5" + "    " + "7" + '\n')



def GridPrep():
	with open("grid.in", 'w') as grid:
		grid.write("compute_grids yes" + '\n')
		grid.write("grid_spacing 0.4" + '\n')
		grid.write("output_molecule no" + '\n')
		grid.write("contact_score no" + '\n')
		grid.write("energy_score yes" + '\n')
		grid.write("energy_cutoff_distance 9999" + '\n')
		grid.write("atom_model a" + '\n')
		grid.write("attractive_exponent 6" + '\n')
		grid.write("repulsive_exponent 12" + '\n')
		grid.write("distance_dielectric yes" + '\n')
		grid.write("dielectric_factor              4" + '\n')
		grid.write("bump_filter yes" + '\n')
		grid.write("bump_overlap 0.75" + '\n')
		grid.write("receptor_file" + '  ' + str(args.protein_mol2[:-5]) +"_charge.mol2" + '\n')
		grid.write("box_file box.pdb" + '\n')
		grid.write("vdw_definition_file /home/sylvia/software/dock6/parameters/vdw_AMBER_parm99.defn" + '\n')
		grid.write("score_grid_prefix grid " + '\n')


def FlexDock():
	with open(args.in_file) as in_file_edit:
		logging.info("opening")

		with open("newlib_dock.in", "w") as temp:
			logging.info("creating temp file")

		
			for line in in_file_edit:
				# logging.info("lines")

				if line.startswith("ligand_atom_file"):
					logging.info(line)
					line_edit = str("ligand_atom_file                                             "+str(new_lib_file) + '\n')
					logging.info(line_edit)
					line = line_edit
					temp.write(str(line))

				elif line.startswith("rmsd_reference_filename"):
					logging.info(line)
					line_edit = str("rmsd_reference_filename                                      "+str(new_lib_file) + '\n')
					logging.info(line_edit)
					line = line_edit
					temp.write(str(line))

				elif not line.startswith("ligand_atom_file") or line.startswith("rmsd_reference_filename"):
					temp.write(str(line))