def check_palindrome(chars):

    word = "".join(chars)

    # Two base cases combined into one:
    if len(word) == 0 or len(word) == 1:
        return "is a palindrome"

    if word[0] != word[-1]:
        return "is not a palindrome"

    # The ends match. Remove them and check the remainder.
    next_text = word[1:-1]
    return check_palindrome(next_text)


print(check_palindrome(['r','e','d','d','e','r']))
