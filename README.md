## Steps 

* Please run `pip install -r requirements.txt` to install required packages.


## Assumptions
* This code was tested using Python3.6 and PySpark-2.2.1
* There is a folder (*infolder*) which contains all the weather data files as csvs. Please create a new folder (*outfolder*) where parquet files will be saved.
* To use pyspark, all related configurations/env variables should be set. E.g **SPARK_HOME, PYTHONPATH** (pointing to python from spark) & **PYSPARK_PYTHON**


## Running the code
* There are three python scripts:
    - convert_to_parquet.py
    - max_temperature.py
    - max_temperature_spark.py
    
* Please run **convert_to_parquet.py** as following:<br>
    ` python3 convert_to_parquet -i (infolder) -o (outfolder)` <br>
  This code reads all the csv files in the infolder and writes the files as parquet to outfolder.

* For small number files, we can use python's pandas. Please run: <br>
    ` python3.6 max_temperature.py -i (outfolder)`

* For bigger files, it is best to use spark. There is a chance of getting **'Out of Memory'** error if using python/pandas. Please run:<br>
    `spark-submit max_temperature_spark.py -i (outfolder)`
