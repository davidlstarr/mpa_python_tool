#---------------------------------------------------#
#--------Step 3-Update PCA Polygons PCA WFS---------#
#---------------------------------------------------#

import arcpy
import json

# Script parameters
arcpy.env.workspace = arcpy.GetParameterAsText(0)
SDE_CONNECTION = arcpy.GetParameterAsText(1)

workspace_split = arcpy.env.workspace[:46]

#Make sure to drop the config file in your ArcPro project
with open(workspace_split+'/config.json') as json_data_file:
    data = json.load(json_data_file)

#Web Feature Service Paths:
WFS_paver_path = data["wfs_paths"]["WFS_paver_path"]
WFS_concrete_path = data["wfs_paths"]["WFS_concrete_path"]
WFS_asphalt_path = data["wfs_paths"]["WFS_asphalt_path"]
WFS_other_type_path = data["wfs_paths"]["WFS_other_type_path"]
WFS_PCA_PHOTOS = data["wfs_paths"]["WFS_PCA_PHOTOS"]
WFS_Pavement_Assessment_Areas = data["wfs_paths"]["WFS_Pavement_Assessment_Areas"]
WFS_Historic_Assessment_points = data["wfs_paths"]["WFS_Historic_Assessment_points"]

#Temporary Paths
TEMP_PAVERS_PCA = data["temp_paths"]["TEMP_PAVERS_PCA"]
TEMP_CONCRETE_PCA = data["temp_paths"]["TEMP_CONCRETE_PCA"]
TEMP_ASPHALT_PCA = data["temp_paths"]["TEMP_ASPHALT_PCA"]
TEMP_OTHER_PCA = data["temp_paths"]["TEMP_OTHER_PCA"]

PAVERS_PCA_Updates = data["temp_paths"]["PAVERS_PCA_Updates"]
CONCRETE_PCA_Updates = data["temp_paths"]["CONCRETE_PCA_Updates"]
ASPHALT_PCA_Updates = data["temp_paths"]["ASPHALT_PCA_Updates"]
OTHER_PCA_Updates = data["temp_paths"]["OTHER_PCA_Updates"]

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

arcpy.AddMessage("Update PCA Polygons PCA WFS")

#local variables

MPA_USER_PCA_POLYGONS = SDE_CONNECTION + "/MPA_USER.Pavement/PCA_POLYGONS"
Updated_record = "Updated_record"

temp_layers = "'" + TEMP_PAVERS_PCA + "';'" + TEMP_CONCRETE_PCA + "';'" + TEMP_ASPHALT_PCA + "';'" + TEMP_OTHER_PCA + "'"

arcpy.Delete_management(Updated_record)
arcpy.Delete_management("WFS_PCA_POLYGON_SELECTION")
arcpy.Delete_management("WFS_PCA_POLYGON_JOIN")
arcpy.Delete_management("WFS_Pavement_Assessment_Areas_copy")
arcpy.Delete_management("WFS_Historic_Assessment_points_copy")

