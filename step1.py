#---------------------------------------------------------#
#--------Step 1-Download data from WFS for review---------#
#---------------------------------------------------------#


import arcpy
import json

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

#Make sure to drop the config file in your ArcPro project and change this to the config location

# with open('C:\\Users\\dstarr\\Documents\\ArcGIS\\Projects\MPA\\config.json') as json_data_file:
#     data = json.load(json_data_file)
# print(data)
#
# local_gdb_path = data['local_paths']['local_gdb_path']
# sde_path = data['local_paths']['sde_path']

# Script parameters
arcpy.env.workspace = arcpy.GetParameterAsText(0)
SDE_CONNECTION = arcpy.GetParameterAsText(1)

#Make sure to drop the config file in your ArcPro project
with open(arcpy.env.workspace+'/config.json') as json_data_file:
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

#arcpy.AddMessage(data["wfs_paths"]["WFS_paver_path"])
arcpy.AddMessage("Download data from WFS for review")

# Export Messaging
WFS_path_array = [WFS_paver_path, WFS_concrete_path, WFS_asphalt_path, WFS_other_type_path]
WFS_message_array = ["Paver Feature Layer", "Concrete Feature Layer", "Asphalt Feature Layer", "Other Feature Layer"]

for wfs_path, wfs_message in zip(WFS_path_array, WFS_message_array):
    message = int(arcpy.GetCount_management(wfs_path).getOutput(0))

    if message == 0:
        arcpy.AddWarning(wfs_message +" has no features.".format(wfs_path))
    else:
        arcpy.AddMessage(
            wfs_message +" exported {1} features.".format(wfs_path, message))



# Local variables:
merged_PCA_Updates = "merged_PCA_Updates"
merged_PCA_Updates_SpatialJo = "merged_PCA_Updates_SpatialJo"
merged_PCA_Updates_SpatialJoin_GT_2 = "merged_PCA_Updates_SpatialJoin_GT_2"
MPA_USER_PCA_POLYGONS = SDE_CONNECTION + "/MPA_USER.Pavement/PCA_POLYGONS"

#This is check to ensure that there is only one inspection point per polygon

arcpy.Delete_management(merged_PCA_Updates)
arcpy.Delete_management(merged_PCA_Updates_SpatialJo)
arcpy.Delete_management(merged_PCA_Updates_SpatialJoin_GT_2)

# Process: Merge
arcpy.Merge_management(inputs=WFS_paver_path+";"+WFS_concrete_path+";"+WFS_asphalt_path+";"+WFS_other_type_path, output=merged_PCA_Updates, field_mappings="", add_source="NO_SOURCE_INFO")

