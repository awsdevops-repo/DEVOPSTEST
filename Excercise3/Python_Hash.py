'''
Challenge #3
We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you.
Example Inputs
object = {“a”:{“b”:{“c”:”d”}}}
key = a/b/c

'''

def nested_dictonary(hashname, keys):
    for key in keys:
        hashname = hashname[key]
    return hashname

hashname = {'a': {'b': {'c': 'd'}}}
keystring = "a/b/c"
hashkeys = keystring.split("/")
hashvalue = nested_dictonary(hashname,hashkeys)

print(hashvalue)
