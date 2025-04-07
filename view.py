#!/home/sparrow/Firmware_Slap/fwslap/bin/python

import pickle
from firmware_slap.function_handler import print_function
pickle_name = "Vulnerable_Pickle"
with open(pickle_name, 'rb') as f:
    results = pickle.load(f)
for result in results:
    print_function(result)
