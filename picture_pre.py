from PIL import Image
import glob
from tqdm import tqdm






def changeExtensionBatch(input_file, output_file,change_name_flag = False,target_Extension = 'png'):

	def change(path_in, path_out):

		t_e = target_Extension
		if t_e.upper() == 'JPG':
			t_e = 'JPEG'

		img = Image.open(path_in)
		img = img.convert("RGB")
		img.save(path_out, t_e.upper(), quality=80, optimize=True, progressive=True)


	input_list = glob.glob(input_file+'/*')
	for index,every_file in enumerate(tqdm(input_list)):
		
		name = every_file.split('/')[-1]
		e_n = name.split('.')[-1]
		f_n = name[:-(len(e_n) + 1)]
		if change_name_flag:
			change(every_file, output_file + '/' +str(index) + '.' + target_Extension)
		else:
			change(every_file, output_file + '/' +f_n + '.' + target_Extension)


def changeSizeBatch(input_file, output_file, width, height):
	input_list = glob.glob(input_file+'/*')
	for index,every_file in enumerate(tqdm(input_list)):

		
		img = Image.open(every_file)
		img.resize((width, height))
		img.save(path_out, t_e.upper(), quality=80, optimize=True, progressive=True)


		



changeExtension('./picture','./new_picture',change_name_flag=True,target_Extension='png')
