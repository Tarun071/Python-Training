def good_customer_feedback():
    good_feedback=['good' ,'excellent', 'awesome' ,'great']
    customer=input().split()
    print(customer)
    for i in customer:
        if i in good_feedback:
            print("Positive")
            
    
good_customer_feedback()