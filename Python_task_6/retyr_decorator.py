def retry(fun):
    def wrapper():
        count=5
        while count!=1:
            try:
                fun()
            except:
                count-=1
                # wrapper()
                print("Retrying ",count)
    return wrapper

@retry
def error():
    prinf("this is error")

error()