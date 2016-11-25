print('Single quoted string with double quote - "')
print("Double quoted string with single quote - '")
print('''Multi line comment
whitespace is preserved''')

print('Escape sequences : new line in \\n - \n Backslash is \\\\ - \\ \n Single quote is \\\' - \' \n Double quote is \\\" - \"')

print('len(\'String\') is ',len('string'))

slice_example='string contents'
print(slice_example[3:12])
print(slice_example[:10])
print(slice_example[4:])

print('Convert other datatypes to a string using str(). str(100) is 100 and type is ', type(str(100)))
