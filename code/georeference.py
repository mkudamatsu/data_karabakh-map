print "Setting the working directory"
import os
work_dir = os.path.dirname(os.path.realpath(__file__)) # This method returns the directry path of this script.
os.chdir(work_dir)

print "Importing the regular expression module" # For custumizing spatial reference. See https://arcpy.wordpress.com/2013/06/21/altering-spatial-references-in-python/
import re

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
    # Lambert Conformal Conic projection paramters used by C.I.A for the map of Armenia: see https://legacy.lib.utexas.edu/maps/armenia.html and https://legacy.lib.utexas.edu/maps/commonwealth/armenia_rel-2002.pdf
    lambert = arcpy.SpatialReference(102014) # see page 18 of http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-classes/pdf/projected_coordinate_systems.pdf
    print "Changing parameters 1/3"
    lambert.loadFromString(re.sub('PARAMETER\[\'Central_Meridian\'\,.+?]', 'PARAMETER\[\'Central_Meridian\',45.0]', lambert.exportToString()))
    print "Changing parameters 2/3"
    lambert.loadFromString(re.sub('PARAMETER\[\'Standard_Parallel_1\'\,.+?]', 'PARAMETER\[\'Standard_Parallel_1\',39.0]', lambert.exportToString()))
    print "Changing parameters 3/3"
    lambert.loadFromString(re.sub('PARAMETER\[\'Standard_Parallel_2\'\,.+?]', 'PARAMETER\[\'Standard_Parallel_2\',41.0]', lambert.exportToString()))
    # Azerbaijan rayon polygons
    gadm = "../orig/AZE_adm.gdb/AZE_adm2"           # coordinate system already defined as WGS 1984
    acasian = "../orig/Acasian/azerbaijan_adm2.shp" # coordinate system undefined

    print "Outputs being set..."
    output_fishnet = "georeference_fishnet.shp"
    output_gadm = "georeference_gadm.shp"
    output_acasian = "georeference_acasian.shp"

    print "Processing..."
    create_grid(output_fishnet, wgs1984, lambert)
    project4karabakh(gadm, output_gadm, lambert)
    define_and_project4karabakh(acasian, output_acasian, wgs1984, lambert)
    print "All done."

  except:
    print arcpy.GetMessages()

# subfunctions
def create_grid(out_shp, datum, projection):
  print "...Deleting the output if it exists"
  delete_if_exists(out_shp)
  print "...Setting intermediate files"
  fishnet_shp = "fishnet.shp"
  print "...Creating a fishnet"
  arcpy.CreateFishnet_management(fishnet_shp, "46 39", "46 49", "0.5", "0.5", "", "", "47 40.5", "NO_LABELS", "46 39 47 40.5", "POLYLINE")
  print "...Defining datum"
  arcpy.DefineProjection_management(fishnet_shp, datum)
  print "...Projecting"
  project4karabakh(fishnet_shp, out_shp, projection)
  print "...Deleting intermediate files"
  arcpy.Delete_management(fishnet_shp)

def define_and_project4karabakh(in_shp, out_shp, datum, projection):
  print "...Copying the input file"
  copy_shp = "copy.shp"
  arcpy.CopyFeatures_management(in_shp, copy_shp)
  print "...Defining datum"
  arcpy.DefineProjection_management(copy_shp, datum)
  print "...Projecting"
  project4karabakh(copy_shp, out_shp, projection)
  print "...Deleting intermediate files"
  arcpy.Delete_management(copy_shp)

def project4karabakh(in_shp, out_shp, projection):
  print "...Deleting the output if it exists"
  delete_if_exists(out_shp)
  print "...Projecting"
  arcpy.Project_management(in_shp, out_shp, projection)

def delete_if_exists(file):
  if arcpy.Exists(file):
    arcpy.Delete_management(file)


### Execute the main function ###
if __name__ == "__main__":
    main()
