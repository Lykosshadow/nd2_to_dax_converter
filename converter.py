import glob
import numpy as np
import sys
import os
import tifffile
import nd2 

import datawriter
import datareader 


def convert_nd2_to_tiff(nd2_path, tiff_path):
    print(f"Converting ND2 to TIFF: {nd2_path} → {tiff_path}")
    try:
        nd2.nd2_to_tiff(nd2_path, tiff_path, progress=False)
    except Exception as e:
        print(f"Error converting ND2: {e}")
        return False
    return True

def convert_tiff_to_dax(tiff_path, dax_path):
    print(f"Converting TIFF to DAX: {tiff_path} → {dax_path}")
    
    try:
        reader=datareader.TifReader(tiff_path)
        dax_file=datawriter.DaxWriter(dax_path)

        try:
            num_frames = reader.filestream.shape[0]
        except AttributeError:
            num_frames = 1

        for i in range(num_frames):
            frame = reader.loadAFrame(i)
            dax_file.addFrame(frame)

        dax_file.close()
    except Exception as e:
        print(f"Error converting TIFF to DAX: {e}")
        return False

    return True    
    

def main(nd2_folder, output_folder):
    if not os.path.isdir(nd2_folder):
        print(f"Folder not found: {nd2_folder}")
        sys.exit(1)
    
    nd2_files = sorted(glob.glob(os.path.join(nd2_folder, "*.nd2")))

    if not nd2_files:
        print(f"No ND2 files found.")
        sys.exit(1)

    tiff_dir = os.path.join(output_folder, "tiff_files")
    dax_dir = os.path.join(output_folder, "dax_files")
    os.makedirs(tiff_dir, exist_ok=True)
    os.makedirs(dax_dir, exist_ok=True)


    for nd2_file in nd2_files:
        base_name = os.path.splitext(os.path.basename(nd2_file))[0]
        tiff_path = os.path.join(tiff_dir, base_name + ".tif")
        dax_path = os.path.join(dax_dir, base_name + ".dax")

        success_tiff = convert_nd2_to_tiff(nd2_file, tiff_path)
        if success_tiff:
            convert_tiff_to_dax(tiff_path, dax_path)

    print("Batch conversion completed.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python nd2_to_dax_batch.py /path/to/nd2_files/ /path/to/output_folder/")
        sys.exit(1)

    nd2_folder = sys.argv[1]
    output_folder = sys.argv[2]
    main(nd2_folder, output_folder)