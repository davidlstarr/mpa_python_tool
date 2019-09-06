# -*- coding: utf-8 -*-
"""Generated by ArcGIS ModelBuilder on: 2019-09-03 16:25:52
All ModelBuilder functionality may not be exported. Edits may be required for equivalency with the original model.
"""

import arcpy

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

# Script parameters
Pavement_Assessment_Areas_WFS = arcpy.GetParameterAsText(0) or r"PCA_Collector_WFS\Pavement Assessment Areas WFS"
Pavement_Assessment_Areas__3_ = arcpy.GetParameterAsText(1) or r"Local Datasets\Pavement Assessment Areas"
Updated_record = arcpy.GetParameterAsText(2) or r"C:\Users\temp\PCA_DATA.gdb\Updated_record"
# Local variables:
Pavement_Assessment_Areas_WFS__7_ = Pavement_Assessment_Areas_WFS
Pavement_Assessment_Areas = Pavement_Assessment_Areas__3_
Asphalt_Pavement_Condition_Assessment = r"Local Datasets\Asphalt Pavement Condition Assessment"
Paver_Condition_Assessment = r"Local Datasets\Paver Condition Assessment"
Concrete_Pavement_Condition_Assessment = r"Local Datasets\Concrete Pavement Condition Assessment"
Other_Type_of_Pavement_Condition_Assessment = r"Local Datasets\Other Type of Pavement Condition Assessment"
Pavement_Assessment_Areas_WFS__6_ = Pavement_Assessment_Areas_WFS__7_
Pavement_Assessment_Areas_WFS__3_ = Pavement_Assessment_Areas_WFS__7_
Pavement_Assessment_Areas_WFS__4_ = Pavement_Assessment_Areas_WFS__7_
Pavement_Assessment_Areas_WFS__2_ = Pavement_Assessment_Areas_WFS__7_
Pavement_Assessment_Areas_WFS__5_ = Pavement_Assessment_Areas_WFS__7_
Other_Type_of_Pavement_Condition_Assessment__2_ = r"Local Datasets\Other Type of Pavement Condition Assessment"
Assessment_Locations_Historic = Other_Type_of_Pavement_Condition_Assessment__2_
Asphalt_Pavement_Condition_Assessment__2_ = r"Local Datasets\Asphalt Pavement Condition Assessment"
Concrete_Pavement_Condition_Assessment__2_ = r"Local Datasets\Concrete Pavement Condition Assessment"
Paver_Condition_Assessment__2_ = r"Local Datasets\Paver Condition Assessment"
Assessment_Locations_Historic__3_ = r"PCA_Collector_WFS\Assessment Locations Historic"
Delete_Succeeded = "false"
Layer_With_Join_Removed = Pavement_Assessment_Areas_WFS__5_

