def email_domain():
    emails=[ "tarun@gmail.com","ganesh@yahoo.com","teja@gmail.com","naveen@company.com","pavan@yahoo.com","ravi@gmail.com"]
    domains=[]
    for email in emails:
        domain = email.split("@")[1]
        if domain not in domains:
            domains.append(domain)
    for domain in domains:
        count=0
        for email in emails:
            if email.split("@")[1]==domain:
                count+=1
        print(domain,":",count)
email_domain()