"""Contains the class and associated methods for generating the database of all the guide-RNAs utilizing a mySQL
data structure containing the necessary categories."""

import os

# Storage containers
off_target_dict = dict()  # key: sequence, value: score


# This function gathers the off-target data and puts it into a python object
def get_off_target_scores(filename):
    f = open(filename)
    for line in f:
        my = line[:-1].split(":")
        off_target_dict[my[0]] = my[1]
    f.close()


def iterate_concise_data_file(filename, outfile, remove_iSTOP=False):
    f = open(filename)
    outfile = open(outfile, 'w')
    for line in f:
        # make sure its not a gene or scaffold line:
        if line.startswith("GENE") or line.startswith("SCAFFOLD"):
            outfile.write(line)
        # obtain sequence and lookup in off dictionary
        else:
            target = line[:-1].split(",")
            if target[1] not in off_target_dict:
                offscore = "0.0000000"
            else:
                offscore = off_target_dict[target[1]]
            outstring = ""
            for i in range(len(target)):
                if i == 4 and remove_iSTOP:
                    poo = 1
                else:
                    outstring += target[i] + ","
            outstring += offscore[0:6] + "\n"
            print(outstring)
            outfile.write(outstring)
    f.close()
    outfile.close()


get_off_target_scores("/Users/brianmendoza/Dropbox/kfd_batch/kfd_off_scores.txt")
iterate_concise_data_file("/Users/brianmendoza/Desktop/kfd_concise_data_iSTOP.csv",
                          "/Users/brianmendoza/Dropbox/kfd_concise_data_offscores.csv", remove_iSTOP=True)