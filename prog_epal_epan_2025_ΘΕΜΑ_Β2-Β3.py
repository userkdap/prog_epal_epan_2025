##ΕΠΑΝΑΛΗΠΤΙΚΕΣ ΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ
##HMEΡΗΣΙΩΝ ΚΑΙ ΕΣΠΕΡΙΝΩΝ ΕΠΑΓΓΕΛΜΑΤΙΚΩΝ ΛΥΚΕΙΩΝ
##ΤΡΙΤΗ 30 ΣΕΠΤΕΜΒΡΙΟΥ 2025
##ΕΞΕΤΑΖΟΜΕΝΟ ΜΑΘΗΜΑ:
##ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ ΥΠΟΛΟΓΙΣΤΩΝ
##
##ΘΕΜΑ B
##B2. Να μεταφέρετε στο τετράδιό σας τον παρακάτω πίνακα και να
##συμπληρώσετε για την κάθε γραμμή το αποτέλεσμα της λογικής έκφρασης αν
##A = True, B = False και C = True.
##Λογική Έκφραση            Αποτέλεσμα
##α. A and (not B)
##β. A and B and C
##γ. (not A) or B
##δ. (not C) and (not B)
##ε. (A or B) and C
##στ. not A and B or C
##Μονάδες 12
##
A = True
B = False
C = True
print("A =", A)
print("B =", B)
print("C =", C)
print("A and (not B):", A and (not B)) ## True
print("A and B and C:", A and B and C) ## False
print("(not A) or B:", (not A) or B) ## False
print("(not C) and (not B):", (not C) and (not B)) ## False
print("(A or B) and C:", (A or B) and C) ## True
print("not A and B or C:", not A and B or C) ## True
##
##A = True
##B = False
##C = True
##A and (not B): True
##A and B and C: False
##(not A) or B: False
##(not C) and (not B): False
##(A or B) and C: True
##not A and B or C: True
##
##Λογική Έκφραση            Αποτέλεσμα
##α. A and (not B)          True
##β. A and B and C          False
##γ. (not A) or B           False
##δ. (not C) and (not B)    False
##ε. (A or B) and C         True
##στ. not A and B or C      True
##
##B3. Να γράψετε στο τετράδιό σας το παρακάτω τμήμα προγράμματος,
##χρησιμοποιώντας την εντολή επανάληψης for αντί της εντολής επανάληψης while
##έτσι, ώστε να εμφανίζεται το ίδιο αποτέλεσμα.
##i = 10
##while i >= 0:
##    i-= 2
##    print i
##Μονάδες 5
##
i = 10
while i >= 0:
    i-= 2
    print(i)
for i in range(8, -3, -2):
    print(i)
for i in range(8, -4, -2):
    print(i)
##
##8
##6
##4
##2
##0
##-2
##8
##6
##4
##2
##0
##-2
##8
##6
##4
##2
##0
##-2
