text = input("text: ")
letters = 0
words = 1
sentences = 0
for i in text:
    if (i.isalpha()):
        letters += 1
    elif (i == " "):
        words += 1
    elif (i == "." or i == "?" or i == "!"):
        sentences += 1
Le = (letters / words) * 100
Se = (sentences / words) * 100
index = 0.0588 * Le - 0.296 * Se - 15.8
index = round(index)
if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")


for i in range(3):
    i == 4
    break
else:
    