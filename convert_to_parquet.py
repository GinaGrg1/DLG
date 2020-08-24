
import pandas as pd
from datetime import datetime
import os
import sys
import glob

import argparse


def getfiles(expr):
    return glob.glob(expr)


def convert_csv(filelist, outfolder):
    for file in filelist:
        filename = file.replace('.csv','').split('/')[-1]
        df = pd.read_csv(file)
        df.to_parquet(f"{outfolder}{filename}.parquet")


if __name__ == "__main__":
    file_pattern = "*.csv"
    parser = argparse.ArgumentParser("Convert csv from infolder into parquet to outfolder")
    parser.add_argument('-i', '--infolder', type=str, 
                        help="Folder where all the weather files are stored as csvs", required=True)
    parser.add_argument('-o', '--outfolder', type=str,
                        help="Folder where the paquet files will be saved.", required=True)
    
    args = parser.parse_args()
    input_folder = './' + args.infolder + '/' + file_pattern
    output_folder = './' + args.outfolder + '/'
    
    files = getfiles(input_folder)
    convert_csv(files, output_folder)
