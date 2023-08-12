print("****************GRADE CALCULATOR****************")
N=int(input("KI KANTITE NOT OU VLE SEZI?:"))

print(f"OU CHWAZI RANTRE" ,N,"NOT SELMAN")
liste_notes = []

moyenne=0.00
notes=0



for i in range (N) :
    if i>=0:
         
        notes=int(input("RANTRE YON NOT:"))
        liste_notes.append(notes)
    continue

somme = sum(liste_notes)
moyenne=round(somme/N,2)

print("Mwayenn lan se:", moyenne)


if (moyenne>=90):
    print("A")
elif(moyenne >= 80 and moyenne <90):
    print("B")
elif(moyenne >= 70 and moyenne <80):
    print("C")
elif(moyenne >= 60 and moyenne < 70):
    print ("D")
elif (moyenne < 60):
    print("F")
else:
    print(" ")

print("MEN REZILTA W TAP TANN LAN:\n", "Mwayèn lan se:", moyenne, "\n Klasifikasyon an se:")

       
        

       
        
    
   

    
