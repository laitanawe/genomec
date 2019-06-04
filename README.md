# GENOMEC
## <i>A Novel Bioinformatics Tool for Analyzing Genomic Features in NGS Data</i>
## Abstract

Human diseases are abnormal expression of particular genes in the body. In the neuroscience space, external factors like age might increase the risk for a condition or disorder. Examples include disorders like: Alzheimer's Disease, Frontotemporal Dementia, Amyotrophic Lateral Sclerosis, LBD and other cognitive declines.
Given some NGS datasets from a specific human disease, if you were to decide on which genes or genomic features should be investigated in this particular human disease, how would you choose? In order to answer this question, in this study, we have developed a novel bioinformatics tool for the analysis of genomic features in human disease samples.
<br>
We developed a bioinformatics tool for the statistical analysis of genomic features (i.e. genes, exons, viruses, phages, microbes, bacteria e.t.c) across regions of interest in human disease samples using public datasets by computing the number of blocks (exons) 
in each targeted region or Browser Extensible Data (BED) line in the sample.
<br><br>
For instance if we have more than 100 human samples, and each sample has a summary of its significant genomic features (with corresponding coverage for each feature) like this:
{'NC_010463.1': 92, 'NC_019488.1': 89, 'NC_018275.1': 53, 'NC_031129.1': 53, 'NC_010393.1': 77, 'NC_005841.1': 53, 'NC_030919.1': 53, 'NC_028699.1': 89, 'NC_019545.1': 72, 'NC_005340.1': 56, 'NC_010392.1': 70, 'NC_014900.1': 63, 'NC_011802.1': 69, 'NC_031946.1': 55, 'NC_017985.1': 80, 'NC_018279.1': 62, 'NC_004348.1': 66}
<br><br>
If the total no. of features is 153 but each sample has different significant features. We want to compare all 100 samples and find out if there are specific features that occur in all 100 samples or most of them, and what is the corresponding coverage for each feature in these samples. We are already printing the above summary for each sample. It's just the sample comparison part that is being worked on at the moment. "Compare significant features in each sampl and print most frequent features and corresponding coverage".
<br><br>
Again, we want to compare all samples and find out which of the features are most frequent and print corresponding coverage. The goal is to recommend the most common features to scientists for further investigation or study.



## Introduction


## Methods


## Results


## Conclusion
