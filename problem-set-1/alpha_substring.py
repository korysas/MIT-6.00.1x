def main():
    s = 'azcbobobegghakl'

    result = alpha_subs(s)

    print(result)

def alpha_subs(s):
    s = s.lower()

    i = 0
    start = 0
    end = 0
    is_alphabetical = False
    max_alpha_length = 0
    max_alpha_indexes = [0, 0]
    while i < len(s) - 2:
        left = s[i]
        right = s[i + 1]

        if left <= right and not is_alphabetical:
            is_alphabetical = True
            start = i
        if left > right and is_alphabetical:
            is_alphabetical = False
            end = i
            current_alpha_length = end - start + 1
            if current_alpha_length > max_alpha_length:
                max_alpha_length = current_alpha_length
                max_alpha_indexes = [start, end]

        i += 1

    return s[max_alpha_indexes[0]: max_alpha_indexes[1] + 1]

if __name__ == '__main__':
    main()
