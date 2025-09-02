runes = list(input("Enter the runes"))
s = set(runes)
print(s)
count = 0

for el in s:
    if(el == 'l'):
        count = count + 1
    elif(el == 'u'):
        count = count + 1
    elif(el == 'm'):
        count = count + 1
    elif(el == 'o'):
        count = count + 1
    elif(el == 's'):
        count = count + 1
        
        
if(count == 5):
    print("LUMOS")
else:
    print(-1)