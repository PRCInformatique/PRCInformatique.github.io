#Coding:utf-8
Amperemetre = """Un Ampèremetre est un instrument qui permet de mesurer l'intensité du courant électrique \
dans un circuit. Il se branche en série dans le circuit et comporte deux bornes: \
le positif (+ en rouge) et le négatif (- en noir). La borne + est relié à la borne positif du générateur \
de sorte que le courant entre par la borne positive et sort par celle négative."""

Amperemetre_aiguille = """ Un ampèremètre à aiguille possède une aiguille qui devie devant un cadran gradué et qui \
indique le nombre de divisions. Le nombre de divisions correspondant à la déviation de l'aiguille est \
proportionnel à l'intensité du courant qui traverse l'ampèremètre.\
"""

Calibre = """Le calibre d'un ampèremètre représente l'intensité maximale que l'appareil peut \
mésurer lorsqu'il fonctionne sur ce calibre: c'est l'intensité du courant traversant l'appareil \
lorsque l'aiguille se place sur la dernière division de la graduation (à droite)."""

Intensite_Calibre = """Pour déterminer l'intensité du courant mésuré avec un ampèremètre a calibre (Imésurer), \
on multiplie le nombre de division lu (n) par la valeur du calibre choisi (Ic) et on divise par le nombre total \
de division (N). Soit Imésuer = (n * Ic)/N"""

Calcule_intensité = lambda Ic,n,N : (n*Ic)/N