
import re
######### numbering of ligands and poses ##############

with open("flex_scored.mol2") as flex_scored:

	with open("scored_numbered.mol2", "w") as numbering:

		pose_id = 0
		ligand_id = 0
		ligands = {}
	
		for line in flex_scored:

			if line.startswith('#'):
				if 'Name:' in line:
					name = line.strip('#')
					name = name.strip(' ')
					name = name.strip('Name:')
					name = name.strip(' ')
					
					if name not in ligands.keys():
						ligand_id += 1

						ligands[name] = {}
						ligands[name]["ligand_id"] = ligand_id
						ligands[name]["pose_count"] = 1

						pose_id = ligands[name]["pose_count"]

						numbering.write(str(ligand_id) + '  ' + str(pose_id) + ' ' + line)

					else:
						ligands[name]["pose_count"] += 1

						pose_id = ligands[name]["pose_count"]
						ligand_id = ligands[name]["ligand_id"]

						numbering.write(str(ligand_id) + '  ' + str(pose_id) + ' ' + line)

				else:
					numbering.write(str(ligand_id) + '  ' + str(pose_id) + ' ' + line)

			else:
				numbering.write(str(ligand_id) + '  ' + str(pose_id) + ' ' + line)

		numbering.write("EOF")


################# load the numbered file to begin the scoring process #########################################

with open("scored_numbered.mol2") as numligsfile:
	with open("scored_ligands_temp.mol2", 'w') as scored_file:

		template = []
		reference = []

		current_pose = 1
		current_ligand = 1
		es_energy = None
		reference_es_energy = 100

		print(current_ligand)

		for line in numligsfile:

			if line.startswith('0'):
				print("Ordering")

			elif line.startswith('EOF'):
				print(line)
				for item in reference:
					scored_file.write(item)

			else:

				col = line.split()

				if int(col[0]) == int(current_ligand):

					if int(col[1]) == int(current_pose):

						template.append(line)

					elif (current_pose + 1) <= 66:

						for item in template:

							if "Grid_es_energy:" in item:

								item = item[10:]
								es_energy = item.strip('#')
								es_energy = es_energy.strip(' ')
								es_energy = es_energy.strip('Grid_es_energy:')
								es_energy = es_energy.strip(' ')
								es_energy = es_energy.strip( '\n')
								es_energy = es_energy.strip( '\'')

								if float(es_energy) < float(reference_es_energy):
									reference = template
									reference_es_energy = es_energy
									template = []
									template.append(line)

								else:
									template = []
									template.append(line)

						current_pose += 1
						template = []
						template.append(line)

					else:

						for item in reference:
							scored_file.write(item)

						current_ligand += 1
						current_pose = 1
						reference = []
						template = []
						template.append(line)
						reference_es_energy = 100

				else:

					for item in reference:
						scored_file.write(item)

					current_ligand += 1
					current_pose = 1
					reference = []
					template = []
					template.append(line)
					reference_es_energy = 100


################## tidy file ############

with open("scored_ligands_temp.mol2") as temp:
	with open("scored_ligands.mol2", 'w') as final:

		for line in temp:
			split_line = re.split(r'(\s+)', line)
			fresh_line = ''.join(split_line[3:])
			final_line = fresh_line[1:]
			final.write(final_line)

