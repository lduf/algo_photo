# algo_photo
Des algos dev pour nous faciliter la vie en photo

Parfois, souvent on peut avoir des tâches répétitives à effectuer sur nos photos (genre passer nos négatifs en positifs ^^). 
Flemme d'utiliser photoshop ou d'appliquer un preset sur l'ensemble de mes photos. Vous trouverez ici des algos en python pour faire ces tâches.

## invertImg 

Celui là permet d'inverser les couleurs d'une photo : **negatif -> positif** (et fatalement l'inverse). 

Pour l'utiliser, on l'appelle en lui passant comme argument un chemin. Si ce chemin est un fichier, ce dernier sera convertit ; si c'est un dossier, l'ensemble des fichiers seront convertis (ouaa c bo) ! Les fichiers ne seront pas écrasés. Les nouvelles photos seront enregistrées dans un dossier nommé `positif`

*Exemple d'appel du script*

	invertImg path/to/my/folder
	//convertir l'ensemble des photos
	invertImg path/to/my/file.{JPG/JPEG/PNG}
	//convertir une seule photo
  
## grayscale 

Celui là permet de passer une photo en nuance de gris 

Même fonctionnement que invertImg. Les nouvelles photos seront enregistrées dans un dossier nommé `grayscale`

*Exemple d'appel du script*

	grayscale path/to/my/folder
	//convertir l'ensemble des photos
	grayscale path/to/my/file.{JPG/JPEG/PNG}
	//convertir une seule photo
