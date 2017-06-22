# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SleuthInputs
                                 A QGIS plugin
 a qgis plugin to prepare sleuth inputs
                             -------------------
        begin                : 2017-06-21
        copyright            : (C) 2017 by LANCIS
        email                : serranoycandela@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SleuthInputs class from file SleuthInputs.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sleuth_inputs import SleuthInputs
    return SleuthInputs(iface)
