#from sh import gdalwarp, gdal_translate
##import subprocess
##import os
##import shlex
##
##from osgeo import gdal
#from processing.core.Processing import Processing
#Processing.initialize()
#from processing.tools import *
import processing
import os
from qgis.PyQt.QtCore import QFileInfo
from qgis.core import *
import json


def clip(shape, tiff, location, gif_output):
 
    tif_output = gif_output[:-3] + "tif"

    processing.run('gdal:cliprasterbymasklayer', 
                            {'INPUT':tiff,
                             'MASK':shape,
                             'NODATA':0,
                             'ALPHA_BAND':False,
                             'CROP_TO_CUTLINE':True,
                             'KEEP_RESOLUTION':True,
                             'DATA_TYPE':5,
                             'OUTPUT':tif_output})


    
    
   

    fileInfo = QFileInfo(tif_output)
    baseName = fileInfo.baseName()    
    rlayer = QgsRasterLayer(tif_output, baseName)
    extent = rlayer.extent()
    xmin = extent.xMinimum()
    xmax = extent.xMaximum()
    ymin = extent.yMinimum()
    ymax = extent.yMaximum()
    epsg = rlayer.crs().authid().replace("EPSG:","")
    rows = rlayer.height()
    columns = rlayer.width()
    if ".slope." in tif_output:
        extent_path = os.path.join(os.path.dirname(tif_output),"extent.json")
        extentDict = {"xmin":xmin, "xmax":xmax, "ymin":ymin, "ymax":ymax, "epsg": epsg, "columns": columns, "rows": rows}
        #extent_path = gif_output[:-3] + "extent"
        extent_path = extent_path.replace(".slope.", ".")
        with open (extent_path, "w") as fp:
            json.dump(extentDict, fp)
    
       #hay que checar nodata!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! en los dos comandos
    #processing.run('gdal:translate',{"INPUT":tif_output,"OUTSIZE":100,"OUTSIZE_PERC":True,"EXPAND":0,"PROJWIN":"%f,%f,%f,%f"%(xmin, xmax, ymin, ymax),"OUTPUT":gif_output})
    processing.run('gdal:translate', {"INPUT":tif_output,"COPY_SUBDATASETS":False,"DATA_TYPE":0,"OUTPUT":gif_output})





##    sh.gdalwarp("-cutline", shape,
##             "-crop_to_cutline", 
##             "-cwhere", 'location="%s"' % location,
##             "-of", 'GTiff',
##             tiff,
##             tif_output)
##
##    sh.gdal_translate("-of", "GIF",
##                   tif_output,
##                   gif_output)

# clip('General/delegaciones.shp',
#       'General/General.urban.1980.tif',
#       'Iztapalapa',
#       'iz.gif')
