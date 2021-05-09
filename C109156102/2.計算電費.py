#他是累計電費
summer=0
nosummer=0

much=int(input("輸入度數:"))

if much <=120:
    summer=much*2.1
    nosummer=much*2.1
elif 121<= much <=330:
    summer=(much-120)*3.02 + 252
    nosummer=(much-120)*2.68 + 252
elif 331<= much <=500:
    summer=(much-330)*4.39 + 886.2
    nosummer=(much-330)*3.61 +814.8
elif 501<= much <=700:
    summer=(much-500)*4.97 + 1632.5
    nosummer=(much-500)*4.01 +1428.5
else:
    summer=(much-700)*5.63 + 2626.5
    nosummer=(much-700)*4.50 +2230.5

print(round(summer,2))
print(round(nosummer,2))
