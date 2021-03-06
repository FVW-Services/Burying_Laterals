# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Burying_LateralsDialog
                                 A QGIS plugin
  This plugin adds lateral and prints a recommended elevation and Distance along the mainlines.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-01-12
        git sha              : $Format:%H$
        copyright            : (C) 2021 by FALASY Anamelechi
        email                : fvw.services@gmail.com
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

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt import QtCore
from qgis.core import *

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Burying_Laterals_dialog_base.ui'))


class Burying_LateralsDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Burying_LateralsDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.VectorLayer)
        self.mMapLayerComboBox_2.setFilters(QgsMapLayerProxyModel.VectorLayer)
        self.mMapLayerComboBox_3.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.LineLayer)
        self.mMapLayerComboBox_2.setFilters(QgsMapLayerProxyModel.LineLayer)
        self.mMapLayerComboBox_4.setFilters(QgsMapLayerProxyModel.VectorLayer)
        self.mMapLayerComboBox_4.setFilters(QgsMapLayerProxyModel.PolygonLayer)
        # self.mMapLayerComboBox.setShowCrs(True)
        # self.mMapLayerComboBox_2.setShowCrs(True)
        # self.mMapLayerComboBox_3.setShowCrs(True)
        # self.getLayer_main()
        # self.getLayer_lateral()
        # self.getLayer_overlay()
                
    # def getLayer_main(self):
        # # # get main layer from combobox 1
        # self.comboMains.clear()
        # layers = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
        # self.comboMains.addItems(layers)
                
    # def getLayer_lateral(self):
        # # # get lateral layer from combobox 2
        # self.comboLaterals.clear()
        # layers = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
        # self.comboLaterals.addItems(layers)
        
    # def getLayer_overlay(self):
        # # # get overlaying layer from combobox 3
        # self.comboOvalay.clear()
        # layers = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
        # self.comboOvalay.addItems(layers)
        
