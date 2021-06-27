import re

line = "The ghost that says boo haunts the loo"
found = re.findall(".oo", line)
print(found)