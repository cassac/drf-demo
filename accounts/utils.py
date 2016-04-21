import os
import datetime

from PIL import Image
from django.conf import settings
from .models import Picture

def attach_pictures(fortune, pictures):
	today = datetime.datetime.today()
	for picture in pictures:
		image = Image.open(picture)
		image_type = picture.split('.')[-1]
		filename = picture.split('/')[-1]
		dir_structure = '%d/%02d/%02d' % (today.year, today.month, today.day)
		dir_path = os.path.join(settings.MEDIA_ROOT, dir_structure)
		full_path = os.path.join(dir_path, filename)
		file_path = os.path.join(dir_structure, filename)
		try:
			os.stat(dir_path)
		except:
			os.makedirs(dir_path)
		Picture(fortune=fortune, image=file_path).save()
		image.save(full_path, image_type)