# Process: Spatial Join
arcpy.SpatialJoin_analysis(target_features=WFS_Pavement_Assessment_Areas, join_features=merged_PCA_Updates, out_feature_class=merged_PCA_Updates_SpatialJo, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_ALL", field_mapping="", match_option="CONTAINS", search_radius="", distance_field_name="")

# Process: Select Layer By Attribute
#arcpy.SelectLayerByAttribute_management(in_layer_or_view=merged_PCA_Updates_SpatialJo, selection_type="NEW_SELECTION", where_clause="Join_Count >= 2", invert_where_clause="")
arcpy.Select_analysis(in_features=merged_PCA_Updates_SpatialJo, out_feature_class=merged_PCA_Updates_SpatialJoin_GT_2, where_clause="Join_Count >= 2")


message = int(arcpy.GetCount_management(merged_PCA_Updates_SpatialJoin_GT_2).getOutput(0))
if message == 0:
   arcpy.AddMessage("Inspection point check success. There is one point per polygon!")
else:
   arcpy.AddError("Please check to ensure there is only one inspection point per polygon.")
   join_paver_path = r""+arcpy.env.workspace+"\merged_PCA_Updates_SpatialJoin_GT_2"
   aprx = arcpy.mp.ArcGISProject("CURRENT")
   map = aprx.listMaps()[0]  # assumes data to be added to first map listed
   map.addDataFromPath(join_paver_path)

   merged_paver_path = r""+arcpy.env.workspace+"\merged_PCA_Updates"
   aprx = arcpy.mp.ArcGISProject("CURRENT")
   map = aprx.listMaps()[0]  # assumes data to be added to first map listed
   map.addDataFromPath(merged_paver_path)




#Deleting Temporary Feature classes
arcpy.Delete_management(TEMP_PAVERS_PCA)
arcpy.Delete_management(TEMP_CONCRETE_PCA)
arcpy.Delete_management(TEMP_ASPHALT_PCA)
arcpy.Delete_management(TEMP_OTHER_PCA)

#Expression and code blocks variables:

Paver_Expression = "MinimumValue( !PAVERS_OVERALL!, !PAVERS_PATCHES!, !PAVERS_PUMPING!, !PAVERS_RUTTING!, !PAVERS_JOINT_MATERIAL!)"
codeblock = """def MinimumValue(*args):
    return min(args)"""
Concrete_Expression = "MinimumValue( !CONCRETE_CRACKING!, !CONCRETE_DCRACKING!, !CONCRETE_MIDSLAB_CRACKING!, !CONCRETE_SPALLING!, !CONCRETE_PATCHES!, !CONCRETE_PUMPING!)"
Asphalt_Expression = "MinimumValue(!ASPHALT_CRACKING!,!ASPHALT_RUTTING!,!ASPHALT_PATCHES!,!ASPHALT_POTHOLES_RAVELING!)"

temp_layers_path = [TEMP_PAVERS_PCA, TEMP_CONCRETE_PCA, TEMP_ASPHALT_PCA]
expression_array = [Paver_Expression, Concrete_Expression, Asphalt_Expression]
WFS_path_array = [WFS_paver_path, WFS_concrete_path, WFS_asphalt_path, WFS_other_type_path]

for wfs_path, temp_layers, expression in zip(WFS_path_array, temp_layers_path, expression_array):
        arcpy.FeatureClassToFeatureClass_conversion(in_features=wfs_path, out_path=arcpy.env.workspace, out_name=temp_layers, where_clause="", field_mapping="", config_keyword="")
        arcpy.CalculateField_management(in_table=wfs_path, field="CONDITION", expression=expression, expression_type="PYTHON_9.3", code_block=codeblock)

arcpy.FeatureClassToFeatureClass_conversion(in_features=WFS_other_type_path, out_path=arcpy.env.workspace, out_name=TEMP_OTHER_PCA, where_clause="", field_mapping="", config_keyword="")

# Get the count from Temp Layers
WFS_path_array = [WFS_paver_path, WFS_concrete_path, WFS_asphalt_path, WFS_other_type_path]
temp_path_message_array = ["Temporary Paver Feature Class", "Temporary Concrete Feature Class", "Temporary Asphalt Feature Class", "Temporary Other Feature Class"]

for temp_path, temp_message in zip(temp_layers_path, temp_path_message_array):
    message = int(arcpy.GetCount_management(temp_path).getOutput(0))

    if message == 0:
        arcpy.AddWarning("{0} has no features. Please ensure your inputs are correct.".format(temp_path))
    else:
        arcpy.AddMessage(
             "{1} features were imported into ".format(temp_path, message) + temp_message + ".")


#------Create temporary layers with Lot IDs and Recent Assessment values combined------#

arcpy.AddMessage("Create temporary layers with Lot IDs and Recent Assessment values combined")

arcpy.Delete_management(PAVERS_PCA_Updates)
arcpy.Delete_management(CONCRETE_PCA_Updates)
arcpy.Delete_management(ASPHALT_PCA_Updates)
arcpy.Delete_management(OTHER_PCA_Updates)

temp_pavers_pca_path = arcpy.env.workspace + "/PAVERS_PCA"
temp_concrete_pca_path = arcpy.env.workspace + "/CONCRETE_PCA"
temp_asphalt_pca_path = arcpy.env.workspace + "/ASPHALT_PCA"
temp_other_pca_path = arcpy.env.workspace + "/OTHER_PCA"

intersect_variable_paver = r"'" + MPA_USER_PCA_POLYGONS + "' #;" + temp_pavers_pca_path + " #"
#arcpy.AddMessage(intersect_variable_paver)
intersect_variable_concrete = r"'" + MPA_USER_PCA_POLYGONS + "' #;" + temp_concrete_pca_path + " #"
#arcpy.AddMessage(intersect_variable_concrete)
intersect_variable_asphalt = r"'" + MPA_USER_PCA_POLYGONS + "' #;" + temp_asphalt_pca_path + " #"
intersect_variable_other = r"'" + MPA_USER_PCA_POLYGONS + "' #;" + temp_other_pca_path + " #"

#arcpy.AddMessage(intersect_variable_paver)

pca_update_layers_list = [PAVERS_PCA_Updates, CONCRETE_PCA_Updates, ASPHALT_PCA_Updates, OTHER_PCA_Updates]
intersect_variables_list = [intersect_variable_paver, intersect_variable_concrete, intersect_variable_asphalt, intersect_variable_other]

for pca_update_layers, intersect_variables in zip(pca_update_layers_list, intersect_variables_list):
        arcpy.Intersect_analysis(in_features=intersect_variables, out_feature_class=pca_update_layers, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")

#Messaging for creation of PCA Update layers
for pca_update_layers in pca_update_layers_list:
    message = int(arcpy.GetCount_management(pca_update_layers).getOutput(0))

    if message == 0:
        arcpy.AddWarning(pca_update_layers + " layer has not been created.")
    else:
        arcpy.AddMessage(
            pca_update_layers + " has been created")


#Do logging for error tracking

#Add to PCA_Updates layers to  the map

paver_path = r""+arcpy.env.workspace+"\PAVERS_PCA_Updates"
aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]  # assumes data to be added to first map listed
map.addDataFromPath(paver_path)

paver_path = r""+arcpy.env.workspace+"\CONCRETE_PCA_Updates"
aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]  # assumes data to be added to first map listed
map.addDataFromPath(paver_path)

paver_path = r""+arcpy.env.workspace+"\ASPHALT_PCA_Updates"
aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]  # assumes data to be added to first map listed
map.addDataFromPath(paver_path)

paver_path = r""+arcpy.env.workspace+"\OTHER_PCA_Updates"
aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]  # assumes data to be added to first map listed
map.addDataFromPath(paver_path)

wfs_paver_path = WFS_paver_path
aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]  # assumes data to be added to first map listed
map.addDataFromPath(wfs_paver_path)

wfs_concrete_path = WFS_concrete_path
aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]  # assumes data to be added to first map listed
map.addDataFromPath(wfs_concrete_path)

wfs_asphalt_path = WFS_asphalt_path
aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]  # assumes data to be added to first map listed
map.addDataFromPath(wfs_asphalt_path)

wfs_other_path = WFS_other_type_path
aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]  # assumes data to be added to first map listed
map.addDataFromPath(wfs_other_path)

arcpy.AddWarning("Please confirm that this data is correct before running Step 2.")

