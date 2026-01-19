def palindrome(string):
    left = 0
    right = len(string) -1
    while right >= left:
        if string[left] != string[right]:
            return False
        left = left +1
        right = right-1
    return True
word=input("Enter a word:")
print("Is this a palimdrome?", palindrome(word))
