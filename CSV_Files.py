import csv

# 7
with open(r"C:\Users\User\OneDrive\Desktop\FILES\12 - sample_names.csv", 'r') as f:
    lst_row = csv.reader(f)
    for row in lst_row:
        # lst_row = cs.reader()
        print(f"my name is : {row[0]} , live at : {row[4]} , work at : {row[3]}")



# 8
with open(r"C:\Users\User\OneDrive\Desktop\FILES\12 - sample_names.csv", 'a') as f:
    GivenName = input("enter name : ")
    Gender = input("Male or female ? ")
    Title = input("Mr. or Mrs.? ")
    Occupation = input("whats your Occupation? ")
    City = input("whats your city? ")

    writer = csv.writer(f)
    writer.writerow((GivenName, Gender, Title, Occupation, City))

# 9
