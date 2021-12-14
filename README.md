# Thank you for downloading the plugin.

# Plugin for Qgis : Burying_Laterals

## Function : 
This plugin “Burying_Laterals” is used for accurately burying the laterals along a main in a subsurface tile drainage system, using the field profile from a DEM with a defined area. 

Basically, the plugin is developed for the following reasons:

1. Used to help visualize the burying of tile drainage systems, and thereby simplifying its process, particularly for inexperienced designers.
2. Used for proving both a depth elevation profile and a direction on where best laterals can be buried on the field along a main.

This plugin defines an area from a DEM data using an input boundary layer and then performs analysis such as:

1. Performs terrain analysis to extracts out the field surface profiles in DEM and then determines the best depth for burying the tile drainage system based on the main primary input parameters. 
2. Generates elevation depths along both the main and laterals line layers within the boundary layer extent on the map canvas of the DEM file. 
All results from the plugin execution are saved in the specified folder. At the end, go to the specified folder and there you will see  
subfolders where all save files. : “Plugin_Results” and “Laterals_(name of DEM layer)”. The entire task of the plugin takes few seconds depending on the extent of the boundary layer extracted.

## Issues
You can report a issue [here](https://github.com/FVW-Services/Burying_Laterals/issues/new) and check the current [issues](https://github.com/FVW-Services/Burying_Laterals/issues).

## Developers :
Compile `ressources.py` with OSGeo4W Shell and the command : `pyrcc5 -o resources.py resources.qrc`

Edit `Burying_Laterals_dialog_base.ui` with QT designer (in Qt Creator).

## Feedbacks
Feel free to contact us: fvw.services@gmail.com

## User Guide :
ILLINOIS DRAINAGE GUIDE (ONLINE) : (http://www.wq.illinois.edu/DG/extraction/BURYING_LATERALS_User_Guide.pdf) 