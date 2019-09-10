#-----------------------------------------------#
#--------Step 2-Update PCA Polygons GDB---------#
#-----------------------------------------------#

import arcpy
import json

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

#parameters
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

MPA_USER_PCA_POLYGONS = SDE_CONNECTION + "/MPA_USER.Pavement/PCA_POLYGONS"

arcpy.AddMessage("Update PCA Polygons GDB")

# Local variables:

PCA_POLYGONS_TEMP_LAYER = "PCA_POLYGONS_TEMP_LAYER"
MPA_USER_PCA_POLYGONS = SDE_CONNECTION + "/MPA_USER.Pavement/PCA_POLYGONS"

codeblock2 = """def Reclass(field):
  if field == 5:
    return "Good"
  elif field == 4:
    return "Good"
  elif field == 3:
    return "Fair"
  elif field == 2:
    return "Poor"
  elif field == 1:
    return "Poor"
    """

#------Update PCA Polygons------#

arcpy.AddMessage("Update PCA Polygons")

# Process: Make Feature Layer (3)
arcpy.MakeFeatureLayer_management(in_features=MPA_USER_PCA_POLYGONS, out_layer="PCA_POLYGONS_TEMP_LAYER_PAVER", where_clause="", workspace="", field_info="OBJECTID OBJECTID VISIBLE NONE;AREASQYD AREASQYD VISIBLE NONE;AREASQFT AREASQFT VISIBLE NONE;MATERIAL MATERIAL VISIBLE NONE;LOCATION LOCATION VISIBLE NONE;USE_ USE_ VISIBLE NONE;USE_CUST USE_CUST VISIBLE NONE;LEASED LEASED VISIBLE NONE;MAIN_RESP MAIN_RESP VISIBLE NONE;CONDITION CONDITION VISIBLE NONE;COND_DATE COND_DATE VISIBLE NONE;TYPE TYPE VISIBLE NONE;TERMINAL TERMINAL VISIBLE NONE;ASSETID ASSETID VISIBLE NONE;ASSESSOR ASSESSOR VISIBLE NONE;ASSESSMENT_COMMENTS ASSESSMENT_COMMENTS VISIBLE NONE;GLOBALID GLOBALID VISIBLE NONE;AREAACRES AREAACRES VISIBLE NONE;CREATED_USER CREATED_USER VISIBLE NONE;CREATED_DATE CREATED_DATE VISIBLE NONE;LAST_EDITED_USER LAST_EDITED_USER VISIBLE NONE;LAST_EDITED_DATE LAST_EDITED_DATE VISIBLE NONE;COND_LABEL COND_LABEL VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.AREA SHAPE.AREA VISIBLE NONE;SHAPE.LEN SHAPE.LEN VISIBLE NONE")
arcpy.MakeFeatureLayer_management(in_features=MPA_USER_PCA_POLYGONS, out_layer="PCA_POLYGONS_TEMP_LAYER_ASPHALT", where_clause="", workspace="", field_info="OBJECTID OBJECTID VISIBLE NONE;AREASQYD AREASQYD VISIBLE NONE;AREASQFT AREASQFT VISIBLE NONE;MATERIAL MATERIAL VISIBLE NONE;LOCATION LOCATION VISIBLE NONE;USE_ USE_ VISIBLE NONE;USE_CUST USE_CUST VISIBLE NONE;LEASED LEASED VISIBLE NONE;MAIN_RESP MAIN_RESP VISIBLE NONE;CONDITION CONDITION VISIBLE NONE;COND_DATE COND_DATE VISIBLE NONE;TYPE TYPE VISIBLE NONE;TERMINAL TERMINAL VISIBLE NONE;ASSETID ASSETID VISIBLE NONE;ASSESSOR ASSESSOR VISIBLE NONE;ASSESSMENT_COMMENTS ASSESSMENT_COMMENTS VISIBLE NONE;GLOBALID GLOBALID VISIBLE NONE;AREAACRES AREAACRES VISIBLE NONE;CREATED_USER CREATED_USER VISIBLE NONE;CREATED_DATE CREATED_DATE VISIBLE NONE;LAST_EDITED_USER LAST_EDITED_USER VISIBLE NONE;LAST_EDITED_DATE LAST_EDITED_DATE VISIBLE NONE;COND_LABEL COND_LABEL VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.AREA SHAPE.AREA VISIBLE NONE;SHAPE.LEN SHAPE.LEN VISIBLE NONE")
arcpy.MakeFeatureLayer_management(in_features=MPA_USER_PCA_POLYGONS, out_layer="PCA_POLYGONS_TEMP_LAYER_CONCRETE", where_clause="", workspace="", field_info="OBJECTID OBJECTID VISIBLE NONE;AREASQYD AREASQYD VISIBLE NONE;AREASQFT AREASQFT VISIBLE NONE;MATERIAL MATERIAL VISIBLE NONE;LOCATION LOCATION VISIBLE NONE;USE_ USE_ VISIBLE NONE;USE_CUST USE_CUST VISIBLE NONE;LEASED LEASED VISIBLE NONE;MAIN_RESP MAIN_RESP VISIBLE NONE;CONDITION CONDITION VISIBLE NONE;COND_DATE COND_DATE VISIBLE NONE;TYPE TYPE VISIBLE NONE;TERMINAL TERMINAL VISIBLE NONE;ASSETID ASSETID VISIBLE NONE;ASSESSOR ASSESSOR VISIBLE NONE;ASSESSMENT_COMMENTS ASSESSMENT_COMMENTS VISIBLE NONE;GLOBALID GLOBALID VISIBLE NONE;AREAACRES AREAACRES VISIBLE NONE;CREATED_USER CREATED_USER VISIBLE NONE;CREATED_DATE CREATED_DATE VISIBLE NONE;LAST_EDITED_USER LAST_EDITED_USER VISIBLE NONE;LAST_EDITED_DATE LAST_EDITED_DATE VISIBLE NONE;COND_LABEL COND_LABEL VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.AREA SHAPE.AREA VISIBLE NONE;SHAPE.LEN SHAPE.LEN VISIBLE NONE")
arcpy.MakeFeatureLayer_management(in_features=MPA_USER_PCA_POLYGONS, out_layer="PCA_POLYGONS_TEMP_LAYER_OTHER", where_clause="", workspace="", field_info="OBJECTID OBJECTID VISIBLE NONE;AREASQYD AREASQYD VISIBLE NONE;AREASQFT AREASQFT VISIBLE NONE;MATERIAL MATERIAL VISIBLE NONE;LOCATION LOCATION VISIBLE NONE;USE_ USE_ VISIBLE NONE;USE_CUST USE_CUST VISIBLE NONE;LEASED LEASED VISIBLE NONE;MAIN_RESP MAIN_RESP VISIBLE NONE;CONDITION CONDITION VISIBLE NONE;COND_DATE COND_DATE VISIBLE NONE;TYPE TYPE VISIBLE NONE;TERMINAL TERMINAL VISIBLE NONE;ASSETID ASSETID VISIBLE NONE;ASSESSOR ASSESSOR VISIBLE NONE;ASSESSMENT_COMMENTS ASSESSMENT_COMMENTS VISIBLE NONE;GLOBALID GLOBALID VISIBLE NONE;AREAACRES AREAACRES VISIBLE NONE;CREATED_USER CREATED_USER VISIBLE NONE;CREATED_DATE CREATED_DATE VISIBLE NONE;LAST_EDITED_USER LAST_EDITED_USER VISIBLE NONE;LAST_EDITED_DATE LAST_EDITED_DATE VISIBLE NONE;COND_LABEL COND_LABEL VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.AREA SHAPE.AREA VISIBLE NONE;SHAPE.LEN SHAPE.LEN VISIBLE NONE")

