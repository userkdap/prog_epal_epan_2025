##ΕΠΑΝΑΛΗΠΤΙΚΕΣ ΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ
##HMEΡΗΣΙΩΝ ΚΑΙ ΕΣΠΕΡΙΝΩΝ ΕΠΑΓΓΕΛΜΑΤΙΚΩΝ ΛΥΚΕΙΩΝ
##ΤΡΙΤΗ 30 ΣΕΠΤΕΜΒΡΙΟΥ 2025
##ΕΞΕΤΑΖΟΜΕΝΟ ΜΑΘΗΜΑ:
##ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ ΥΠΟΛΟΓΙΣΤΩΝ
##
##ΘΕΜΑ Δ
##Σε έναν διαγωνισμό ρομποτικής συμμετέχουν πενήντα (50) ομάδες μαθητών
##από διάφορα σχολεία. Από κάθε σχολείο μπορούν να συμμετέχουν
##περισσότερες από μία ομάδες. Η βαθμολογία των ομάδων κυμαίνεται από 1
##έως και 100 ακέραιες μονάδες.
##Να αναπτύξετε πρόγραμμα σε γλώσσα προγραμματισμού Python, το οποίο:
##Δ1. Να διαβάζει το όνομα του σχολείου, το όνομα κάθε ομάδας και τη
##βαθμολογία της. Τα στοιχεία αυτά να καταχωρίζονται στις λίστες SXOLEIA,
##OMAD και BATH αντίστοιχα.
##Μονάδες 4
##Δ2. Να υπολογίζει και να εμφανίζει:
##α) Τον μέσο όρο βαθμολογίας όλων των ομάδων.
##β) Το πλήθος των ομάδων που συγκέντρωσαν βαθμολογία μεγαλύτερη ή ίση με
##50 μονάδες.
##Μονάδες 6
##Δ3. Να βρίσκει και να εμφανίζει τα ονόματα των ομάδων και των
##αντίστοιχων σχολείων με τη μεγαλύτερη βαθμολογία.
##Μονάδες 8
##Δ4. Να δημιουργεί και να εμφανίζει τη λίστα BESTSXOLEIA με τα ονόματα
##των σχολείων που έχουν ομάδες με βαθμολογία πάνω από 80 μονάδες. Το
##όνομα του σχολείου να καταχωρίζεται στη λίστα BESTSXOLEIA μία μόνο φορά.
##Μονάδες 7
##Σημείωση: Δεν απαιτούνται έλεγχοι ορθότητας δεδομένων.
##
OMADES = 50
PANW = 1
KATW = 100
BASI = 50
BEST_BATH = 80

OMAD = []
SXOLEIA = []
BATH = []
BESTSXOLEIA = []

synolo_bath = 0
panw_apo_basi = 0
max_bath = 0

try:
    print("Ανάγνωση του αρχείου εισόδου...\n")
    INPUTFILENAME="robotiki.txt"
    with open(INPUTFILENAME, 'r', encoding="utf-8") as inputfile:
        for omada in range(1, OMADES+1):
            onoma_omad = inputfile.readline().strip('\n').strip('\ufeff')
            print("Όνομα ομάδας {}: {}".format(omada, onoma_omad))
            OMAD.append(onoma_omad)
            onoma_sxol = inputfile.readline().strip('\n').strip('\ufeff')
            print("Σχολείο ομάδας {}: {}".format(omada, onoma_sxol))
            SXOLEIA.append(onoma_sxol)
            bathmologia = ""
            while not bathmologia.isdigit() \
              or int(bathmologia) not in range(PANW, KATW+1):
                bathmologia = inputfile.readline().strip('\n').strip('\ufeff')
                print("Βαθμολογία ομάδας {}: {}".format(omada, bathmologia))
            bathmologia = int(bathmologia)
            BATH.append(bathmologia)
            synolo_bath += bathmologia
            if bathmologia >= BASI:
                panw_apo_basi += 1
            if bathmologia > BEST_BATH and onoma_sxol not in BESTSXOLEIA:
                BESTSXOLEIA.append(onoma_sxol)
except Exception as err:
    print("Σφάλμα στην ανάγνωση του αρχείου εισόδου!", err)

print("Μέσος όρος βαθμολογίας όλων των ομάδων: {:.1f}".format(synolo_bath / OMADES))        
print("Πλήθος ομάδων που συγκέντρωσαν βαθμολογία μεγαλύτερη ή ίση με {} μονάδες: {}".format(BASI, panw_apo_basi))        

for i in range(OMADES-1): # range(0, OMADES–1, 1)
    for j in range(OMADES-1 , i , -1): # μέχρι και i–1
        if BATH[j] > BATH[j-1]:
            BATH[j], BATH[j-1] = BATH[j-1], BATH[j]
            OMAD[j], OMAD[j-1] = OMAD[j-1], OMAD[j]
            SXOLEIA[j], SXOLEIA[j-1] = SXOLEIA[j-1], SXOLEIA[j]

max_bath = BATH[0]
print("----------------------------------------------------------------------------------------")
print("Oνόματα των ομάδων και των αντίστοιχων σχολείων με τη μεγαλύτερη βαθμολογία ({} μονάδες)".format(max_bath))
print("----------------------------------------------------------------------------------------")
i = 0
while i < OMADES and BATH[i] == max_bath:
    print("{}\t{}".format(OMAD[i], SXOLEIA[i]))
    i += 1

print("---------------------------------------------------------------------------------")
print("Oνόματα των σχολείων που έχουν ομάδες με βαθμολογία πάνω από ογδόντα (80) μονάδες")
print("---------------------------------------------------------------------------------")
for i in range(len(BESTSXOLEIA)):
    print(BESTSXOLEIA[i])
