import csv


columns = ["GivenName","Gender","Title","Occupation","City"]

# 7
''' reader '''
# with open(r"C:\Users\User\OneDrive\Desktop\FILES\12 - sample_names.csv", 'r') as f:
#     lst_row = csv.reader(f)
#     for row in lst_row:
#         print(row)
#         print(f"my name is : {row[0]} , live at : {row[4]} , work at : {row[3]}")


# opt 2
# with open(r"C:\Users\User\OneDrive\Desktop\FILES\12 - sample_names.csv", 'r', encoding='utf-8-sig') as f:
#     dict_row = csv.DictReader(f)
#     print((dict_row))
#     for row in dict_row:
#         print(row)
#         print(f"my name is : {row['GivenName']} , live at : {row['City']} , work at : {row['Occupation']}")



# 8
''' writer '''
# with open(r"C:\Users\User\OneDrive\Desktop\FILES\12 - sample_names.csv", 'a') as f:
#     GivenName = input("enter name : ")
#     Gender = input("Male or female ? ")
#     Title = input("Mr. or Mrs.? ")
#     Occupation = input("whats your Occupation? ")
#     City = input("whats your city? ")
#
#     writer = csv.writer(f)
#     writer.writerow([GivenName, Gender, Title, Occupation, City])



# opt 2
try:
    with open(r"C:\Users\User\OneDrive\Desktop\FILES\12 - sample_names.csv", 'a') as f:
        GivenName = input("enter name : ")
        Gender = input("Male or female ? ")
        Title = input("Mr. or Mrs.? ")
        Occupation = input("whats your Occupation? ")
        City = input("whats your city? ")

        write= csv.DictWriter(f, fieldnames=columns)
        writer.writerow({columns[0]:GivenName, columns[1]:Gender, columns[2]:Title, columns[3]:Occupation, columns[4]:City})

except IOError as ex:
    print("Error performing I/O operations on the file: ", ex)


# 9
