print("Language:")
language = str(input())

words = ()
with open(language + "_words.txt", "r", encoding="utf-8") as file:
    words = set(file.read().replace("\"", "").replace("\n", "").split(","))
        

with open(language + "_words.txt", "w", encoding="utf-8") as file:
    file.write(",".join([f'"{w.lower()}"' for w in words]))