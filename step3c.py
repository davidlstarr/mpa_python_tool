#-----------------------------------------------------------------#
#--------Step 3c-Reset Collection Points, Local PCA Point---------#
#-----------------------------------------------------------------#

import arcpy
import json

# Script parameters
arcpy.env.workspace = arcpy.GetParameterAsText(0)
SDE_CONNECTION = arcpy.GetParameterAsText(1)

workspace_split = arcpy.env.workspace[:46]

#Make sure to drop the config file in your ArcPro project
with open(workspace_split+'/config.json') as json_data_file:
    data = json.load(json_data_file)

# Web Feature Service Paths:
WFS_paver_path = data["wfs_paths"]["WFS_paver_path"]
WFS_concrete_path = data["wfs_paths"]["WFS_concrete_path"]
WFS_asphalt_path = data["wfs_paths"]["WFS_asphalt_path"]
WFS_other_type_path = data["wfs_paths"]["WFS_other_type_path"]
WFS_PCA_PHOTOS = data["wfs_paths"]["WFS_PCA_PHOTOS"]
WFS_Pavement_Assessment_Areas = data["wfs_paths"]["WFS_Pavement_Assessment_Areas"]
WFS_Historic_Assessment_points = data["wfs_paths"]["WFS_Historic_Assessment_points"]

# Temporary Paths
TEMP_PAVERS_PCA = data["temp_paths"]["TEMP_PAVERS_PCA"]
TEMP_CONCRETE_PCA = data["temp_paths"]["TEMP_CONCRETE_PCA"]
TEMP_ASPHALT_PCA = data["temp_paths"]["TEMP_ASPHALT_PCA"]
TEMP_OTHER_PCA = data["temp_paths"]["TEMP_OTHER_PCA"]

PAVERS_PCA_Updates = data["temp_paths"]["PAVERS_PCA_Updates"]
CONCRETE_PCA_Updates = data["temp_paths"]["CONCRETE_PCA_Updates"]
ASPHALT_PCA_Updates = data["temp_paths"]["ASPHALT_PCA_Updates"]
OTHER_PCA_Updates = data["temp_paths"]["OTHER_PCA_Updates"]

arcpy.AddMessage("Reset Collection Points, Local PCA Point")


# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

#Delete Temporary Layers
arcpy.Delete_management("TEMP_PAVERS_PCA_SELECTION")
arcpy.Delete_management("TEMP_CONCRETE_PCA_SELECTION")
arcpy.Delete_management("TEMP_ASPHALT_PCA_SELECTION")
arcpy.Delete_management("TEMP_OTHER_PCA_SELECTION")
arcpy.Delete_management("merged_PCA_Polygons")
arcpy.AddMessage("Updated_record has been removed")
arcpy.Delete_management("Updated_record")
arcpy.Delete_management("WFS_PCA_POLYGON_SELECTION")
arcpy.Delete_management("WFS_PCA_POLYGON_JOIN")
arcpy.Delete_management("merged_PCA_Updates")
arcpy.Delete_management("merged_PCA_Updates_SpatialJo")
arcpy.Delete_management("merged_PCA_Updates_SpatialJoin_GT_2")
arcpy.AddMessage("PAVERS_PCA has been removed")
arcpy.Delete_management(TEMP_PAVERS_PCA)
arcpy.AddMessage("CONCRETE_PCA has been removed")
arcpy.Delete_management(TEMP_CONCRETE_PCA)
arcpy.AddMessage("ASPHALT_PCA has been removed")
arcpy.Delete_management(TEMP_ASPHALT_PCA)
arcpy.AddMessage("OTHER_PCA has been removed")
arcpy.Delete_management(TEMP_OTHER_PCA)
arcpy.AddMessage("PAVERS_PCA_Updates has been removed")
arcpy.Delete_management(PAVERS_PCA_Updates)
arcpy.AddMessage("CONCRETE_PCA_Updates has been removed")
arcpy.Delete_management(CONCRETE_PCA_Updates)
arcpy.AddMessage("ASPHALT_PCA_Updates has been removed")
arcpy.Delete_management(ASPHALT_PCA_Updates)
arcpy.AddMessage("OTHER_PCA_Updates has been removed")
arcpy.Delete_management(OTHER_PCA_Updates)

arcpy.AddWarning("All temporary layers have been removed. If no errors, you can move on to Step 4.")