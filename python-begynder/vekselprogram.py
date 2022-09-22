#crazy veksel program som skal skal omregne DKK til EUR og der skal pålægges kommission opp 2%, dog mindst 0,5 euro.

print("Hej, hvor mange DKK vil du veksle til EUR?") 

userinput = input()
DKK=float(userinput)

print("Du vil veksle, " + (userinput) + "DKK korrekt?") #spørg hvor meget kunden vil veksle

svar = input() #kundens svar til om antallet er korrekt?

euro = float("7.44") #fortæller programmer hvad en euro er værd.

if svar.lower() == "ja": #derefter fortæller programmet hvad kursen er på euro.
    print("Godt, kursen er på 7.44 DKK for 1 EUR, det svarer til at dine " + (userinput) + "DKK er:" )
else:
    print("Træls prøv igen.")
    
result = (DKK/euro) #jeg skal ændre euro til en float værdig
print(result)