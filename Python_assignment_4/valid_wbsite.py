def validate_url():
    url = input("Enter URL: ")
    if url[:7] == "http://" or url[:8] == "https://":
        print("Valid Website URL")
    else:
        print("Invalid Website URL")
validate_url()