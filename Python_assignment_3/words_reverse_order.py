def reverse_words():
    s = input("Enter a string: ")
    words = s.split()
    for i in range(len(words) - 1, -1, -1):
        print(words[i], end=" ")
reverse_words()