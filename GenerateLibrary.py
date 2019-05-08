"""File for generating a library of sequences given an input of gene locations."""

from SeqTranslate import SeqTranslate

class Library:

    def __init__(self, cspr_file, genelistfile):
        self.cspr_file = cspr_file
        self.genelist = genelistfile

        self.S = SeqTranslate()

        self.Genes = dict()

        self.CSPR = list()  # list of lists with chromosomes and targets
        for i in range(0,17):
            self.CSPR.append(list())

        self.import_gene_list()
        self.import_cspr()

        self.Output = dict()

    def import_gene_list(self):
        f = open(self.genelist)
        for line in f:
            geneinfo = line[:-1].split("\t")
            self.Genes[geneinfo[0]] = [int(geneinfo[1]),int(geneinfo[2]),int(geneinfo[3]),geneinfo[4]]
        f.close()
        print("Gene list imported.")

    def import_cspr(self):
        i = 0  # keeps track of chromosome
        f = open(self.cspr_file)
        f.readline()  # skips genome name
        f.readline()  # skips karystats
        f.readline()  # skips miscellaneous
        while True:
            line = f.readline()
            if line.startswith("REPEATS"):
                break
            if line.startswith(">"):
                i += 1
            else:
                mytuple = self.S.decompress_csf_tuple(line[:-1])
                self.CSPR[i].append(mytuple)
        print("cspr file imported.")

    def generate(self,num_targets_per_gene, score_limit, space, output_file):
        for gene in self.Genes:
            chrom_list = self.CSPR[self.Genes[gene][0]]  # Gets the chromosome the gene is on
            j = 0
            k = 0 #  This keeps track of the index of the chrom list to start at
            l = 0 # This keeps track of the index of the chrom list to end at
            # this loop sets j and k to the be indeces of the start and stop targets
            while j <  self.Genes[gene][1]:
                j = chrom_list[k][0]  # k is the index of the item, 0 is the location
                k += 1
                l = k
            while j < self.Genes[gene][2]:
                j = chrom_list[l][0]
                l += 1
            target_list = chrom_list[k:l+1]
            # Filter out the guides with low scores
            for pos in range(0, len(target_list)):
                if target_list[pos][3] < score_limit:
                    del target_list[pos]
            self.Output[gene] = list()
            for i in range(0,num_targets_per_gene):
                # select the first five targets with the score and space filter that is set in the beginning
                self.Output[gene].append(target_list[i])

        print(self.Output)











L = Library("/Users/brianmendoza/Dropbox/sce_spCas9.cspr", "/Users/brianmendoza/Desktop/sacc_gene_list.txt")
L.generate(5, 30, "/Users/brianmendoza/Desktop/Sce_Library_spCas9.txt")