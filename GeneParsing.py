"""Use this if there is a .gbff file to sort the gRNA target sequences for reporting and off target searching."""


class CASPER_Database:

    def __init__(self):
        self.annotation_file_path = "/Users/brianmendoza/Dropbox/Trinh_Lab/KFED_annotation/kfd.gbff"
        self.cspr_file_path = "/Users/brianmendoza/Dropbox/JGI/kfdspCas9.cspr"
        self.exons = list()

        self.database = dict()


    def generate_exons(self):
        f = open(self.annotation_file_path)
        for line in f:


    def setup_database(self):



