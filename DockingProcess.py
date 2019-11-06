import time
import logging
import subprocess

from FileLoading import args as args
from FileLoading import cwd as cwd
import DockInputs as dockInput
import ProgramData as data


class Docking():

	# new_lib_file = None

	def __init__(self):
		super(Docking, self).__init__()

		logging.info("Docking the molecule")
		self.libmerge()
		self.run_dock6()
		
	#merge the library 

	def libmerge(self):
		logging.info("Writing lib for dock6")
		with open("re_written_lib.mol2", "w") as new_lib:

			for molecule in range(data.mol_id):		
				molecule += 1
				molecule = str(molecule)
				input_molecule = "mol_" + molecule + "_" + args.mol2_filename[:-5]

				with open(cwd+"/"+input_molecule+"_charge.acpype/"+input_molecule+"_charge_user_gaff.mol2") as mol_file_in:
					for line in mol_file_in:
						new_lib.write(str(line))

			dockInput.new_lib_file = "re_written_lib.mol2"
			logging.info(dockInput.new_lib_file)
			#remove old files

	
	def run_dock6(self):
		# call dock6


		logging.info("running dock6")
		dockInput.InsphPrep()

		# # prepare the INSPH file
		# with open(args.dms_file) as dms_file:
		# 	logging.info("opening")

		# 	with open("INSPH", "w") as insph:
		# 			logging.info("creating INSPH file")

		# 			insph.write(args.dms_file + '\n')
		# 			insph.write("R" + '\n')
		# 			insph.write("X" + '\n')
		# 			insph.write("0.0" + '\n')
		# 			insph.write("4.0" + '\n')
		# 			insph.write("1.4" + '\n')
		# 			insph.write("spheres.sph" + '\n')

		cmd = ['sphgen', '-i', 'INSPH', '-o', 'OUTSPH']
		logging.info(str(cmd))
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		for line in p.stdout:
		    logging.info(line)
		p.wait()
		logging.info(p.returncode)

		cmd = ['sphere_selector', 'spheres.sph', 'cys_residue.mol2', '5.0']
		logging.info(str(cmd))
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		for line in p.stdout:
		    logging.info(line)
		p.wait()
		logging.info(p.returncode)


		dockInput.ShowBox()

		dockInput.GridPrep()


		cmd = ['grid', '-i', 'grid.in', '-o', 'gridinfo.out']
		logging.info("creating grid")
		logging.info(str(cmd))
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		for line in p.stdout:
		    logging.info(line)
		p.wait()
		logging.info(p.returncode)
		

		dockInput.FlexDock()
				
		# search for 'ligand_atom_file' line - edit it to ass the correct name of the library from previous functions
		# with open(args.in_file) as in_file_edit:
		# 	logging.info("opening")


			# with open("showbox.in", "w") as showbox:
			# 	logging.info("creating grid file")

			# 	showbox.write("Y" + '\n')
			# 	showbox.write("8" + '\n')
			# 	showbox.write("selected_spheres.sph" + '\n')
			# 	showbox.write("1" + '\n')
			# 	showbox.write("box.pdb" + '\n')

			# with open("grid.in", 'w') as grid:
			# 	grid.write("compute_grids yes" + '\n')
			# 	grid.write("grid_spacing 0.4" + '\n')
			# 	grid.write("output_molecule no" + '\n')
			# 	grid.write("contact_score no" + '\n')
			# 	grid.write("energy_score yes" + '\n')
			# 	grid.write("energy_cutoff_distance 9999" + '\n')
			# 	grid.write("atom_model a" + '\n')
			# 	grid.write("attractive_exponent 6" + '\n')
			# 	grid.write("repulsive_exponent 12" + '\n')
			# 	grid.write("distance_dielectric yes" + '\n')
			# 	grid.write("dielectric_factor              4" + '\n')
			# 	grid.write("bump_filter yes" + '\n')
			# 	grid.write("bump_overlap 0.75" + '\n')
			# 	grid.write("receptor_file" + '  ' + str(args.protein_mol2[:-5]) +"_charge.mol2" + '\n')
			# 	grid.write("box_file box.pdb" + '\n')
			# 	grid.write("vdw_definition_file /home/sylvia/software/dock6/parameters/vdw_AMBER_parm99.defn" + '\n')
			# 	grid.write("score_grid_prefix grid " + '\n')

			# with open("newlib_dock.in", "w") as temp:
			# 	logging.info("creating temp file")

			
			# 	for line in in_file_edit:
			# 		# logging.info("lines")

			# 		if line.startswith("ligand_atom_file"):
			# 			logging.info(line)
			# 			line_edit = str("ligand_atom_file                                             "+str(self.new_lib_file) + '\n')
			# 			logging.info(line_edit)
			# 			line = line_edit
			# 			temp.write(str(line))

			# 		elif line.startswith("rmsd_reference_filename"):
			# 			logging.info(line)
			# 			line_edit = str("rmsd_reference_filename                                      "+str(self.new_lib_file) + '\n')
			# 			logging.info(line_edit)
			# 			line = line_edit
			# 			temp.write(str(line))

			# 		elif not line.startswith("ligand_atom_file") or line.startswith("rmsd_reference_filename"):
			# 			temp.write(str(line))

		# generate spheres
		# add code to check the dir is OUTSPH is present - if yes, delete it before running the code	
		# cmd = ['sphgen', '-i', 'INSPH', '-o', 'OUTSPH']
		# logging.info(str(cmd))
		# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		# for line in p.stdout:
		#     logging.info(line)
		# p.wait()
		# logging.info(p.returncode)


		# cmd = ['sphere_selector', 'spheres.sph', 'cys_residue.mol2', '5.0']
		# logging.info(str(cmd))
		# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		# for line in p.stdout:
		#     logging.info(line)
		# p.wait()
		# logging.info(p.returncode)

		#generate grid

		# cmd = ['showbox','<','showbox.in']
		# logging.info("creating box")
		# logging.info(str(cmd))
		# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		# for line in p.stdout:
		#     logging.info(line)
		# p.wait()
		# logging.info(p.returncode)
		

		# cmd = ['grid', '-i', 'grid.in', '-o', 'gridinfo.out']
		# logging.info("creating grid")
		# logging.info(str(cmd))
		# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		# for line in p.stdout:
		#     logging.info(line)
		# p.wait()
		# logging.info(p.returncode)
		

		cmd = ['dock6', '-i' ,'%s' % "newlib_dock.in"]
		logging.info("docking")
		logging.info(str(cmd))
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		for line in p.stdout:
		    logging.info(line)
		p.wait()
		logging.info(p.returncode)



Docking()