# Process: Merge
arcpy.Merge_management(inputs=r"'Local Datasets\Asphalt Pavement Condition Assessment';'Local Datasets\Paver Condition Assessment';'Local Datasets\Concrete Pavement Condition Assessment';'Local Datasets\Other Type of Pavement Condition Assessment'", output=Updated_record, field_mappings=r"ASPHALT_CRACKING "Asphalt Cracking" true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,ASPHALT_CRACKING,-1,-1;ASPHALT_RUTTING "Asphalt Rutting" true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,ASPHALT_RUTTING,-1,-1;ASPHALT_PATCHES "Asphalt Patches" true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,ASPHALT_PATCHES,-1,-1;ASPHALT_POTHOLES_RAVELING "Asphalt Potholes and Raveling" true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,ASPHALT_POTHOLES_RAVELING,-1,-1;ASSESSMENT_COMMENTS "Assessment Comments" true true false 1000 Text 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Paver Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Concrete Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Other Type of Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000;GLOBALID "GlobalID" false false false 38 GlobalID 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,GLOBALID,-1,-1,Local Datasets\Paver Condition Assessment,GlobalID,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,GlobalID,-1,-1,Local Datasets\Other Type of Pavement Condition Assessment,GlobalID,-1,-1;CREATED_USER "created_user" false true false 255 Text 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Paver Condition Assessment,CREATED_USER,0,255,Local Datasets\Concrete Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_USER,0,255;CREATED_DATE "created_date" false true false 8 Date 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_DATE,-1,-1;LAST_EDITED_USER "last_edited_user" false true false 255 Text 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Paver Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Concrete Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Other Type of Pavement Condition Assessment,LAST_EDITED_USER,0,255;LAST_EDITED_DATE "last_edited_date" false true false 8 Date 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Other Type of Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1;RELATED_ASSETID "RELATED_ASSETID" true true false 50 Text 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,RELATED_ASSETID,0,50,Local Datasets\Paver Condition Assessment,RELATED_ASSETID,0,50,Local Datasets\Concrete Pavement Condition Assessment,RELATED_ASSETID,0,50;POINTID "POINTID" true true false 4 Long 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,POINTID,-1,-1,Local Datasets\Paver Condition Assessment,POINTID,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,POINTID,-1,-1;CONDITION "CONDITION" true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,CONDITION,-1,-1,Local Datasets\Paver Condition Assessment,CONDITION,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CONDITION,-1,-1;MATERIAL "MATERIAL" true true false 50 Text 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Paver Condition Assessment,MATERIAL,0,50,Local Datasets\Concrete Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Other Type of Pavement Condition Assessment,MATERIAL,0,50;PAVERS_OVERALL "Pavers Overall" true true false 2 Short 0 0,First,#,Local Datasets\Paver Condition Assessment,PAVERS_OVERALL,-1,-1;PAVERS_PATCHES "Pavers Patches" true true false 2 Short 0 0,First,#,Local Datasets\Paver Condition Assessment,PAVERS_PATCHES,-1,-1;PAVERS_PUMPING "Pavers Pumping" true true false 2 Short 0 0,First,#,Local Datasets\Paver Condition Assessment,PAVERS_PUMPING,-1,-1;PAVERS_RUTTING "Pavers Rutting" true true false 2 Short 0 0,First,#,Local Datasets\Paver Condition Assessment,PAVERS_RUTTING,-1,-1;PAVERS_JOINT_MATERIAL "Pavers Joint Material" true true false 2 Short 0 0,First,#,Local Datasets\Paver Condition Assessment,PAVERS_JOINT_MATERIAL,-1,-1;CONCRETE_CRACKING "Concrete Cracking" true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_CRACKING,-1,-1;CONCRETE_DCRACKING "Concrete D Cracking" true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_DCRACKING,-1,-1;CONCRETE_MIDSLAB_CRACKING "Concrete Mid-slab Cracking" true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_MIDSLAB_CRACKING,-1,-1;CONCRETE_SPALLING "Concrete Spalling" true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_SPALLING,-1,-1;CONCRETE_PATCHES "Concrete Patches" true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_PATCHES,-1,-1;CONCRETE_PUMPING "Concrete Pumping" true true false 2 Short 0 0,First,#,Local Datasets\Concrete Pavement Condition Assessment,CONCRETE_PUMPING,-1,-1", add_source="NO_SOURCE_INFO")

# Process: Select Layer By Location
arcpy.SelectLayerByLocation_management(in_layer=Pavement_Assessment_Areas__3_, overlap_type="INTERSECT", select_features=Updated_record, search_distance="", selection_type="NEW_SELECTION", invert_spatial_relationship="NOT_INVERT")

# Process: Add Join
arcpy.AddJoin_management(in_layer_or_view=Pavement_Assessment_Areas_WFS, in_field="ASSETID", join_table=Pavement_Assessment_Areas, join_field="ASSETID", join_type="KEEP_COMMON")

# Process: Calculate Field
arcpy.CalculateField_management(in_table=Pavement_Assessment_Areas_WFS__7_, field="L5Pavement_Assessment_Areas.CONDITION", expression="!MPA_USER.PCA_POLYGONS.CONDITION!", expression_type="PYTHON3", code_block="")

# Process: Calculate Field (2)
arcpy.CalculateField_management(in_table=Pavement_Assessment_Areas_WFS__7_, field="L5Pavement_Assessment_Areas.COND_DATE", expression="!MPA_USER.PCA_POLYGONS.LAST_EDITED_DATE!", expression_type="PYTHON3", code_block="")