# Get the count from Temp PCA Polygon Layer Path
Temp_PCA_Polygon_feature_count = int(arcpy.GetCount_management("PCA_POLYGONS_TEMP_LAYER_PAVER").getOutput(0))

if Temp_PCA_Polygon_feature_count == 0:
    arcpy.AddError("The Temporary PCA Polygon layer has not been created. Please ensure your inputs are correct.")
else:
    arcpy.AddMessage("The Temporary PCA Polygon layer has been created")


# pca_update_layers_list = [PAVERS_PCA_Updates, CONCRETE_PCA_Updates, ASPHALT_PCA_Updates]
# make_feature_layer_list =["PCA_POLYGONS_TEMP_LAYER_PAVER", "PCA_POLYGONS_TEMP_LAYER_ASPHALT", "PCA_POLYGONS_TEMP_LAYER_CONCRETE"]
# # Process: Add Join (3)
# for pca_update_layers, make_feature_layer in zip(pca_update_layers_list, make_feature_layer_list):
#     arcpy.AddJoin_management(in_layer_or_view=make_feature_layer, in_field="ASSETID", join_table=pca_update_layers, join_field="ASSETID", join_type="KEEP_COMMON")
#
#  # Field Calculations on PCA Polygons
# pca_update_layers_list2 = ["!PAVERS_PCA_Updates", "!CONCRETE_PCA_Updates", "!ASPHALT_PCA_Updates"]
#
# #NEED TO DETERMINE HOW "OTHER_PCA_UPDATES" ARE HANDLED!!!!!!
#
# field_array = ["MPA_USER.PCA_POLYGONS.COND_DATE", "MPA_USER.PCA_POLYGONS.MATERIAL", "MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS", "MPA_USER.PCA_POLYGONS.ASSESSOR", "MPA_USER.PCA_POLYGONS.CONDITION"]
#
# for pca_update_layers in pca_update_layers_list2:
#      exp_array = [pca_update_layers + ".LAST_EDITED_DATE_1!", pca_update_layers + ".MATERIAL_1!", pca_update_layers + ".ASSESSMENT_COMMENTS_1!", pca_update_layers + ".LAST_EDITED_USER_1!", pca_update_layers + ".CONDITION_1!"]
#
# for field, expression, make_feature_layer in zip(field_array, exp_array, make_feature_layer_list):
#     arcpy.CalculateField_management(in_table=make_feature_layer, field=field, expression=expression, expression_type="PYTHON_9.3",code_block="")
#     arcpy.AddMessage(field)
#     arcpy.AddMessage(expression)
#     arcpy.CalculateField_management(in_table=make_feature_layer, field="COND_LABEL", expression="Reclass(!MPA_USER.PCA_POLYGONS.CONDITION!)", expression_type="PYTHON3", code_block=codeblock2)

