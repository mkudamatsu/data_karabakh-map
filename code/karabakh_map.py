print "Setting the working directory"
import os
work_dir = os.path.dirname(os.path.realpath(__file__)) # This method returns the directry path of this script.
os.chdir(work_dir)

print "Launching ArcGIS"
import arcpy

print "Enabling the Spatial Analyst extension"
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

print "Setting the environment"
arcpy.env.overwriteOutput = True # Allow the overwriting of the output files
arcpy.env.workspace = "../temp/" # NEVER USE single backslash (\). # Set the working directory.

### Define the main function ###
def main():
  try:
    # Input
    url = "http://www.mfa.am/u_files/file/Map_Artsakh_(NKR)_en.pdf"
    # Output
    output_pdf = "../orig/karabakh_map.pdf"
    output_tif = "karabakh_map.tif"
    # Process
    obtain_data(url, output_pdf)
    arcpy.PDFToTIFF_conversion(output_pdf, output_tif)

    print "All done."

  except:
    print arcpy.GetMessages()

# subfunctions
def obtain_data(address, outfile):
    print "...launching urllib"
    import urllib
    print "...downloading data"
    urllib.urlretrieve(address, outfile)

def delete_if_exists(file):
  if arcpy.Exists(file):
    arcpy.Delete_management(file)


### Execute the main function ###
if __name__ == "__main__":
    main()
