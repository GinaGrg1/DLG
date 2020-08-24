import argparse
import pandas as pd


def read_parquet(path):
    df = pd.read_parquet(path, engine='pyarrow')
    max_index = df.ScreenTemperature.idxmax()
    max_temp_row = df.iloc[max_index]

    return max_temp_row


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Read parquet files and get Max temperature details")
    parser.add_argument('-i', '--infolder', type=str, 
                        help="Folder where all the weather files are stored as parquet", required=True)
    
    args = parser.parse_args()
    folder = args.infolder
    print("Hottest day details \n")
    print(read_parquet(folder))