##Paver Calculations##

arcpy.AddMessage("Field Calculations for Pavers")

# Process: Add Join (3)
arcpy.AddJoin_management(in_layer_or_view="PCA_POLYGONS_TEMP_LAYER_PAVER", in_field="ASSETID", join_table=PAVERS_PCA_Updates, join_field="ASSETID", join_type="KEEP_COMMON")

# Process: Paver Calc Date
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_PAVER", field="MPA_USER.PCA_POLYGONS.COND_DATE", expression="!PAVERS_PCA_Updates.LAST_EDITED_DATE_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Material
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_PAVER", field="MPA_USER.PCA_POLYGONS.MATERIAL", expression="!PAVERS_PCA_Updates.MATERIAL_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Assessment
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_PAVER", field="MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS", expression="!PAVERS_PCA_Updates.ASSESSMENT_COMMENTS_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Editor
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_PAVER", field="MPA_USER.PCA_POLYGONS.ASSESSOR", expression="!PAVERS_PCA_Updates.LAST_EDITED_USER_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Cond
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_PAVER", field="MPA_USER.PCA_POLYGONS.CONDITION", expression="!PAVERS_PCA_Updates.CONDITION_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Calculate Field
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_PAVER", field="COND_LABEL", expression="Reclass(!MPA_USER.PCA_POLYGONS.CONDITION!)", expression_type="PYTHON3", code_block=codeblock2)

##Asphalt Calculations##

arcpy.AddMessage("Field Calculations for Asphalt")

# Process: Add Join (3)
arcpy.AddJoin_management(in_layer_or_view="PCA_POLYGONS_TEMP_LAYER_ASPHALT", in_field="ASSETID", join_table=ASPHALT_PCA_Updates, join_field="ASSETID", join_type="KEEP_COMMON")

# Process: Paver Calc Date
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_ASPHALT", field="MPA_USER.PCA_POLYGONS.COND_DATE", expression="!ASPHALT_PCA_Updates.LAST_EDITED_DATE_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Material
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_ASPHALT", field="MPA_USER.PCA_POLYGONS.MATERIAL", expression="!ASPHALT_PCA_Updates.MATERIAL_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Assessment
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_ASPHALT", field="MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS", expression="!ASPHALT_PCA_Updates.ASSESSMENT_COMMENTS_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Editor'
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_ASPHALT", field="MPA_USER.PCA_POLYGONS.ASSESSOR", expression="!ASPHALT_PCA_Updates.LAST_EDITED_USER_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Cond
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_ASPHALT", field="MPA_USER.PCA_POLYGONS.CONDITION", expression="!ASPHALT_PCA_Updates.CONDITION_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Calculate Field
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_ASPHALT", field="COND_LABEL", expression="Reclass(!MPA_USER.PCA_POLYGONS.CONDITION!)", expression_type="PYTHON3", code_block=codeblock2)

##Concrete Calculations##

arcpy.AddMessage("Field Calculations for Concrete")

# Process: Add Join (3)
arcpy.AddJoin_management(in_layer_or_view="PCA_POLYGONS_TEMP_LAYER_CONCRETE", in_field="ASSETID", join_table=CONCRETE_PCA_Updates, join_field="ASSETID", join_type="KEEP_COMMON")

