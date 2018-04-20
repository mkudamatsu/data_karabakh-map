This repository provides the shapefile of Nagorno-Karabakh's Line of Contact line feature, based on (1) the PDF map of Nagorno-Karabakh available on the website of Armenian Ministry of Foreign Affairs and (2) the shapefile of Azerbaijan Soviet Socialist Republic and Nagorno-Karabakh Autonomous Republic Oblast polygon features created by the Acasian project.

To replicate the data creation, follow these steps.

1. Install ArcGIS 10.
2. Run `code/karabakh_map.py` to download the PDF map of Nagorno-Karabakh and convert it into a TIFF image.
3. Run `code/georeference.py` to (1) create control point features for georeferencing the map of Nagorno-Karabakh, (2) produce the grid of meridians and parallels to check if georeferencing is successful, and (3) convert the coordinate system of the Acasian project shapefile. All the output shapefiles are in the Lambert Conformal Conic projection with 45E as the central meridian and 39N and 41N as standard parallels, because this map projection is most likely the closest to the one used by the PDF map of Nagorno-Karabakh.
4. In ArcMap, georeference the map of Nagorno-Karabakh. INSERT THE PROCEDURE IN DETAIL.
5. Run `code/karabakh-border.py` to assign the coordinate system to the georeferenced map and to extract the border line pixels.
6. In ArcMap, create `data/karabakh-line-of-contact.shp` by tracing the border line pixels of Nagorno-Karabakh and, in part, the border of Nagorno-Karabakh Autonomous Republic Oblast. INSERT THE PROCEDURE IN DETAIL.
7. Run `code/karabakh-line-of-contact-wgs1984.py` to convert the map projection of the Line of Contact line feature into WGS 1984 (so that it can be overlayed with various spatial datasets).

The result of processes 4 and 6 can be seen by opening line-of-contact.mxd in ArcMap.
