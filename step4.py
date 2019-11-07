#--------------------------------------#
#--------Step 4- Photo Process---------#
#--------------------------------------#


import arcpy
import json
import time
from datetime import datetime

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

# Script parameters
arcpy.env.workspace = arcpy.GetParameterAsText(0)
SDE_CONNECTION = arcpy.GetParameterAsText(1)
current_date = arcpy.GetParameterAsText(2)

workspace_split = arcpy.env.workspace[:46]

#Make sure to drop the config file in your ArcPro project
with open(arcpy.env.workspace+'/config.json') as json_data_file:
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

arcpy.AddMessage("Photo Process")

# Write messages to a Text File
#
# arcpy.AddMessage(timenow)
# txtFile = open("c:\\temp\\GPMessages.txt", "w")
# txtFile.write(arcpy.GetMessages())
# txtFile.close()

arcpy.Delete_management("WFS_PCA_PHOTOS_SELECTION")
arcpy.Delete_management("SDE_PCA_PHOTOS_copy")

# Local variables:
PCA_Photos = SDE_CONNECTION + "/MPA_USER.PCA_PHOTOS"
TEMP_PCA_Photos = "TEMP_PCA_Photos"

arcpy.Delete_management(TEMP_PCA_Photos)
arcpy.Delete_management("SDE_PCA_PHOTOS_copy")
arcpy.Delete_management("WFS_PCA_PHOTOS_copy")

#Copy WFS PCA Photos and SDE PCA Photos
arcpy.FeatureClassToFeatureClass_conversion(in_features=PCA_Photos, out_path=arcpy.env.workspace, out_name="SDE_PCA_PHOTOS_copy",where_clause="", field_mapping="", config_keyword="")
arcpy.FeatureClassToFeatureClass_conversion(in_features=WFS_PCA_PHOTOS, out_path=arcpy.env.workspace, out_name="WFS_PCA_PHOTOS_copy",where_clause="", field_mapping="", config_keyword="")

# Process: Select Layer By Location
arcpy.AddMessage("Select by location where WFS PCA Photos are identical to SDE PCA Photos")

date = datetime.strptime(current_date, "%d/%m/%Y")
date_str = str(date)

date_expression = "created_date >= timestamp '"+date_str+"'"

#WFS_PCA_PHOTOS_SELECTION = arcpy.SelectLayerByLocation_management(in_layer=WFS_PCA_PHOTOS, overlap_type="ARE_IDENTICAL_TO",select_features=PCA_Photos, search_distance="", selection_type="NEW_SELECTION", invert_spatial_relationship="INVERT")
WFS_PCA_PHOTOS_SELECTION = arcpy.SelectLayerByAttribute_management(in_layer_or_view="WFS_PCA_PHOTOS_copy", selection_type="NEW_SELECTION", where_clause="created_date >= timestamp '"+date_str+"'", invert_where_clause="")
arcpy.CopyFeatures_management(WFS_PCA_PHOTOS_SELECTION, "WFS_PCA_PHOTOS_SELECTION")

WFS_PCA_Photos_result_int = arcpy.GetCount_management("WFS_PCA_PHOTOS_SELECTION")
WFS_PCA_Photos_result = str(arcpy.GetCount_management("WFS_PCA_PHOTOS_SELECTION"))
arcpy.AddMessage("The selection has " + WFS_PCA_Photos_result + " features")

SDE_PCA_Photos_current_int = int(arcpy.GetCount_management(PCA_Photos).getOutput(0))
SDE_PCA_Photos_current = str(arcpy.GetCount_management(PCA_Photos))

# Process: Feature Class to Feature Class
arcpy.AddMessage("Create Temporary PCA Photos feature class based on selection")
arcpy.FeatureClassToFeatureClass_conversion(in_features="WFS_PCA_PHOTOS_SELECTION", out_path=arcpy.env.workspace, out_name="TEMP_PCA_Photos", where_clause="", field_mapping=r"ASSETID 'ASSET ID' true true false 50 Text 0 0,First,#,PCA_Collector_WFS\PCA Photos,ASSETID,0,50;COMMENT 'COMMENT' true true false 50 Text 0 0,First,#,PCA_Collector_WFS\PCA Photos,COMMENT,0,50;created_user 'created_user' false true false 255 Text 0 0,First,#,PCA_Collector_WFS\PCA Photos,created_user,0,255;created_date 'created_date' false true false 8 Date 0 0,First,#,PCA_Collector_WFS\PCA Photos,created_date,-1,-1;last_edited_user 'last_edited_user' false true false 255 Text 0 0,First,#,PCA_Collector_WFS\PCA Photos,last_edited_user,0,255;last_edited_date 'last_edited_date' false true false 8 Date 0 0,First,#,PCA_Collector_WFS\PCA Photos,last_edited_date,-1,-1;GlobalID 'GlobalID' false false false 38 GlobalID 0 0,First,#,PCA_Collector_WFS\PCA Photos,GlobalID,-1,-1", config_keyword="")

# Process: Append
arcpy.AddMessage("Append to SDE PCA Photos")
arcpy.Append_management(inputs=TEMP_PCA_Photos, target=PCA_Photos, schema_type="NO_TEST", field_mapping=r"ASSETID 'ASSET ID' true true false 50 Text 0 0,First,#,C:\Users\temp\PCA_DATA.gdb\TEMP_PCA_Photos,ASSETID,0,50;COMMENT 'COMMENT' true true false 50 Text 0 0,First,#,C:\Users\temp\PCA_DATA.gdb\TEMP_PCA_Photos,COMMENT,0,50", subtype="", expression="")

SDE_PCA_Photos_post_count_int = int(arcpy.GetCount_management(PCA_Photos).getOutput(0))
SDE_PCA_Photos_post_count = str(arcpy.GetCount_management(PCA_Photos))

overall_diff_count = SDE_PCA_Photos_post_count_int -SDE_PCA_Photos_current_int
overall_diff_count_str = str(overall_diff_count)
if overall_diff_count == 1:
    arcpy.AddMessage(overall_diff_count_str + " feature was imported into PCA Photos")
else:
    arcpy.AddMessage(overall_diff_count_str + " features were imported into PCA Photos")

# Process: Delete (2)
arcpy.AddMessage("Deleted Temporary PCA Photos feature class")
arcpy.Delete_management(in_data=TEMP_PCA_Photos, data_type="")
arcpy.Delete_management("SDE_PCA_PHOTOS_copy")
arcpy.Delete_management("WFS_PCA_PHOTOS_copy")