# Process: Paver Calc Date
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_CONCRETE", field="MPA_USER.PCA_POLYGONS.COND_DATE", expression="!CONCRETE_PCA_Updates.LAST_EDITED_DATE_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Material
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_CONCRETE", field="MPA_USER.PCA_POLYGONS.MATERIAL", expression="!CONCRETE_PCA_Updates.MATERIAL_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Assessment
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_CONCRETE", field="MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS", expression="!CONCRETE_PCA_Updates.ASSESSMENT_COMMENTS_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Editor
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_CONCRETE", field="MPA_USER.PCA_POLYGONS.ASSESSOR", expression="!CONCRETE_PCA_Updates.LAST_EDITED_USER_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Cond
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_CONCRETE", field="MPA_USER.PCA_POLYGONS.CONDITION", expression="!CONCRETE_PCA_Updates.CONDITION_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Calculate Field
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_CONCRETE", field="COND_LABEL", expression="Reclass(!MPA_USER.PCA_POLYGONS.CONDITION!)", expression_type="PYTHON3", code_block=codeblock2)

##Other Calculations##

arcpy.AddMessage("Field Calculations for Other")

# Process: Add Join (3)
arcpy.AddJoin_management(in_layer_or_view="PCA_POLYGONS_TEMP_LAYER_OTHER", in_field="ASSETID", join_table=OTHER_PCA_Updates, join_field="ASSETID", join_type="KEEP_COMMON")

# Process: Paver Calc Date
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_OTHER", field="MPA_USER.PCA_POLYGONS.COND_DATE", expression="!OTHER_PCA_Updates.LAST_EDITED_DATE_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Material
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_OTHER", field="MPA_USER.PCA_POLYGONS.MATERIAL", expression="!OTHER_PCA_Updates.MATERIAL_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Assessment
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_OTHER", field="MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS", expression="!OTHER_PCA_Updates.ASSESSMENT_COMMENTS_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Editor
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_OTHER", field="MPA_USER.PCA_POLYGONS.ASSESSOR", expression="!OTHER_PCA_Updates.LAST_EDITED_USER_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Calculate Field
arcpy.CalculateField_management(in_table="PCA_POLYGONS_TEMP_LAYER_OTHER", field="COND_LABEL", expression="Reclass(!MPA_USER.PCA_POLYGONS.CONDITION!)", expression_type="PYTHON3", code_block=codeblock2)



Temp_PCA_Polygon_paver_feature_count = int(arcpy.GetCount_management("PCA_POLYGONS_TEMP_LAYER_PAVER").getOutput(0))

if Temp_PCA_Polygon_paver_feature_count == 0:
    arcpy.AddMessage("No Paver features imported")
else:
    arcpy.AddMessage(
        "Updated {1} paver features in PCA Polygons".format("PCA_POLYGONS_TEMP_LAYER_PAVER", Temp_PCA_Polygon_paver_feature_count))

Temp_PCA_Polygon_concrete_feature_count = int(arcpy.GetCount_management("PCA_POLYGONS_TEMP_LAYER_CONCRETE").getOutput(0))
if Temp_PCA_Polygon_concrete_feature_count == 0:
    arcpy.AddMessage("No Concrete features imported")
else:
    arcpy.AddMessage(
        "Updated {1} concrete features in PCA Polygons".format("PCA_POLYGONS_TEMP_LAYER_CONCRETE", Temp_PCA_Polygon_concrete_feature_count))

Temp_PCA_Polygon_asphalt_feature_count = int(arcpy.GetCount_management("PCA_POLYGONS_TEMP_LAYER_ASPHALT").getOutput(0))
if Temp_PCA_Polygon_asphalt_feature_count == 0:
    arcpy.AddMessage("No Asphalt features imported")
else:
    arcpy.AddMessage(
        "Updated {1} asphalt features in PCA Polygons".format("PCA_POLYGONS_TEMP_LAYER_ASPHALT", Temp_PCA_Polygon_asphalt_feature_count))

Temp_PCA_Polygon_other_feature_count = int(arcpy.GetCount_management("PCA_POLYGONS_TEMP_LAYER_OTHER").getOutput(0))
if Temp_PCA_Polygon_other_feature_count == 0:
    arcpy.AddMessage("No other features imported")
else:
    arcpy.AddMessage(
        "Updated {1} other features in PCA Polygons".format("PCA_POLYGONS_TEMP_LAYER_OTHER", Temp_PCA_Polygon_other_feature_count))

#Add PCA Polygons to the map
# pca_polygons_path = MPA_USER_PCA_POLYGONS
# arcpy.AddMessage(pca_polygons_path)
# aprx = arcpy.mp.ArcGISProject("CURRENT")
# map = aprx.listMaps()[0]  # assumes data to be added to first map listed
# map.addDataFromPath(pca_polygons_path)

arcpy.AddWarning("Please check PCA_Polygons GDB to make sure the PCA Updates for each assessment point came across. If no errors, you can move on to Step 3a.")


