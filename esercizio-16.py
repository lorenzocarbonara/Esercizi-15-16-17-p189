Lnazioni = ["Giappone", "Stati Uniti", "Italia", "Belgio", "Olanda", "Svezia", "Finlandia", "Norvegia", "Germania"]
Lcapitali = ["Tokyo", "Washington", "Roma", "Bruxelles", "Amsterdam", "Stoccolma", "Helsinki", "Oslo", "Berlino"]
dizionario = {}
for i in range (len(Lnazioni)):
    dizionario[Lnazioni[i]] = Lcapitali[i]
A = input("Che capitale di quale nazione vuoi sapere? ")
if A in Lnazioni:
    print("Ecco la capitale:", dizionario[A])
else:
     print("La nazione scelta non è contenuta nella lista, riprova") 