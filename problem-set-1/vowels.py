"""program that counts the number of vowels in a string"""

def main():
    res1 = vowels_in_string('azcbobobegghakl')
    print_result(res1)

    res2 = vowels_in_string('hello')
    print_result(res2)

    res3 = vowels_in_string('HELLO')
    print_result(res3)

def vowels_in_string(string):
    """accepts a string and returns the number of vowels in the string"""
    count = 0
    string = string.lower()
    for c in string:
        if c is 'a' or c is 'e' or c is 'i' or c is 'o' or c is 'u':
            count += 1

    return count

def print_result(no_vowels):
    print("Number of vowels: {0}".format(no_vowels))

if __name__ == '__main__':
    main()
