https://github.com/sidabdullah07/Python-Programs
print("UIN : 251A010", "DATE : 09-02-2026")
try:
    n1 = int(input("ENTER FIRST VALUE : "))
    n2 = int(input("ENTER SECOND VALUE : "))
    d = n1/n2
except ZeroDivisionError:
    print("NUMBER CANNOT BE DIVIDED BY ZERO")
except ValueError:
    print("INVALID INPUT")
else:
    print("DIVICION : ",d)
finally:
    print("THANK YOU......")

