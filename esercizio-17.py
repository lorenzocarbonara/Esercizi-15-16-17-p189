Lnazioni = ["Giappone", "Stati Uniti", "Italia", "Belgio", "Olanda", "Svezia", "Finlandia", "Norvegia", "Germania"]
Lcapitali = ["Tokyo", "Washington", "Roma", "Bruxelles", "Amsterdam", "Stoccolma", "Helsinki", "Oslo", "Berlino"]
dizionario = {}
for i in range (len(Lcapitali)):
    dizionario[Lcapitali[i]] = Lnazioni[i]
A = input("Inserici la capitale della nazione che vuoi trovare: ")
if A in Lcapitali:
    print("Ecco la nazione:", dizionario[A])
else:
     print("La capitale scelta non è contenuta nella lista, riprova") 