text = input("ange en mening: ")
text = text.lower()
konsonanter = "bcdfghjklmnpqrstvwxz"
språk = ""
for i in range(0,len(text)):
    if text[i] in konsonanter:
        språk = språk+text[i]+"o"+text[i]
else:
    språk = språk+text[i]
print (språk)