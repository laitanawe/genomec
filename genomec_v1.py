text_file = open("typhi.DRR070980.bedgraph", "r")
lines = text_file.readlines()
mydictl = {}
mydictg = {}
bin_threshold = 3
sig_threshold = 50
total_lines = 0
for line in lines:
	total_lines += 1
	line = line.split("\t")
	objname = line[0]
	if objname not in mydictl:
		mydictl[objname] = 0
	if objname not in mydictg:
		mydictg[objname] = 0
	integer_val = int(line[3])	
	if (integer_val < bin_threshold):
		mydictl[objname] += 1
	if (integer_val > bin_threshold):
		mydictg[objname] += 1

print("Gene," + "Ins," + "Sig," "Cover")
objcount = 0
mysig = {} ## dictionary
#mysig = []
for myobj in mydictl:
	objcount += 1
	lt3 = mydictl[myobj]
	gt3 = mydictg[myobj]
	coverage = round(100*(gt3 * 1.0)/(gt3+lt3))
	print(myobj, str(lt3), str(gt3), str(coverage) + "%")
	if coverage >= sig_threshold:
#	 mysig.append(myobj)

	 mysig[myobj] = coverage ## Using a dictionary

print("\nGene Count: " + str(objcount))
print("Here are the " + str(len(mysig)) + " significant phages and corresponding coverage in this sample.")
print(mysig) #dictionary
print("There are " + str(total_lines) + " lines in this file.")
