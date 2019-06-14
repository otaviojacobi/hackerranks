def matchingStrings(strings, queries):
    string_table = {}
    for string in strings:
        if string in string_table.keys():
            string_table[string] += 1
        else:
            string_table[string] = 1
    
    ans = []
    for query in queries:
        if query in string_table.keys():
            ans.append(string_table[query])
        else:
            ans.append(0)

    return ans