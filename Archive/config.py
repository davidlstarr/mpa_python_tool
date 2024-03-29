#------------------------------------------------------------------------------------------------------#
#--------All of the variables that are used throughout the steps. Please update accordingly.---------#
#------------------------------------------------------------------------------------------------------#

import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)
SDE_CONNECTION = arcpy.GetParameterAsText(1)

mysql = {'host': 'localhost',
         'user': 'root',
         'passwd': 'my secret password',
         'db': 'write-math'}

#Web Feature Service Paths:
WFS_paver_path = "https://services1.arcgis.com/oS5ru2iHb8I5vlTv/arcgis/rest/services/PCA_Collector_WFS/FeatureServer/0"
WFS_concrete_path =  "https://services1.arcgis.com/oS5ru2iHb8I5vlTv/arcgis/rest/services/PCA_Collector_WFS/FeatureServer/1"
WFS_asphalt_path = "https://services1.arcgis.com/oS5ru2iHb8I5vlTv/arcgis/rest/services/PCA_Collector_WFS/FeatureServer/2"
WFS_other_type_path = "https://services1.arcgis.com/oS5ru2iHb8I5vlTv/arcgis/rest/services/PCA_Collector_WFS/FeatureServer/3"
WFS_PCA_PHOTOS = "https://services1.arcgis.com/oS5ru2iHb8I5vlTv/arcgis/rest/services/PCA_Collector_WFS/FeatureServer/4"
WFS_Pavement_Assessment_Areas = "https://services1.arcgis.com/oS5ru2iHb8I5vlTv/arcgis/rest/services/PCA_Collector_WFS/FeatureServer/5"
WFS_Historic_Assessment_points = "https://services1.arcgis.com/oS5ru2iHb8I5vlTv/arcgis/rest/services/PCA_Collector_WFS/FeatureServer/6"

#Temporary Paths

TEMP_PAVERS_PCA = "PAVERS_PCA"
TEMP_CONCRETE_PCA = "CONCRETE_PCA"
TEMP_ASPHALT_PCA = "ASPHALT_PCA"
TEMP_OTHER_PCA = "OTHER_PCA"

PAVERS_PCA_Updates = "PAVERS_PCA_Updates"
CONCRETE_PCA_Updates = "CONCRETE_PCA_Updates"
ASPHALT_PCA_Updates = "ASPHALT_PCA_Updates"
OTHER_PCA_Updates = "OTHER_PCA_Updates"

