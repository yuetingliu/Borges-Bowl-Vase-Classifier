
# generate new images with the newly generated bom files and Borges API
# usage $ python create_new_bom.py <num_images> <seed>

from create_new_bom import *
import sys
import glob

# Params
num_images=10
seed=0
if len(sys.argv)>1:
	num_images = int(sys.argv[1])
if len(sys.argv)>2:
	seed=int(sys.argv[2])

old_bom_path = './Borges_assessment_data/datadir/vase/bom/*'
new_bom_path = './new_image_files/vase/bom'
new_image_path = './new_image_files/vase/png/'

# Generate new bom files
old_boms = glob.glob(old_bom_path)
for old_bom in old_boms[:num_images]:
	create_new_bom(old_bom, seed=seed, save_path=new_bom_path)

# Generate new png images
# The following codes are from Borges new png generating script
outpath = new_image_path
# Generate new images only with new boms files (filter with name)
filter_name = 'new'+str(seed)+'_'
new_bom_files = glob.glob(new_bom_path+'/*')
for new_bom in [bom for bom in new_bom_files if filter_name in bom]:
	filename = new_bom
	head, tail = os.path.split(filename)
	root, _ = os.path.splitext(tail)

	# generate a thumbnail of the model via the remote api
	cmd = "curl -k -o \"" + outpath + root + ".png\" -H \"Content-Type: application/json\" -X POST -d @" + filename + "  https://dev.borges.xyz/api/thumbnail/?size=256"
	os.system( cmd )

	# # generate an stl file of the model via the remote api
	# cmd = "curl -k -o \"" + outpath + root + ".stl\" -H \"Content-Type: application/json\" -X POST -d @" + filename + "  https://dev.borges.xyz/object/stl/"
	# os.system( cmd )

