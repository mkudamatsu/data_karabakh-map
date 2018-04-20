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
    print "Inputs being set..."
    # Datum: WGS 1984
    wgs1984 = arcpy.SpatialReference(4326) # See page 18 of http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-classes/pdf/geographic_coordinate_systems.pdf
    # Line of Contact line feature
    input_line = "../data/karabakh-line-of-contact.shp" # coordinate system undefined

    print "Outputs being set..."
    output_line = "../data/karabakh-line-of-contact-wgs1984.shp"

    print "Processing..."
    arcpy.Project_management(input_line, output_line, wgs1984)

    print "All done."

  except:
    print arcpy.GetMessages()

# subfunctions
def delete_if_exists(file):
  if arcpy.Exists(file):
    arcpy.Delete_management(file)


### Execute the main function ###
if __name__ == "__main__":
    main()
