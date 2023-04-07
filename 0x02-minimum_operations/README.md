                                         Minimum Operations Algorithm in Python

Minimum Operations algorithm is used to ascertain  the least number of operations needed to convert a string into another.
operation in this case can take a CRUD functionality that involve creating a new character to the string, updating a character
from the string or deleting a character from the string.

example:
Given two strings
str1, str2 = 'python', 'power'
in other to convert str1 to str2 first
1. we would need to determine the length of both strings
2. then we calculate the factor of the length of the strings
3. we loop through each factor and create a new string by repeating the original string Str1 a certain number of times based on the factor
4. we count the number of unique strings in the new string. We can use this information to determine how many swaps and replacements are
needed to transform this new string into the desired string str1.
5. we track the minimum number os operation needed to swap each strings into the newly modified string, which gives us the minimum operation needed
to swap str1 to str2.

```def minimum_opp(str1, str2):
        len_of str_1 = len(str1)
        len_of_str_2 = len(str2)
        temp_storage = [[0 for _ in range(len_of_str_1 + 1)] for _ in range(len_of_str_2 + 1)]
        for i in range(len_of_str_1 + 1):
            for j in range(len_of_str_2 + 1):
                if i == 0:
                    temp_storage[i][j] = j
                elif j == 0:
                    temp_storage[i][j] = i
                elif str1[i-1] == str2[j-1]:
                    temp_storage[i][j] = temp_storage[i - 1][j - 1]
                else:
                    temp_storage[i][j] = 1 + min(temp_storage[i][j - 1], temp_storage[i-1][j], temp_storage[i-1][j-1]
        return temp_storage[len_of_str_1][len_of_str_2]```
