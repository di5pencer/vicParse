#load all the things.
import os
import json

#oh hai JSON
json = json.loads(open('Example.json').read())
value = json['value']

#Make a variable
line = 0
#make a list
hash = []
#count some lines.
length = len(value)


for x in value:
    line = line + 1
    #Print output
    print(json['value'][line]['MD5'])
    hash.append(json['value'][line]['MD5'])
    if line >= (length - 1):
        break

print("\n")
print(str(line) + " lines have been added to the list.")
print("Commence writing text file now")

## Le debug
##print(hash)

outF = open("Hash.txt", "w")
for z in hash:
  # write line by line to output file
  outF.write(z)
  outF.write("\n")
outF.close()

print("\nWriting text file complete\n")
