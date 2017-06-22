from sh import gdalwarp, gdal_translate


def clip(shape, tiff, location, gif_output):
    tif_output = gif_output[:-3] + "tif"
    gdalwarp("-cutline", shape,
             "-crop_to_cutline", 
             "-cwhere", 'location="%s"' % location,
             "-of", 'GTiff',
             tiff,
             tif_output)

    gdal_translate("-of", "GIF",
                   tif_output,
                   gif_output)

# clip('General/delegaciones.shp',
#       'General/General.urban.1980.tif',
#       'Iztapalapa',
#       'iz.gif')
