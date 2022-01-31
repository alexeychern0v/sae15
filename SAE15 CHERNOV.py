

import requests
from lxml import etree

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY','FR_MTP_SABL'] 

total=0 #on defini le nombre de places en total a Montpellier
totallibre=0 #le nombre de places libres en total a Montpellier

for i in range (len(parkings)):
   
    url="https://data.montpellier3m.fr/sites/default/files/ressources/"+parkings[i]+".xml"
    response=requests.get(url) #on obtient les fichier xml de chaque parking

    tree=etree.fromstring(response.content)

    for user in tree.xpath("Name"):
	    print( 'Nom du parking :', user.text) #on obtient le nom du parking
    
    for user in tree.xpath("Total"):
        print('Nombre total de places :', user.text) #on obtient le nombre de places en total du parking
        parktotal=user.text #on le met dans un variable parktotal pour apres le manipuler
        total+=int(parktotal) #on ajoute le nombre de places du parking au nombre total de place a Montpellier
        
    for user in tree.xpath("Free"):
        print('Nombre de places libres : ' , user.text) #on obtient le nombre de places libres du parking
        parklibre=user.text #on le met dans un variable parklibre pour apres le manipuler
        totallibre+=int(parklibre) #on ajoute le nombre de places libres du parking au nombre total de place libres a Montpellier
        
    pourcent=int(((int(parktotal)-int(parklibre))*100)/int(parktotal)) #on calcule le pourcentage de places occupe du parking
    print("Pourcentage de place occupe: "+str(pourcent)+" %")

occupe= int(((total-totallibre)*100)/total) #on calcule le pourcentage de places occupe du parking a Montpellier
print("places en totale a Montpellier ", total)
print("Places libres a Montpellier ", totallibre)
print("Pourcentage de place occupe a Montpellier: "+str(occupe)+" %")

#maintenant pour le cas de velos

velototal=0 #on defini le nombre de places en total a Montpellier (velos)
velolibre=0 #le nombre de places libres en total a Montpellier (velos)

b="https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml"
response=requests.get(b) #on recupere des donnes
tree=etree.fromstring(response.content)

for si in tree.xpath("/vcs/sl/si"):
    total=si.get('to') #on met le nombre de places en total du parking velo dans un variable parktotal pour apres le manipuler
    velototal+=int(total) #on ajoute le nombre de places du parking au nombre total de place velo a Montpellier
    free=si.get('fr') #on met le nombre de places libres en total du parking velo dans un variable parktotal pour apres le manipuler
    velolibre+=int(free) #on ajoute le nombre de places libres du parking au nombre total de place velo libres a Montpellier
occupe=int(((velototal-velolibre)*100)/velototal) #on calcule le pourcentage de places occupe du parking velo a Montpellier

print("places velo en total a Montpellier ", velototal)
print("Places libres velo a Montpellier ", velolibre)
print("Pourcentage de place velo occupe a Montpellier: "+str(occupe)+" %")