# Process: Merge
arcpy.Merge_management(inputs=temp_layers, output=Updated_record, field_mappings=r"ASPHALT_CRACKING 'Asphalt Cracking' true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,ASPHALT_CRACKING,-1,-1;ASPHALT_RUTTING 'Asphalt Rutting' true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,ASPHALT_RUTTING,-1,-1;ASPHALT_PATCHES 'Asphalt Patches' true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,ASPHALT_PATCHES,-1,-1;ASPHALT_POTHOLES_RAVELING 'Asphalt Potholes and Raveling' true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,ASPHALT_POTHOLES_RAVELING,-1,-1;ASSESSMENT_COMMENTS 'Assessment Comments' true true false 1000 Text 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Paver Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Concrete Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Other Type of Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000;GLOBALID 'GlobalID' false false false 38 GlobalID 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,GLOBALID,-1,-1,Local Datasets\Paver Condition Assessment,GlobalID,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,GlobalID,-1,-1,Local Datasets\Other Type of Pavement Condition Assessment,GlobalID,-1,-1;CREATED_USER 'created_user' false true false 255 Text 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Paver Condition Assessment,CREATED_USER,0,255,Local Datasets\Concrete Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_USER,0,255;CREATED_DATE 'created_date' false true false 8 Date 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_DATE,-1,-1;LAST_EDITED_USER 'last_edited_user' false true false 255 Text 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Paver Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Concrete Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Other Type of Pavement Condition Assessment,LAST_EDITED_USER,0,255;LAST_EDITED_DATE 'last_edited_date' false true false 8 Date 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Other Type of Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1;RELATED_ASSETID 'RELATED_ASSETID' true true false 50 Text 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,RELATED_ASSETID,0,50,Local Datasets\Paver Condition Assessment,RELATED_ASSETID,0,50,Local Datasets\Concrete Pavement Condition Assessment,RELATED_ASSETID,0,50;POINTID 'POINTID' true true false 4 Long 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,POINTID,-1,-1,Local Datasets\Paver Condition Assessment,POINTID,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,POINTID,-1,-1;CONDITION 'CONDITION' true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,CONDITION,-1,-1,Local Datasets\Paver Condition Assessment,CONDITION,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CONDITION,-1,-1;MATERIAL 'MATERIAL' true true false 50 Text 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Paver Condition Assessment,MATERIAL,0,50,Local Datasets\Concrete Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Other Type of Pavement Condition Assessment,MATERIAL,0,50;PAVERS_OVERALL 'Pavers Overall' true true false 2 Short 0 0,First,#,Local Datasets\Paver Condition Assessment,PAVERS_OVERALL,-1,-1;PAVERS_PATCHES 'Pavers Patches' true true false 2 Short 0 0,First,#,Local Datasets\Paver Condition Assessment,PAVERS_PATCHES,-1,-1;PAVERS_PUMPING 'Pavers Pumping' true true false 2 Short 0 0,First,#,Local Datasets\Paver Condition Assessment,PAVERS_PUMPING,-1,-1;PAVERS_RUTTING 'Pavers Rutting' true true false 2 Short 0 0,First,#,Local Datasets\Paver Condition Assessment,PAVERS_RUTTING,-1,-1;PAVERS_JOINT_MATERIAL 'Pavers Joint Material' true true false 2 Short 0 0,First,#,Local Datasets\Paver Condition Assessment,PAVERS_JOINT_MATERIAL,-1,-1;CONCRETE_CRACKING 'Concrete Cracking' true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_CRACKING,-1,-1;CONCRETE_DCRACKING 'Concrete D Cracking' true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_DCRACKING,-1,-1;CONCRETE_MIDSLAB_CRACKING 'Concrete Mid-slab Cracking' true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_MIDSLAB_CRACKING,-1,-1;CONCRETE_SPALLING 'Concrete Spalling' true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_SPALLING,-1,-1;CONCRETE_PATCHES 'Concrete Patches' true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_PATCHES,-1,-1;CONCRETE_PUMPING 'Concrete Pumping' true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_PUMPING,-1,-1", add_source="NO_SOURCE_INFO")
# Get the count from Updated Record Layer Path
updated_record_feature_count = int(arcpy.GetCount_management(Updated_record).getOutput(0))

if updated_record_feature_count == 0:
    arcpy.AddError("The Temp Updated Record layer has not been created. Please ensure your inputs are correct.")
else:
    arcpy.AddMessage("The Temp Updated Record layer has been created")


# Execute FeatureClassToFeatureClass
arcpy.FeatureClassToFeatureClass_conversion(in_features=WFS_Pavement_Assessment_Areas, out_path=arcpy.env.workspace, out_name="WFS_Pavement_Assessment_Areas_copy",where_clause="", field_mapping="", config_keyword="")
arcpy.FeatureClassToFeatureClass_conversion(in_features=WFS_Historic_Assessment_points, out_path=arcpy.env.workspace, out_name="WFS_Historic_Assessment_points_copy",where_clause="", field_mapping="", config_keyword="")

# Process: Select Layer By Location
arcpy.AddMessage("Select by location where updated_record features intersect PCA Polygons")
WFS_PCA_POLYGON_SELECTION = arcpy.SelectLayerByLocation_management(in_layer=MPA_USER_PCA_POLYGONS, overlap_type="INTERSECT", select_features=Updated_record, search_distance="", selection_type="NEW_SELECTION", invert_spatial_relationship="NOT_INVERT")

# Copy the layer to a new permanent feature class
arcpy.CopyFeatures_management(WFS_PCA_POLYGON_SELECTION, "WFS_PCA_POLYGON_SELECTION")

# Process: Add Join
arcpy.AddMessage("Joining WFS Pavement Assessment Area with PCA Polygons")
join = arcpy.AddJoin_management(in_layer_or_view=WFS_Pavement_Assessment_Areas, in_field="ASSETID", join_table=MPA_USER_PCA_POLYGONS, join_field="ASSETID", join_type="KEEP_ALL")

# Copy the layer to a new permanent feature class
arcpy.CopyFeatures_management(join, "WFS_PCA_POLYGON_JOIN")

# Process: Calculate Field
arcpy.AddMessage("Condition Field Calculation")
arcpy.CalculateField_management(in_table=join, field="L5Pavement_Assessment_Areas.CONDITION", expression="!MPA_USER.PCA_POLYGONS.CONDITION!", expression_type="PYTHON3", code_block="")

