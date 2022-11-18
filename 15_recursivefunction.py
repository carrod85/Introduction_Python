#Pell number

def Pell(n):
   if n <= 1:
       return n
   else:
       return (2* Pell(n-1) + Pell(n-2))


nterms=13

#check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Pell numbers:")
   for i in range(nterms):
       print(Pell(i))