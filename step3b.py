#---------------------------------------------------------------------#
#--------Step 3b-Update Historic Condition Assessment Records---------#
#---------------------------------------------------------------------#

import arcpy
import json

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

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

arcpy.AddMessage("Update Historic Condition Assessment Records")
arcpy.AddMessage("Update Historic_Pavement_Assessments Table")

# Local variables:
Historic_Pavement_Conditions = SDE_CONNECTION + "/MPA_USER.Historic_Pavement_Assessments"
MPA_USER_PCA_POLYGONS = SDE_CONNECTION + "/MPA_USER.Pavement/PCA_POLYGONS"
Table_Name = "PCA_POLYGONS_View"

arcpy.Delete_management("Historic_Pavement_Assessments_copy")
arcpy.Delete_management("TEMP_PAVERS_PCA_SELECTION")
arcpy.Delete_management("TEMP_CONCRETE_PCA_SELECTION")
arcpy.Delete_management("TEMP_ASPHALT_PCA_SELECTION")
arcpy.Delete_management("TEMP_OTHER_PCA_SELECTION")
arcpy.Delete_management("merged_PCA_Polygons")

#copying Historic Pavement Assessments
arcpy.TableToTable_conversion(in_rows=Historic_Pavement_Conditions, out_path=arcpy.env.workspace, out_name="Historic_Pavement_Assessments_copy", where_clause="", field_mapping="AREASQYD 'AREA SQUARE YARDS' true true false 8 Double 8 38,First,#,PCA_POLYGONS_View,AREASQYD,-1,-1;AREASQFT 'AREA SQUARE FEET' true true false 8 Double 8 38,First,#,PCA_POLYGONS_View,AREASQFT,-1,-1;MATERIAL 'MATERIAL' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,MATERIAL,0,50;LOCATION 'LOCATION' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,LOCATION,0,50;USE_ 'USE' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,USE_,0,50;USE_CUST 'USE CUSTOMER' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,USE_CUST,0,50;LEASED 'LEASED' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,LEASED,0,50;MAIN_RESP 'MAINTENANCE RESPONSIBILITY' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,MAIN_RESP,0,50;CONDITION 'CONDITION' true true false 2 Short 0 5,First,#,PCA_POLYGONS_View,CONDITION,-1,-1;COND_DATE 'COND_DATE' true true false 8 Date 0 0,First,#,PCA_POLYGONS_View,COND_DATE,-1,-1;TYPE 'TYPE' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,TYPE,0,50;TERMINAL 'TERMINAL' true true false 15 Text 0 0,First,#,PCA_POLYGONS_View,TERMINAL,0,15;ASSETID 'ASSET ID' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,ASSETID,0,50;ASSESSOR 'ASSESSOR' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,ASSESSOR,0,50;GLOBALID 'GLOBALID' false false false 38 GlobalID 0 0,First,#,PCA_POLYGONS_View,GLOBALID,-1,-1;AREAACRES 'AREAACRES' true true false 8 Double 8 38,First,#,PCA_POLYGONS_View,AREAACRES,-1,-1;CREATED_USER 'CREATED_USER' true true false 255 Text 0 0,First,#,PCA_POLYGONS_View,CREATED_USER,0,255;CREATED_DATE 'CREATED_DATE' true true false 8 Date 0 0,First,#,PCA_POLYGONS_View,CREATED_DATE,-1,-1;LAST_EDITED_USER 'LAST_EDITED_USER' true true false 255 Text 0 0,First,#,PCA_POLYGONS_View,LAST_EDITED_USER,0,255;LAST_EDITED_DATE 'LAST_EDITED_DATE' true true false 8 Date 0 0,First,#,PCA_POLYGONS_View,LAST_EDITED_DATE,-1,-1;COND_LABEL 'COND_LABEL' true true false 10 Text 0 0,First,#,PCA_POLYGONS_View,COND_LABEL,0,10;SHAPE_AREA 'SHAPE.AREA' true false false 8 Double 8 38,First,#;SHAPE_LEN 'SHAPE.LEN' true false false 8 Double 8 38,First,#;ASSESSMENT_COMMENTS 'ASSESSMENT_COMMENTS' true true false 500 Text 0 0,First,#,PCA_POLYGONS_View,ASSESSMENT_COMMENTS,0,1000", config_keyword="")

temp_layers_path = [TEMP_PAVERS_PCA, TEMP_CONCRETE_PCA, TEMP_ASPHALT_PCA, TEMP_OTHER_PCA]
temp_copy_layers_array =["TEMP_PAVERS_PCA_SELECTION", "TEMP_CONCRETE_PCA_SELECTION", "TEMP_ASPHALT_PCA_SELECTION", "TEMP_OTHER_PCA_SELECTION"]
temp_layer_message = ["Select by location Temp Pavers layers with PCA Polygons","Select by location Temp Concrete layers with PCA Polygons","Select by location Temp Asphalt layers with PCA Polygons","Select by location Temp Other layers with PCA Polygons"]
for temp_layers, temp_message, temp_copy_layers in zip(temp_layers_path, temp_layer_message, temp_copy_layers_array):
    arcpy.AddMessage(temp_message)
    TEMP_PCA_SELECTION = arcpy.SelectLayerByLocation_management(in_layer=MPA_USER_PCA_POLYGONS,overlap_type="INTERSECT",select_features=temp_layers,search_distance="",selection_type="ADD_TO_SELECTION",invert_spatial_relationship="NOT_INVERT")
    arcpy.CopyFeatures_management(TEMP_PCA_SELECTION, temp_copy_layers)