# Process: Calculate Field (2)
arcpy.AddMessage("Condition Date Field Calculation")
arcpy.CalculateField_management(in_table=join, field="L5Pavement_Assessment_Areas.COND_DATE", expression="!MPA_USER.PCA_POLYGONS.LAST_EDITED_DATE!", expression_type="PYTHON3", code_block="")

# Process: Calculate Field (3)
arcpy.AddMessage("Material Field Calculation")
arcpy.CalculateField_management(in_table=join, field="L5Pavement_Assessment_Areas.MATERIAL", expression="!MPA_USER.PCA_POLYGONS.MATERIAL!", expression_type="PYTHON3", code_block="")

# Process: Calculate Field (4)
arcpy.AddMessage("Assessor Field Calculation")
arcpy.CalculateField_management(in_table=join, field="L5Pavement_Assessment_Areas.ASSESSOR", expression="!MPA_USER.PCA_POLYGONS.LAST_EDITED_USER!", expression_type="PYTHON3", code_block="")

# Process: Calculate Field (5)
arcpy.AddMessage("Assessor Comments Field Calculation")
arcpy.CalculateField_management(in_table=join, field="L5Pavement_Assessment_Areas.ASSESSMENT_COMMENTS", expression="!MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS!", expression_type="PYTHON3", code_block="")

temp_layers = "'" + TEMP_PAVERS_PCA + "';'" + TEMP_CONCRETE_PCA + "';'" + TEMP_ASPHALT_PCA + "';'" + TEMP_OTHER_PCA + "'"
# Process: Append
arcpy.AddMessage("Update WFS Historic Assessment Areas")
#arcpy.Append_management(inputs=temp_layers, target=WFS_Historic_Assessment_points, schema_type="NO_TEST", field_mapping=r"AREASQYD 'AREA SQUARE YARDS' true true false 0 Double 0 0,First,#;AREASQFT 'AREA SQUARE FEET' true true false 0 Double 0 0,First,#;MATERIAL 'MATERIAL' true true false 50 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Asphalt Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Concrete Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Paver Condition Assessment,MATERIAL,0,50;LOCATION 'LOCATION' true true false 50 Text 0 0,First,#;USE_ 'USE' true true false 50 Text 0 0,First,#;USE_CUST 'USE CUSTOMER' true true false 50 Text 0 0,First,#;LEASED 'LEASED' true true false 50 Text 0 0,First,#;MAIN_RESP 'MAINTENANCE RESPONSIBILITY' true true false 50 Text 0 0,First,#;CONDITION 'CONDITION' true true false 0 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,CONDITION,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CONDITION,-1,-1,Local Datasets\Paver Condition Assessment,CONDITION,-1,-1;COND_DATE 'COND_DATE' true true false 8 Date 0 0,First,#;TYPE 'TYPE' true true false 50 Text 0 0,First,#;TERMINAL 'TERMINAL' true true false 15 Text 0 0,First,#;ASSETID 'ASSET ID' true true false 50 Text 0 0,First,#;ASSESSOR 'ASSESSOR' true true false 50 Text 0 0,First,#;ASSESSMENT_COMMENTS 'ASSESSMENT_COMMENTS' true true false 1000 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Asphalt Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Concrete Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Paver Condition Assessment,ASSESSMENT_COMMENTS,0,1000;GLOBALID 'GLOBALID' false false false 38 GlobalID 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,GlobalID,-1,-1,Local Datasets\Asphalt Pavement Condition Assessment,GLOBALID,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,GlobalID,-1,-1,Local Datasets\Paver Condition Assessment,GlobalID,-1,-1;AREAACRES 'AREAACRES' true true false 0 Double 0 0,First,#;created_user 'created_user' true true false 255 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Concrete Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Paver Condition Assessment,CREATED_USER,0,255;created_date 'created_date' true true false 8 Date 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,CREATED_DATE,-1,-1;last_edited_user 'last_edited_user' true true false 255 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Asphalt Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Concrete Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Paver Condition Assessment,LAST_EDITED_USER,0,255;last_edited_date 'last_edited_date' true true false 8 Date 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Asphalt Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,LAST_EDITED_DATE,-1,-1", subtype="", expression="")

# Process: Delete
arcpy.AddMessage("Delete Updated_record layer")
arcpy.Delete_management(in_data=Updated_record, data_type="")



# Process: Remove Join
#arcpy.AddMessage("Remove Join of WFS Pavement Assessment Area with PCA Polygons")
#arcpy.RemoveJoin_management(in_layer_or_view=WFS_Pavement_Assessment_Areas, join_name=MPA_USER_PCA_POLYGONS)

# # Write messages to a Text File
# txtFile = open("c:\\temp\\GPMessages.txt", "w")
# txtFile.write(sel_message)
# txtFile.write(arcpy.GetMessages())
# txtFile.close()

arcpy.AddWarning("If no errors, you can move on to Step 3b.")
