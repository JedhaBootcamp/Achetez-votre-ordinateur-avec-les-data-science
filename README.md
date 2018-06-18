# Achetez votre ordinateur avec les Data Sciences
### Projet de Guillaume Vilain - Batch#2

## Introduction

Vous vous êtes déjà surement posé ce problème : vous voulez acheter un ordinateur au meilleur prix, mais vous faites face à plusieurs difficultés. Il y a beaucoup de critères à prendre en compte, dont certains sont assez techniques, et vous n’avez pas tellement le temps pour vous informer précisément.

Sortir des tendances significatives d’un grand ensemble de données hétérogène est précisément l’intérêt des statistiques. L’étude s’attache ainsi à savoir comment les algorithmes de Machine Learning peuvent nous aider à faire des choix complexes et ce jusque dans ce problème de la vie quotidienne.

L’algorithme choisi pour répondre à cette problématique est celui de la régression linéaire multi-variable. L’algorithme détermine les coefficients de l’équation linéaire permettant de prédire au mieux le prix de l’ensemble des ordinateurs de la base de données. Les coefficients ainsi déterminés prennent en compte la présence ou non de chaque composant ainsi que la valeur de chaque caractéristique. Ils représentent ainsi un prix « moyen » pour chaque composant ou caractéristique.


## Données, préparation et nettoyage

La base de données est agrégée depuis la page internet du revendeur. Le texte est directement copié du site internet. La méthode est ainsi transposable à tous les sites d’e-commerce. Les données textuelles sont ensuite réorganisées grâce aux fonctions automatiques d’un logiciel de type tableur. L’exemple d’analyse se base sur 26 ordinateurs afin que l’exercice puisse être réalisé dans un temps limité, celui de l’atelier.

Le jeu de donnée est préparé informatiquement, afin qu’on puisse lui appliquer l’algorithme de la régression linéaire multi-variable. On s’assure que les coefficients de l’équation linéaire soient positifs car ils représentent des prix moyens. Les composants à contribution nulle ont été enlevés et sont donc, d’après cette étude, jugés comme non-significatifs. Les composants restants sont d’après l’étude les composants significatifs dans l’établissement du prix.

## Résultats de la prédiction

Les coefficients de l’équation, représentant le prix « moyen » de chaque composant ou caractéristique, sont présentés dans le tableau suivant :

| Composants | Prix Moyen | Unité |
| ---------- | ---------- | ----- |
| Windows 10 Home |	69 |	€ |
| DDR4-SDRAM |	89 |	€ |
| Full HD	| 24 |	€ |
| QHD+	| 465 |	€ |
| Stockage Combiné HDD+SSD |	70 |	€ |
| Stockage de type SSD |	84 |	€ |
| Processeur de type N4200 |	97 |	€ |
| Processeur de type i5-7200U |	64 |	€ |
| Capacité totale de stockage |	0,13 |	€/Go |
| Capacité de la batterie |	1,8 |	€/Wh |
| Cache du processeur	| 51 |	€/Mo |
| Mémoire interne RAM |	36 |	€/Go |
| Quantité de ports de type A USB 3	| 56 | €/Port |
| Nombre maximum de voies PCI Express |	10 | €/Voie |
| Ecran tactile|	4 |	€ |
| Bus système |	2,4 |	€/Gts |

Le graphique suivant montre les prix estimés selon l’algorithme, pour les comparer avec les prix réels observés sur le site d’e-commerce. Les chiffres en abscisse correspondent au numéro d’identification des ordinateurs, classés par ordre de prix croissant.

https://github.com/JedhaBootcamp/Achetez-votre-ordinateur-avec-les-data-science/blob/master/graph.png

On observe ainsi que l’algorithme arrive à prédire le prix avec une très grande précision.

## Impact du modèle – L’offre est-elle une « bonne affaire » ?

Le modèle de prédiction permet ainsi d’obtenir des informations capitales dans le choix de l’ordinateur, au prix d’un effort très raisonnable. Le temps nécessaire peut être quasi-instantané si la base de données est déjà disponible et le code informatique correctement paramétré. Le modèle permet ainsi de savoir :

  * Quels sont les caractéristiques significatives dans l’établissement du prix de l’ordinateur ? Êtes-vous prêts à payer le prix moyen d’une caractéristique particulière ?

  * S’agit-il d’une bonne affaire ou non ? Le prix prédit représente un prix moyen calculé sur la base des caractéristiques de l’ordinateur. Si le prix réel est plus faible que le prix prédit, alors cela veut dire que l’offre est statistiquement une « bonne affaire » !


## Pistes d’amélioration du modèle

Les résultats présentés s’appuient sur un nombre très limité d’ordinateurs. La précision de prédiction d’estimation est jugée trop forte dans ce cas-là. Dans un second temps, il est ainsi possible de constituer une base de données plus conséquente et d’appliquer les mêmes algorithmes que ceux développés pour cet atelier. Les prix par composants et le modèle en général seront alors plus fiables.

Si vous êtes intéressé à l'idée d'apprendre les Data Sciences, regardez notre site : [Jedha.co](jedha.co)
