"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s
For example, if s = 'azcbobobegghakl', then your program should print
"""

def main():
    string = 'azcbobobegghakl'

    count = occurrences(string, 'bob')

    print(count)

def occurrences(s, pattern):
    count = 0

    for i in range(len(s) - len(pattern) + 1):
        if s[i:(i + len(pattern))] == pattern:
            count += 1

    return count

if __name__ == '__main__':
    main()
