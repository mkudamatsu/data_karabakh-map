To replicate the georeferencing of the map of Nagorno-Karabakh, follow these steps (see [ArcGIS Help "](http://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/georeferencing-a-raster-to-a-vector.htm) for detail)

1. Launch ArcMap.
2. Add `georeference_control_points.shp`.
3. Then add `karabakh_map.tif`. Do not add this file first: otherwise the mapping projection may be distorted.
4. Display ArcMap's Georeference tool bar. (See Step 2 in [this ArcGIS help](http://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/georeferencing-a-raster-to-a-vector.htm).)
5. Right-click `georeference_control_points.shp` and choose Zoom To Layer.
6. In the Georeference tool bar, click the Georeferencing drop-down menu and click Fit To Display. This displays `karabakh_map.tif` in the same area as `georeference_control_points.shp`.
7. Click the Add Control Points tool in the Georeference tool bar. (See [this help](http://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/georeferencing-toolbar-tools.htm) for detail.)
8. Click one of the 12 intersections of grid lines in the `karabakh_map.tif`. Then click the corresponding point in `georeference_control_points.shp`. Repeat this for all the 12 points.
9. In the Georeference tool bar, click the View Link table icon (see [this ArcGIS help](http://desktop.arcgis.com/en/arcmap/10.3/manage-data/cad/managing-links-and-control-points.htm) for detail). In the window that opens, select "2nd Order Polynomial" in the dropdown menu for Transformation at the bottom of the window. (See [this ArcGIS help](http://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/fundamentals-for-georeferencing-a-raster-dataset.htm#GUID-E0959E92-489D-4956-BF2B-B50170242E22) for detail on polynomial transformation.) 
10. In the Georeference tool bar, click the Georeferencing drop-down menu and click Rectify. A new file is created. Name this file `karabakh_map_georeferenced.tif`.
