full_name=input("Full Name: ")
email_id=input("Email Id: ")
mobile_no=input("Mobile No: ")
age=int(input("Age: "))
valid= True

if full_name[0]==' ' or  full_name[len(full_name)-1]==' ' or ' ' not in full_name :
    valid=False

if  email_id[0] == '@' or '@' not in email_id or '.' not in email_id :
    valid=False

if len(mobile_no)!=10 or mobile_no[0]=='0' or not mobile_no.isdigit():
    valid=False

if age<18 or age>60:
    valid=False

if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")