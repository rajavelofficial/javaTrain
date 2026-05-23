# blood_donation.py

donor = input("Enter donor name: ")

blood_group = input("Enter blood group: ")

age = int(input("Enter donor age: "))

units = int(input("Enter blood units donated: "))

print("Donor Name:", donor)
print("Blood Group:", blood_group)

print("Donor Age:", age)
print("Blood Units:", units)

if age >= 18:
    print("Eligible for Donation")
else:
    print("Not Eligible for Donation")

hospital = input("Enter hospital name: ")

print("Hospital Name:", hospital)

for i in range(3):
    print("Donation Record Updated")

print("Blood Donation System")
print("Thank You")