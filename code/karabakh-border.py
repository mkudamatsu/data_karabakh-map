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
    rgb_raster = "Map_Artsakh_(NKR)_en_equidistant_conic_395_400_cm440.tiff"
    rgb_value_for_border = [171, 52, 69]
    # Output
    border_raster = "karabakh-border.tif"
    # Process
    extract_border(rgb_raster, border_raster, rgb_value_for_border)

    print "All done."

  except:
    print arcpy.GetMessages()

# subfunctions
def extract_border(in_rgb_raster, out_indicator_raster, rgb_value_list):
  print "Deleting the output if it exists"
  delete_if_exists(out_indicator_raster)
  print "Extracting red values"
  red_raster = "red.tif"
  rgb_to_color(in_rgb_raster, red_raster, "red")
  print "Extracting green values"
  green_raster = "green.tif"
  rgb_to_color(in_rgb_raster, green_raster, "green")
  print "Extracting blue values"
  blue_raster = "blue.tif"
  rgb_to_color(in_rgb_raster, blue_raster, "blue")

  print "Extracting the border's red value locations"
  red_value_for_border = "VALUE = " + str(rgb_value_list[0])
  red_object = Con(Raster(red_raster), 1, 0, red_value_for_border)
  print "Extracting the border's green value locations"
  green_value_for_border = "VALUE = " + str(rgb_value_list[1])
  green_object = Con(Raster(green_raster), 1, 0, green_value_for_border)
  print "Extracting the border's blue value locations"
  blue_value_for_border = "VALUE = " + str(rgb_value_list[2])
  blue_object = Con(Raster(blue_raster), 1, 0, blue_value_for_border)

  print "Extracting the border"
  border_raster_object = red_object * green_object * blue_object
  print "Saving the raster object"
  border_raster_object.save(out_indicator_raster)

  print "Deleting intermediate files"
  file_list = [red_raster, green_raster, blue_raster]
  for file in file_list:
    delete_if_exists(file)

def rgb_to_color(in_raster, out_ras, color):
  print "... deleting the output file if it exists"
  delete_if_exists(out_ras)
  print "... setting the color"
  if color == "red":
      color_number = "1"
  if color == "green":
      color_number = "2"
  if color == "blue":
      color_number = "3"
  print "... making raster layer"
  # arcpy.MakeRasterLayer_management(in_raster, out_ras, band_index = color_number)
  arcpy.MakeRasterLayer_management(in_raster, "temp_layer", band_index = color_number)
  # See http://pro.arcgis.com/en/pro-app/tool-reference/data-management/make-raster-layer.htm for the tool help
  print "... saving as a tiff file"
  arcpy.CopyRaster_management("temp_layer", out_ras)

def delete_if_exists(file):
  if arcpy.Exists(file):
    arcpy.Delete_management(file)


### Execute the main function ###
if __name__ == "__main__":
    main()
