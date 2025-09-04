a = input("Fayl kiriting: ")

b = a.endswith('.pdf')
c= a.endswith('.docx')
d=a.endswith('.txt')

if b:
   print(f"Fayl turi pdf")
elif c:
     print(f"Fayl turi docx")
elif d:
     print(f"Fayl turi txt")
else:
    print(False)
    