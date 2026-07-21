# PDF, Word, Excel, or Image file based on its extension.

def extension_finder():
    file=input().split(".")
    if file[1]=="pdf":
        print("It is an PDF file")
    elif file[1]=="xls":
        print("It is an Excel file")
    elif file[1]=="jpg" or file[1]=="png":
        print("It is an photo")
    else:
        print("Extension not available")
extension_finder()