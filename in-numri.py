import time
import random

print("Ħelow. Jiena Ġianni. I'll help you in learning Maltese.")
isem = input("Inti x'jismek? ").capitalize()
print(f"Ħelow, {isem}!")
time.sleep(3)


print("\nLet's start learning numbers 1-10!")


numri1_10 = {
    1: "wieħed",
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

for numri, kelma in numri1_10.items():
    print(f"{numri} - {kelma}")

print("\nProsit! You know the numbers 1-10. Now, let's practice them.")

time.sleep(1)
print("\nWrite the Maltese word for each number (1-10).")

for numri, kelma in numri1_10.items():
    risposta = input(f"What is {numri} in Maltese? ").strip().lower()
    if risposta == kelma:
        print(f"Tajjeb! {kelma.capitalize()} means {numri}.")
    else:
        print(f"Le, mhux hekk. In Maltese {numri} is '{kelma}'.")
    time.sleep(0.5)

print("\nProsit! You finished the writing practice!")

print("Now it's time for the quiz!")

def countdown(start):
    for i in range(start, -1, -1):
        print(f"{i}...")
        time.sleep(1)

countdown(5)

def run_quiz(numri_dict):
    numri_quiz = list(numri_dict.items())
    random.shuffle(numri_quiz)
    score = 0

    for numri, kelma in numri_quiz:
        risposta = input(f"What is {numri} in Maltese? ").strip().lower()
        if risposta == kelma:
            print(f"Tajjeb! {kelma.capitalize()} is {numri}.")
            score += 1
        else:
            print(f"Le, mhux hekk. In Maltese {numri}  is '{kelma}'.")
        time.sleep(0.5)

    print(f"\nProsit! You got {score} out of {len(numri_dict)} correct.")

    if score == 10:
        print(f"Are you a genius, {isem.capitalize()}?")
    elif score >= 7:
        print(f"Tajjeb ħafna, {isem.capitalize()}!")
    else:
        print(f"You're almost there, {isem}.")
        for numri, kelma in numri_dict.items():
            print(f"{numri} - {kelma}")
            time.sleep(0.5)
        time.sleep(3)

        play_again = input("\nWould you like to play the quiz again? (yes/no): ").strip().lower()
        if play_again in ["yes", "y", "iva"]:
            run_quiz(numri_dict)
        else:
            print("Ok, take a break!")

run_quiz(numri1_10)

time.sleep(10)


numri11_20 = {
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

print("\nLet's learn numbers 11-20!")


for numri, kelma in numri11_20.items():
    print(f"{numri} - {kelma}")

print("Prosit! You know the numbers 11-20. Now, let's practice them.")

time.sleep(1)
print("\nWrite the Maltese word for each number (11-20).")

for numri, kelma in numri11_20.items():
    risposta = input(f"What is {numri} in Maltese? ").strip().lower()
    if risposta == kelma:
        print(f"Tajjeb! {kelma.capitalize()} means {numri}.")
    else:
        print(f"Le, mhux hekk. In Maltese {numri} is '{kelma}'.")
    time.sleep(0.5)

print("\nProsit! You finished the writing practice!")

print("\nNow it's time for the quiz!")

countdown(5)

run_quiz(numri11_20)

print("\nYou did well. Great job! Take a rest.")

time.sleep(3)

print("The program will exit in 10 seconds.")

countdown(10)

print("Saħħa!")

exit()