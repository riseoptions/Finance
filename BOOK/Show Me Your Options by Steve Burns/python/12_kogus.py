# Riskieelarve ja täisarvuline kogus
# Õppenäide; hinnad ei ole turuandmed.
from math import floor
konto=25000;riskiosa=0.02;max_kahju=150;kulureserv=10
eelarve=konto*riskiosa
n=floor(eelarve/(max_kahju+kulureserv))
print("Lepinguid:",n,"; eelarve:",eelarve,"; kogurisk:",n*(max_kahju+kulureserv))
