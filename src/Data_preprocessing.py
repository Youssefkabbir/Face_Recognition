# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:01:15 2022

@author: 21260
"""

import os
import pandas as pd
#on donne le chemin de notre dataset qui contient  les images de cahque personne
train_data_dir=r'C:\\Users\\21260\\Projet\\Face_Recognition\\src\\resources\\Data\\Dataset'

#on créons la  liste Y et la liste Z
Y = []
Z = []
#cette variable pour voir le nombre des échtillons de cahque classe
i=0
#on va boucler dans toutes les dossiers qu' otn dans le chemin train_data_dir
folders=os.listdir(train_data_dir)
for class_dir in folders:
    i=0
    print(class_dir)    
    for image_name in os.listdir(os.path.join(train_data_dir, class_dir)):
        path_image=os.path.join(train_data_dir,class_dir, image_name)
        #on ajoute cahque classe que on trouve dans notre  dataset à la liste Y           
        Y.append(class_dir)
        #on ajoute cahque chemin de chaque image que on trouve dans notre  dataset à la liste Z           
        Z.append(path_image)
        i+=1
    #on ' affiche le nombre des échontillions  de chaque sous dossier
    print(i)
                  
#
label = pd.DataFrame(Y,columns=['classe']) 
path = pd.DataFrame(Z,columns=['path']) 
result2 = pd.merge(path,label,left_index=True, right_index=True)
#on transforme notre data en  format .csv
result2.to_csv (r'C:\\Users\\21260\\Projet\\Face_Recognition\\src\\resources\\Data\\datacsv\\datacsv.csv',index = None, header=True)
