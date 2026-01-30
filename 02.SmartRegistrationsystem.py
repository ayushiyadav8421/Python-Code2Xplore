from curses.ascii import isdigit

student_id=input("Student ID: ")
email_id=input("Email ID: ")
password=input("Password: ")
ref_code=input("Referral Code: ")
valid=True
if not(student_id[0:3]=='CSE' and student_id[3]=='-' and student_id[4:].isdigit()):
    valid=False

if not((email_id[0]!='@' and email_id[len(email_id)-1]!='@' and '@' in email_id and '.' in email_id
        and email_id.endswith('.edu'))):
    valid=False

if not(len(password)>=8 and password[0]==password[0].upper() and  any('0' <= ch <= '9'for ch in password)):
    valid=False

if not (ref_code[0:3]=='REF' and ref_code[3:5].isdigit() and ref_code[len(ref_code)-1]=='@'):
    valid=False

if valid:
    print("Approved")
else:
    print("Rejected")

