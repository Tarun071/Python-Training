# ● Program to calculate Simple intrest
def simple_intrest():
    principle=int(input())
    time=int(input())
    rate=int(input())
    si=(principle*time*rate)/100
    print(f"Simple Intrest = {si}")
simple_intrest()