"""File for generating a library of sequences given an input of gene locations."""

import SeqTranslate

class Library:

    def __init__(self, cspr_file, genelistfile):
        self.cspr_file = cspr_file
        self.genelist = genelistfile

        self.Genes = dict()

        self.CSPR = list()  # list of lists with chromosomes and targets
        for i in range(0,17):
            self.CSPR.append(list())

        self.import_gene_list()
        self.import_cspr()

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
            self.CSPR[i].append(line[:-1])
        print("cspr file imported.")

    def generate(self,num_targets_per_gene, score_limit, space, output_file):
        for gene in self.Genes:
            target_list = self.CSPR[self.Genes[gene][0]]
            for i in range(0,num_targets_per_gene):









L = Library("/Users/brianmendoza/Dropbox/sce_spCas9.cspr", "/Users/brianmendoza/Desktop/sacc_gene_list.txt")
L.generate(5, 30, "/Users/brianmendoza/Desktop/Sce_Library_spCas9.txt")