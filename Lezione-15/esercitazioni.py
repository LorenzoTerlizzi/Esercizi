def longest_palindrome(s: str) -> int:
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
        
    lenght_palindrome = 0
    odd_count = False

    for count in dict.values():
        if count % 2 == 0:
            lenght_palindrome += count
        else:
            lenght_palindrome += count - 1
            odd_count = True
        
    if odd_count:
        lenght_palindrome += 1
        
    return lenght_palindrome