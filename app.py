string = input("Inserisci una stringa: ")
string += "$"
print(string)

for i in range (len(string)):
    rotazioni = testo[i:] + testo[:i]

n = len(string)
temp = ""
for i in range(n):
    for j in range(0, n-i-1):
        if(string[j] > string[j+1]):
            temp = string[j]
            string[j] = string[j+1]
            string[j+1] = temp




