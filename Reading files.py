
#r - read w -write a - append info r+ - read and write
employee_file = open("reading_files_employes.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()