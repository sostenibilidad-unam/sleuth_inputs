# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SleuthInputs
                                 A QGIS plugin
 a qgis plugin to prepare sleuth inputs
                              -------------------
        begin                : 2017-06-21
        git sha              : $Format:%H$
        copyright            : (C) 2017 by LANCIS
        email                : serranoycandela@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import print_function
from __future__ import absolute_import
from builtins import object
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from qgis.PyQt.QtWidgets import QAction, QFileDialog
from qgis.PyQt.QtGui import QIcon
# Initialize Qt resources from file resources.py
from . import resources
# Import the code for the dialog
from .sleuth_inputs_dialog import SleuthInputsDialog
import os.path
import os
#from qgis.analysis import QgsGeometryAnalyzer
import processing
from qgis.core import QgsVectorLayer
from .clip import clip
from os.path import dirname, join, basename
from os import mkdir
#from processing.core.Processing import Processing
#Processing.initialize()
#from processing.tools import *
import time

class SleuthInputs(object):
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'SleuthInputs_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Sleuth Inputs')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'SleuthInputs')
        self.toolbar.setObjectName(u'SleuthInputs')        
        
    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('SleuthInputs', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference
        self.dlg = SleuthInputsDialog()

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/SleuthInputs/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u''),
            callback=self.run,
            parent=self.iface.mainWindow())

        self.dlg.pushButton.clicked.connect(self.rasters_path)
        self.dlg.pushButton_2.clicked.connect(self.get_mask)

        
    def rasters_path(self):
        self.rasters = []
        openFile = QFileDialog()
        self.rasters_path = QFileDialog.getExistingDirectory(self.dlg, ("Select Output Folder"), '')

        if self.rasters_path:
            for f in os.listdir(self.rasters_path):
                if f.endswith('.tif'):
                    self.dlg.textBrowser.append(f)
                    self.rasters.append(f)
                
        


        
    def get_mask(self):
        openFile = QFileDialog()
        shp_file, __ = QFileDialog.getOpenFileName(self.dlg, "Select shape file", 'C:', "shp(*.shp)")

        if shp_file:
            layer = QgsVectorLayer(shp_file, "sub", "ogr")
            features = layer.getFeatures()
            idx= layer.fields().indexFromName('location')
            #idx = layer.fieldNameIndex('location')
            temp_path = join(self.rasters_path, "temp")
            if not os.path.exists(temp_path):
                mkdir(temp_path)

            
            for feat in features:
                location = feat.attributes()[idx]
                shapeLocation = os.path.join(temp_path,  location + ".shp")
                shapeBuffer = os.path.join(temp_path,  location + "_b.shp")
                # fix_print_with_import
                print(shapeBuffer)
                parameters = {'INPUT': shp_file,
                'FIELD': "location",
                'OPERATOR': 0,
                'VALUE': location,
                'OUTPUT': shapeLocation}
                processing.run('qgis:extractbyattribute', parameters)
                self.dlg.textBrowser.append(location)
                feature_path = join(self.rasters_path, location)
                if not os.path.exists(feature_path):
                    mkdir(feature_path)
                location_layer = QgsVectorLayer(shapeLocation, "location", "ogr")
                #QgsGeometryAnalyzer().buffer(location_layer, shapeBuffer, 3000, False, False, -1)
                processing.run('native:buffer', {"INPUT": location_layer,
                                                 "DISTANCE": 3000,
                                                 'SEGMENTS': 10,
                                                 'DISSOLVE': False,
                                                 'END_CAP_STYLE': 0,
                                                 'JOIN_STYLE': 0,
                                                 'MITER_LIMIT': 10,
                                                 "OUTPUT": shapeBuffer})
                for raster in self.rasters:
                    gif_name = raster.replace("General.",location + ".")[:-3]+'gif'
                    # fix_print_with_import
                    print(gif_name)
                    clip(shape=shapeBuffer,
                         tiff=join(self.rasters_path, raster),
                         location=location,
                         gif_output=join(feature_path, gif_name))


            time.sleep(2)
            for f in os.listdir(temp_path):
                os.remove(join(temp_path,f))
            os.rmdir(temp_path)
                


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Sleuth Inputs'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            openFile = QFileDialog()
            fname = QFileDialog.getExistingDirectory(self.dlg, ("Select Output Folder"), '')
