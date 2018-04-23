To replicate the creation of `data/karabakh-line-of-contact.shp`, follow these steps. (See Parts 3 and 4 of [this document](http://helpwiki.evergreen.edu/wiki/index.php/ArcGIS_10:_Editing_%26_Creating_Your_Own_Shapefiles) for detail.)

**Step 1: Prepare the empty shapefile**
1. Open ArcCatalog.
2. In the Catalogue Tree section on the left, right-click on the `data` folder.
3. Choose “New>>Shapefile”. You will see a new window on the screen called “Create New Shapefile”.
4. Name your new shapefile `karabakh-line-of-contact.shp`. Under the “Feature Type” dropdown, choose “Polyline.”
5. Under “Spatial Reference: Description” click the “Edit” button. Then click the globe icon (the second icon to the last on the top row) and select “Import”. Select `temp/georeference_acasian.shp` and click "Add". Then click “OK.” This assigns the same map projection to `karabakh-line-of-contact.shp` as that of `georeference_acasian.shp`.
6. Finally, click “OK”. A new empty shapefile called `karabakh-line-of-contact.shp` is created. 

**Step 2: Trace the border**
1. In ArcMap, add `data/karabakh-line-of-contact.shp`, `temp/georeference_acasian.shp`, and `temp/karabakh-border.tif`. 
2. In the Table of Contents on the left, right-click `karabakh-line-of-contact` and select “Edit Features>> Organize Feature Templates”.
3. In the window that opens, select `karabakh-line-of-contact` and click “New Template”. The “Create New Templates Wizard” will appear.
4. Make sure `karabakh-line-of-contact` is checked and click “Finish”. Close the “Organize Feature Templates” window.
5. Right-click the `karabakh-line-of-contact` layer and select “Edit Features>>Start Editing”. If any warnings appear, click “Continue”. 
6. A new “Create Features” pane will appear on the right-hand side of the screen. `karabakh-line-of-contact` should appear as one of the layers in this pane. Click on `karabakh-line-of-contact` in the right-hand pane. Note that, in the bottom-right area, you can see some “Construction Tools” and that “Polyline” is selected. 
7. In the Editor toolbar (if you do not see it, in the menu bar, click Cutomize >> Toolbars >> Editor), click the Editor dropdown menu and select Snapping > Snapping Window.
8. In the Snapping Window, check the boxes for Vertex, Edge, and End of `georeference_acasian` in the upper half and Centerline, Corner, Intersection, Ends, and Solid of Raster in the lower half. This enables snapping to the other shapefile and raster during the process of tracing the border. (See [this ArcGIS Help](http://desktop.arcgis.com/en/arcmap/10.3/manage-data/editing-fundamentals/enabling-snapping-classic-snapping-.htm) for detail about snapping.)
9. Now, if you move the mouse cursor into the central map area, the cursor is now a crosshair (like a plus-sign). Click a vertex or edge of `georeference_acasian` to start drawing the border (the snapping helps you do this). Then continue clicking to create the vertices of a new polyline feature of Nagorno-Karabakh Line of Contact along the border raster cells in `karabakh-border.tif` and, when paralleled, the border of Nagorno-Karabakh Autonomous Oblast in `georeference_acasian.shp`.
10. Once you click the last vertex on the line feature of `georeference_acasian`, double-click to finish the drawing.
11. In the Editor toolbar, click “Editor” dropdown menu and select “Stop Editing” to save the new shapefile. 
