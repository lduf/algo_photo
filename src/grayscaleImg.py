#! /usr/local/bin/python3

from PIL import Image
import PIL.ImageOps
from os import walk
import os, sys

def convert(path) :
	""" Cette fonction permet de convertir et d'enregister le contenu du path"""
	extention = ["JPG", "JPEG", "PNG"] #extention autorisée pour la conversion
	f = [] # on a ici la liste des fichiers sur lesquels on va travailler
		
	# si c'est un dossier, on parse tous les élements dudit dossier
	if(os.path.isdir(path)) :
		for(dirpath, dirnames, filenames) in walk(path) :
			f.extend(filenames)
			break
	# si c'est un fihier on l'ajoute juste à la liste des fichiers sur lesquels on travail
	if(os.path.isfile(path)) :
		head, tail = os.path.split(path)
		f.append(tail)
		path=head+"/"
	if(path[-1] !=  "/"):
		path+="/"
	pathInv = path+"grayscale/"
	#Si pathInv n'existe pas je le crée
	if( not os.path.isdir(pathInv)):
		os.mkdir(pathInv)

	f = [elt for elt in f if any(ext in elt.upper() for ext in extention)]
	#on fait la conversion et on enregistre notre taff
	for i,elt in enumerate(f) :
		if any(ext in elt.upper() for ext in extention):
			print("****  processing {} : {}/{} ****".format(elt, i+1, len(f)))
			image = Image.open(path+elt)
			if 'png' in elt :
				gray_image = image.convert('LA')
			else :
				gray_image = image.convert('L')
			gray_image.save(pathInv+"/"+elt)

if len(sys.argv) != 2 :
	print("2 args needed")
else :
	path = str(sys.argv[1])
	if(not (os.path.isfile(path) or os.path.isdir(path))) :
		print("L'élément {} n'existe pas".format(path))
	else :
		convert(path)
