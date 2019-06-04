## Genomec is Python v2 and v3 compatible 
import glob
import errno
sample_type = "Typhi/Paratyphi"
genome_type = "Phages" ##Specify Genome of Interest (Genes, Viruses, Phages, Microbes, Bacteria... )
filetype = ".bedgraph"
path = "bedgraphs/*"+filetype
bin_threshold = 3
sig_threshold = 50
files = glob.glob(path)
for file in files:
	print('-'*50)#just a line to distinguish between all the outputs
	if file.endswith( filetype ):
		print(file)
		print('*'*len(file))#do some underlining here
		try:
			with open( file ,"r") as text_file:
				lines = text_file.readlines()
				mydictl = {}
				mydictg = {}
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
				print("GeneOfStudy" + "\tIns" + "\tSig" "\tCoverage")
				objcount = 0
				mysig = {} ## dictionary
				for myobj in mydictl:
					objcount += 1
					lt3 = mydictl[myobj]
					gt3 = mydictg[myobj]
					coverage = round(100*(gt3 * 1.0)/(gt3+lt3))
					print(myobj +"\t" + str(lt3) + "\t" + str(gt3) + "\t" + str(coverage) + "%")
					if coverage >= sig_threshold:
						mysig[myobj] = coverage ## Using a dictionary
				print("\nGene Count: " + str(objcount))
				print("Here are the " + str(len(mysig)) + " significant " + genome_type + " and corresponding coverage in this " + sample_type + " sample.")
				print(mysig) #dictionary
				print("There are " + str(total_lines) + " targeted regions of interest in this sample.")
				print("")
		except IOError as exc:
			if exc.errno != errno.EISDIR:
				raise

