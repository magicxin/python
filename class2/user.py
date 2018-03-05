dictionary = {'color':'green','name':'magic'}
print(dictionary.items())
for key,value in dictionary.items():
    print("\nkey:"+key)
    print("\nvalue:"+value)

for keyname in dictionary.keys():
    print(keyname)

for value in dictionary.values():
    print(value)