a = int(input("Yosh kiriting: "))
narx = 100000 

if 0<a<7 :
    print(f"Yakuniy narx {(narx*50)/100} (50% chegirma qo'llanildi)")

elif 7<a<18:
    print(f"Yakuniy narx {(narx*20)/100} (20% chegirma qo'llanildi)")

elif a>60:
    print(f"Yakuniy narx {(narx*30)/100} (30% chegirma qo'llanildi")

else:
    print("Chegirma yo'q")
