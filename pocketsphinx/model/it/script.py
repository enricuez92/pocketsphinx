

with open("voxforge_it_sphinx.dic") as f:
    content = f.readlines()

for l in content:
	words=l.split(" ") 
	if words[0][-2:]=="ei":
		print words