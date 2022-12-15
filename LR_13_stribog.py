from pygost.gost34112012 import GOST34112012

# make a hash object with the default parameters
h = GOST34112012()
# update the hash object with the data
h.update(b'Hello, world!')
# get the digest
print(h.hexdigest())

# see the gost34.11-2012.py full source code
