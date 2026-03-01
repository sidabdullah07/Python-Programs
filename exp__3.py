https://github.com/sidabdullah07/Python-Programs
print("UIN : 251A010", "DATE : 27-01-2026")
basic_salary = int(input("ENTER THE BASIC SALARY: "))
DA = basic_salary*0.70
TA = basic_salary*0.30
HRA = basic_salary*0.10
gross_salary = basic_salary + DA + TA + HRA
print("***** Salary Details *****")
print(f"DEARNESS ALLOWANCE IS {DA} ")
print(f"TRAVEL ALLOWANCE IS {TA} ")
print(f"HOUSE RENT ALLOWANCE {HRA} ")
print(f"GROSS SALARY IS : {gross_salary} ")


