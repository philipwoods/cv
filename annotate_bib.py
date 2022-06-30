import os

with open("Exported Items.bib", 'r') as f:
	bib_in = f.readlines()
with open("mypubs.bib", 'w') as f:
	for line in bib_in:
		f.write(line)
		if "author = " in line:
			authors = line.split(' and ')
			index = 1
			for i,author in enumerate(authors):
				if "Woods, P" in author: index += i
			annotation = "	Author+an = {" + str(index) + "=highlight},"
			print(annotation, file=f)
os.remove("Exported Items.bib")