# GENOMEC
## <i>A Novel Bioinformatics Tool for Analyzing Genomic Features in NGS Data</i>

## Abstract
By changing a gene's instructions for making a protein, gene mutations can often cause protein malfunction, thereby preventing the associated cells from working properly, and this leads to  human disease or abnormal expression of these genes in the body. These expressed genes are located in the protein-coding regions of the genome.
<br>
Leveraging on Next Generation Sequencing (NGS) datasets allows us the possibility to analyze genomic features (i.e. genes, exons, viruses, phages, microbes, bacteria e.t.c) which are abundant in human samples. Some of these features are organisms like viruses, phages or microbes which invade living, normal cells and use those cells to multiply and produce other organisms like themselves, thereby damaging, killing, attacking certain cells in the body such as the liver, respiratory system, brain, blood or simply changing the cells and leading to sickness.
<br><br>

## Introduction


## Methods
Given some NGS datasets of some organism e.g bacteria causing a specific human disease, deciding on which genes or genomic features should be investigated in the disease requires some selection metric. In order to answer this question, in this study, we have developed a novel bioinformatics tool which uses bedgraphs generated from Sequence Alignment Maps for the analysis of genomic features in human disease samples. A use-case for this study is the analysis of phages in Salmonella Typhi samples.
<br><br>
We developed a bioinformatics tool for the statistical analysis of genomic features across regions of interest in human disease samples using public datasets by computing the number of blocks (exons) in each targeted region or Browser Extensible Data (BED) line in the sample.

<br><br>
## Results
The following accession numbers show the result from analyzing 911 S. Typhi samples. The number before comma is the frequency of occurence for each phage:
<br>
NC_028699.1:	910,
NC_019488.1:	909,
NC_010393.1:	909,
NC_010463.1:	909,
NC_019545.1:	905,
NC_018279.1:	894,
NC_010392.1:	891,
NC_004348.1:	866,
NC_017985.1:	860,
NC_002371.2:	828,
NC_014900.1:	822,
NC_031946.1:	812,
NC_030919.1:	808,
NC_011802.1:	804,
NC_005841.1:	771,
NC_018275.1:	764,
NC_010391.1:	751,
NC_004313.1:	681,
NC_005340.1:	581,
NC_011976.1:	567,
NC_016761.1:	540,
NC_031129.1:	504,
NC_021774.1:	494,
NC_013059.1:	401

<br><br>
Of all the 153 phages analyzed, each sample has different significant phages. We want to compare all samples and find out if there are specific phages that occur in all samples or most of them, and what is the corresponding coverage for each phage in these samples. We are already printing the above summary.

<br><br>
## Conclusion
Our goal is to compare all samples and find out which of the high-coverage phages or genomic features are the most frequent. We will then recommend the most common phages or genomic features to investigators for further study.

