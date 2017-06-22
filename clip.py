from sh import gdalwarp


def clip(shape, tiff, location, output):
    gdalwarp("-cutline", shape,
             "-crop_to_cutline", 
             "-cwhere", 'location="%s"' % location,
             "-of", 'GTiff',
             tiff,
             output)


# clip('General/delegaciones.shp',
#      'General/General.urban.1980.tif',
#      'Iztapalapa',
#      'iz.tif')
