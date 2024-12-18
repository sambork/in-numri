import time #will be used later for pausing the code

print("Dzień dobry! Jestem twoim pomocnikiem w nauce maltańskiego. Mów mi Ġianni!") #prints in Polish "Hello! I'm your helper in learning Maltese. Call me Gianni"
\
twoje_imię = input("Jak masz na imię? ") #asks the user to input their name
print(f"Dzień dobry, {twoje_imię}!") #greets the user
print("Zacznijmy naukę liczb w języku maltańskim. Na początek liczby 1-10.") #prints "Let's start learning numbers in Maltese. In the beginning numbers 1-10."
\
liczby_do10 = {
1: "wieħed (m) lub waħda (ż)",
2: "tnejn",
3: "tlieta",
4: "erbgħa",
5: "ħamsa",
6: "sitta",
7: "sebgħa",
8: "tmienja",
9: "disgħa",
10: "għaxra"
}
print(liczby_do10) #prints all the list above
\
listan = input("A może wolisz zobaczyć listę numerowaną? ").lower() #ask for decision if the user wants to see a numbered list; user's input is converted to lower case.

if listan == "nie": #if equal to "no", prints "Ok. Have a nice lesson!"
    print("Ok. Miłej nauki!"),
elif listan == "tak": #if equal to "yes" prints the numbered list (items)
    for key, value in liczby_do10.items():
        print(key, value),
else: #if anything else than "no" or "yes" is written, comments that the user is not in the mood for learning and says bye.
    print("Ġianni: " + listan + "?" + " " + "Chyba nie jesteś w nastroju do nauki liczb 1-10. Pa!")

liczby11_20 = {
11: "ħdax",
12: "tnax",
13: "tlettax",
14: "erbatax",
15: "ħmistax",
16: "sittax",
17: "sbatax",
18: "tmintax",
19: "dsatax",
20: "għoxrin"
}

time.sleep(15) #waits (sleeps) for 15 seconds before executing the next lines

print("Ġianni: " + twoje_imię +", a może chcesz się pouczyć liczb 11-20 po maltańsku?") #asks user if they want to learn numbers 11-20 
liczby_do20 = input("Wyświetlić liczby 11-20? ").lower() #asks for no/yes/other input from the user; input will be converted to lowercase
if liczby_do20 == "nie": #no for learning numbers 11-20
    print("Ok. Rozumiem, że chcesz dłużej pouczyć się liczb 1-10.") 
    \
    print(liczby_do10) #after user didn't want to learn numbers 11-20, shows numbers 1-10 again
elif liczby_do20 == "tak":
    print(liczby11_20)
    listan = input("A może wolisz zobaczyć listę numerowaną? ").lower() #if yes, asks if the user wants to see the numbered list 
    if listan == "nie": #no for the numbered list
        print("Ok. Miłej nauki!"),
    elif listan == "tak": #user wished to see the numbered list of 11-20
        for key, value in liczby11_20.items():
            print(key, value),
    else:
        print("Ġianni: " + listan + "?" + " " + "Chyba nie masz motywacji do nauki. Odpocznij chwilę. Pa!")
else: #if the user will provide any other answer other than "no" or "yes" to the question if they want to learn numbers 11-20, as in earlier case, the program will say bye.  
    print("Ġianni: " + listan + "?" + " " + "Chyba nie jesteś w nastroju do nauki liczb 11-20. Zrób sobie przerwę! Pa!") 

time.sleep(300)