date=str(input("輸入月 /日:")).split()
date=int(date[0])*30+int(date[1])
if 51<=date<=78:
    print("Aqarius")
elif 79<=date<=110:
    print("Pisces")
elif 111<=date<=140:
    print("Aries")
elif 141<=date<=171:
    print("Tauus")
elif 172<=date<=201:
    print("Gemini")
elif 202<=date<=232:
    print("Cancer")
elif 233<=date<=263:
    print("Leo")
elif 264<=date<=293:
    print("Aries")
elif 294<=date<=323:
    print("Libra")
elif 324<=date<=352:
    print("Scorpio")
elif 353<=date<=381:
    print("Sagittarius")
else:
    print("Capricorn")
    

