def email_generator():
    full_name=input().lower().strip()
    dep=input().lower()
    mail_name=full_name.replace(" ",".")
    email=mail_name+"."+dep+"@miracle.com"
    print(email)
email_generator()