# Process: Calculate Field (3)
arcpy.CalculateField_management(in_table=Pavement_Assessment_Areas_WFS__7_, field="L5Pavement_Assessment_Areas.MATERIAL", expression="!MPA_USER.PCA_POLYGONS.MATERIAL!", expression_type="PYTHON3", code_block="")

# Process: Calculate Field (4)
arcpy.CalculateField_management(in_table=Pavement_Assessment_Areas_WFS__7_, field="L5Pavement_Assessment_Areas.ASSESSOR", expression="!MPA_USER.PCA_POLYGONS.LAST_EDITED_USER!", expression_type="PYTHON3", code_block="")

# Process: Append
arcpy.Append_management(inputs=r"'Local Datasets\Other Type of Pavement Condition Assessment';'Local Datasets\Asphalt Pavement Condition Assessment';'Local Datasets\Concrete Pavement Condition Assessment';'Local Datasets\Paver Condition Assessment'", target=Assessment_Locations_Historic__3_, schema_type="NO_TEST", field_mapping=r"AREASQYD "AREA SQUARE YARDS" true true false 0 Double 0 0,First,#;AREASQFT "AREA SQUARE FEET" true true false 0 Double 0 0,First,#;MATERIAL "MATERIAL" true true false 50 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Asphalt Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Concrete Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Paver Condition Assessment,MATERIAL,0,50;LOCATION "LOCATION" true true false 50 Text 0 0,First,#;USE_ "USE" true true false 50 Text 0 0,First,#;USE_CUST "USE CUSTOMER" true true false 50 Text 0 0,First,#;LEASED "LEASED" true true false 50 Text 0 0,First,#;MAIN_RESP "MAINTENANCE RESPONSIBILITY" true true false 50 Text 0 0,First,#;CONDITION "CONDITION" true true false 0 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,CONDITION,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CONDITION,-1,-1,Local Datasets\Paver Condition Assessment,CONDITION,-1,-1;COND_DATE "COND_DATE" true true false 8 Date 0 0,First,#;TYPE "TYPE" true true false 50 Text 0 0,First,#;TERMINAL "TERMINAL" true true false 15 Text 0 0,First,#;ASSETID "ASSET ID" true true false 50 Text 0 0,First,#;ASSESSOR "ASSESSOR" true true false 50 Text 0 0,First,#;ASSESSMENT_COMMENTS "ASSESSMENT_COMMENTS" true true false 1000 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Asphalt Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Concrete Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Paver Condition Assessment,ASSESSMENT_COMMENTS,0,1000;GLOBALID "GLOBALID" false false false 38 GlobalID 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,GlobalID,-1,-1,Local Datasets\Asphalt Pavement Condition Assessment,GLOBALID,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,GlobalID,-1,-1,Local Datasets\Paver Condition Assessment,GlobalID,-1,-1;AREAACRES "AREAACRES" true true false 0 Double 0 0,First,#;created_user "created_user" true true false 255 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Concrete Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Paver Condition Assessment,CREATED_USER,0,255;created_date "created_date" true true false 8 Date 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,CREATED_DATE,-1,-1;last_edited_user "last_edited_user" true true false 255 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Asphalt Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Concrete Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Paver Condition Assessment,LAST_EDITED_USER,0,255;last_edited_date "last_edited_date" true true false 8 Date 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Asphalt Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,LAST_EDITED_DATE,-1,-1", subtype="", expression="")

# Process: Delete
arcpy.Delete_management(in_data=Updated_record, data_type="")

# Process: Calculate Field (5)
arcpy.CalculateField_management(in_table=Pavement_Assessment_Areas_WFS__7_, field="L5Pavement_Assessment_Areas.ASSESSMENT_COMMENTS", expression="!MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS!", expression_type="PYTHON3", code_block="")

# Process: Remove Join
arcpy.RemoveJoin_management(in_layer_or_view=Pavement_Assessment_Areas_WFS__5_, join_name="MPA_USER.PCA_POLYGONS")

