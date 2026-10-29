# Oodatav väärtus ja tasuvus-p
# Õppenäide; hinnad ei ole turuandmed.
p=0.9;voit=10;kahju=120;kulu=2
E=p*voit-(1-p)*kahju-kulu
piir=(kahju+kulu)/(voit+kahju)
print("Oodatav tulemus:",round(E,2))
print("Tasuvuse võidumäär:",round(piir*100,2),"%")