# Process: Merge
arcpy.Merge_management(inputs="TEMP_PAVERS_PCA_SELECTION;TEMP_CONCRETE_PCA_SELECTION;TEMP_ASPHALT_PCA_SELECTION;TEMP_OTHER_PCA_SELECTION", output="merged_PCA_Polygons", field_mappings="", add_source="NO_SOURCE_INFO")

# Process: Make Table View
arcpy.AddMessage("Make table view based on selection")
table = arcpy.MakeTableView_management(in_table="merged_PCA_Polygons", out_view=Table_Name, where_clause="", workspace="", field_info="OBJECTID OBJECTID VISIBLE NONE;AREASQYD AREASQYD VISIBLE NONE;AREASQFT AREASQFT VISIBLE NONE;MATERIAL MATERIAL VISIBLE NONE;LOCATION LOCATION VISIBLE NONE;USE_ USE_ VISIBLE NONE;USE_CUST USE_CUST VISIBLE NONE;LEASED LEASED VISIBLE NONE;MAIN_RESP MAIN_RESP VISIBLE NONE;CONDITION CONDITION VISIBLE NONE;COND_DATE COND_DATE VISIBLE NONE;TYPE TYPE VISIBLE NONE;TERMINAL TERMINAL VISIBLE NONE;ASSETID ASSETID VISIBLE NONE;ASSESSOR ASSESSOR VISIBLE NONE;ASSESSMENT_COMMENTS ASSESSMENT_COMMENTS VISIBLE NONE;GLOBALID GLOBALID VISIBLE NONE;AREAACRES AREAACRES VISIBLE NONE;CREATED_USER CREATED_USER VISIBLE NONE;CREATED_DATE CREATED_DATE VISIBLE NONE;LAST_EDITED_USER LAST_EDITED_USER VISIBLE NONE;LAST_EDITED_DATE LAST_EDITED_DATE VISIBLE NONE;COND_LABEL COND_LABEL VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.AREA SHAPE.AREA VISIBLE NONE;SHAPE.LEN SHAPE.LEN VISIBLE NONE")
arcpy.AddMessage(table)

message = int(arcpy.GetCount_management(Table_Name).getOutput(0))

if message == 0:
        arcpy.AddWarning(" has no features.".format(Table_Name))
else:
        arcpy.AddMessage(
            "exported {1} features.".format(Table_Name, message))

# Process: Append
arcpy.AddMessage("Append Table view to Historic Pavement Conditions")
arcpy.Append_management(inputs="PCA_POLYGONS_View", target=Historic_Pavement_Conditions, schema_type="NO_TEST", field_mapping="AREASQYD 'AREA SQUARE YARDS' true true false 8 Double 8 38,First,#,PCA_POLYGONS_View,AREASQYD,-1,-1;AREASQFT 'AREA SQUARE FEET' true true false 8 Double 8 38,First,#,PCA_POLYGONS_View,AREASQFT,-1,-1;MATERIAL 'MATERIAL' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,MATERIAL,0,50;LOCATION 'LOCATION' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,LOCATION,0,50;USE_ 'USE' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,USE_,0,50;USE_CUST 'USE CUSTOMER' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,USE_CUST,0,50;LEASED 'LEASED' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,LEASED,0,50;MAIN_RESP 'MAINTENANCE RESPONSIBILITY' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,MAIN_RESP,0,50;CONDITION 'CONDITION' true true false 2 Short 0 5,First,#,PCA_POLYGONS_View,CONDITION,-1,-1;COND_DATE 'COND_DATE' true true false 8 Date 0 0,First,#,PCA_POLYGONS_View,COND_DATE,-1,-1;TYPE 'TYPE' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,TYPE,0,50;TERMINAL 'TERMINAL' true true false 15 Text 0 0,First,#,PCA_POLYGONS_View,TERMINAL,0,15;ASSETID 'ASSET ID' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,ASSETID,0,50;ASSESSOR 'ASSESSOR' true true false 50 Text 0 0,First,#,PCA_POLYGONS_View,ASSESSOR,0,50;GLOBALID 'GLOBALID' false false false 38 GlobalID 0 0,First,#,PCA_POLYGONS_View,GLOBALID,-1,-1;AREAACRES 'AREAACRES' true true false 8 Double 8 38,First,#,PCA_POLYGONS_View,AREAACRES,-1,-1;CREATED_USER 'CREATED_USER' true true false 255 Text 0 0,First,#,PCA_POLYGONS_View,CREATED_USER,0,255;CREATED_DATE 'CREATED_DATE' true true false 8 Date 0 0,First,#,PCA_POLYGONS_View,CREATED_DATE,-1,-1;LAST_EDITED_USER 'LAST_EDITED_USER' true true false 255 Text 0 0,First,#,PCA_POLYGONS_View,LAST_EDITED_USER,0,255;LAST_EDITED_DATE 'LAST_EDITED_DATE' true true false 8 Date 0 0,First,#,PCA_POLYGONS_View,LAST_EDITED_DATE,-1,-1;COND_LABEL 'COND_LABEL' true true false 10 Text 0 0,First,#,PCA_POLYGONS_View,COND_LABEL,0,10;SHAPE_AREA 'SHAPE.AREA' true false false 8 Double 8 38,First,#;SHAPE_LEN 'SHAPE.LEN' true false false 8 Double 8 38,First,#;ASSESSMENT_COMMENTS 'ASSESSMENT_COMMENTS' true true false 500 Text 0 0,First,#,PCA_POLYGONS_View,ASSESSMENT_COMMENTS,0,1000", subtype="", expression="")

# Write messages to a Text File
# txtFile = open("c:\\temp\\GPMessages.txt", "w")
# txtFile.write(arcpy.GetMessages())
# txtFile.close()

arcpy.AddWarning("If no errors, you can move on to Step 3c. Before moving to Step 3c please make sure to remove all layers from your map.")