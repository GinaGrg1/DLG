## Steps 

* Please run `pip install -r requirements.txt` to install required packages.

## Assumptions
* There is a folder (*infolder*) which contains all the weather data files as csvs. Please create a new folder (*outfolder*)where parquet files will be saved.

## Running the code
* There are three python scripts:
    - convert_to_parquet.py
    - max_temperature.py
    - max_temperature_spark.py
* Please run convert_to_parquet.py as following:
` python3 convert_to_parquet -i (*infolder*) -o (*outfolder*)`
  
