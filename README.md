# nd2_to_dax_converter
This repository is intended to complete batch conversions of nd2 files to dax files for STORM image analysis (adapted from HazenBabcock at Zhaung Lab).


## Instructions for use
Before getting started with the file conversion, ensure that all files in the nd2_to_dax_converter are downloaded and unzipped. To ensure that no errors occur during processing, folders should be set up according to the following:

- **Project Folder/**
  - **nd2_to_dax_converter-main/**
    - datawriter.py   
    - converter.py  
  - **input_data/** — folder containing ND2 files  
  - **output_data/**
    - **tiff_files/** — TIFF output files  
    - **dax_files/** — DAX output files

**Create the Input and Output data folders but DO NOT add any files into the Output folder**

Once the files have been set up this way, the code can be run in either the terminal (Mac) or command line (Windows). Be sure to navigate to the directory/folder called nd2_to_dax_converter-main. From this directory, type **python converter.py "..\input_data" "..\output_data"** to run the program. 
