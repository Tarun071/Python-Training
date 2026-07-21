def invoice_generator():
    invoice_number=input().strip().upper()
    final_invoice=invoice_number.replace(" ","-")
    print(final_invoice)
invoice_generator()