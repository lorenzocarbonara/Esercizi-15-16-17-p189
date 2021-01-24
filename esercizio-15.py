Lnazioni = ["Giappone", "Stati Uniti", "Italia", "Belgio", "Olanda", "Svezia", "Finlandia", "Norvegia", "Germania"]
Lcapitali = ["Tokyo", "Washington", "Roma", "Bruxelles", "Amsterdam", "Stoccolma", "Helsinki", "Oslo", "Berlino"]
A = input("Che capitale di quale nazione vuoi sapere? ")
if A in Lnazioni:
    B = Lnazioni.index(A)
    print("Ecco la capitale:", (Lcapitali[B]))
else:
    print("La nazione scelta non è contenuta nella lista, riprova inserendo un'altra nazione.")