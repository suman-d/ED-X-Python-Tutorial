s = 'azcbobobegghakl'

longest_substring_count = 0
longest_substring = s[0]

for i in range(len(s) - 1):
    temp_str = s[i]
    count = 0
    for j in range(i, len(s) - 1):
        if s[j] <= s[j + 1]:
            count = count + 1
            temp_str = temp_str + s[j + 1]
            if longest_substring_count < count:
                longest_substring_count = count
                longest_substring = temp_str
        else:
            break

print("Longest substring in alphabetical order is: %s" % longest_substring)