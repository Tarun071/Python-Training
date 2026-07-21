def product_code_generator():
    p_name=input().upper()
    p_brand=input().upper()
    p_id=input()

    code=p_name[0:3]+p_brand[0:2]+p_id[-3:-1]
    print(code)
product_code_generator()