# this script was written by Jack Stevenson in 2022
# input: CSV of publications downloaded from Pubmed
# (recommended search: author "Shokat K")
# output: body text of Shokat lab website publications page
# note 1: after updating pubs.md content, still need to upload pdfs
# name pdfs by PMID and put in "/pdfs" folder
# note 2: I have made some minor corrections to the Pubmed download by hand
# when updating in future, I recommend just running this script on new pubs
# then just add the new pubs to the top of pubs.md
# good luck!

import pandas as pd


def format(df):
    return (f"* {df.Authors} {df.Title}. {df.Citation}\n\n"
            f"    ([PMID {df.PMID}]"
            f"(https://www.ncbi.nlm.nih.gov/pubmed/{df.PMID})) ([PDF]"
            f"({{{{ site.baseurl }}}}/pdfs/{df.PMID}.pdf))\n")


#  read in data from downloaded CSV file (change file name if necessary)
pubs = pd.read_csv("csv-ShokatKAut-set.csv", dtype=str)
# create a new dataframe column of the text output for each publication
pubs["formatted"] = pubs.apply(format, axis=1)
# concatenate all the outputs together to make one big chunk of body text
output = pubs.formatted.str.cat(sep="\n")
# write the output to a file for later copying into pubs.md
with open("pubs_body.txt", 'w') as f:
    f.write(output)
