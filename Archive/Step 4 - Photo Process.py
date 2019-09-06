# -*- coding: utf-8 -*-
"""Generated by ArcGIS ModelBuilder on: 2019-09-04 16:09:43
All ModelBuilder functionality may not be exported. Edits may be required for equivalency with the original model.
"""

import arcpy

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

# Script parameters
PCA_Photos = arcpy.GetParameterAsText(0) or r"Local Datasets\PCA Photos"
PCA_Photos__5_ = arcpy.GetParameterAsText(1) or r"PCA_Collector_WFS\PCA Photos"
PCA_DATA_gdb = arcpy.GetParameterAsText(2) or r"C:\Users\temp\PCA_DATA.gdb"
TEMP_PCA_Photos = arcpy.GetParameterAsText(3) or r"C:\Users\temp\PCA_DATA.gdb\TEMP_PCA_Photos"
PCA_Photos__6_ = arcpy.GetParameterAsText(4) or r"Local Datasets\PCA Photos"
# Local variables:
PCA_Photos__4_ = PCA_Photos__5_
PCA_Photos__2_ = TEMP_PCA_Photos
Delete_Succeeded__2_ = "false"

# Process: Select Layer By Location
arcpy.SelectLayerByLocation_management(in_layer=PCA_Photos__5_, overlap_type="ARE_IDENTICAL_TO", select_features=PCA_Photos__6_, search_distance="", selection_type="NEW_SELECTION", invert_spatial_relationship="INVERT")

# Process: Feature Class to Feature Class
arcpy.FeatureClassToFeatureClass_conversion(in_features=PCA_Photos__4_, out_path=PCA_DATA_gdb, out_name="TEMP_PCA_Photos", where_clause="", field_mapping=r"ASSETID "ASSET ID" true true false 50 Text 0 0,First,#,PCA_Collector_WFS\PCA Photos,ASSETID,0,50;COMMENT "COMMENT" true true false 50 Text 0 0,First,#,PCA_Collector_WFS\PCA Photos,COMMENT,0,50;created_user "created_user" false true false 255 Text 0 0,First,#,PCA_Collector_WFS\PCA Photos,created_user,0,255;created_date "created_date" false true false 8 Date 0 0,First,#,PCA_Collector_WFS\PCA Photos,created_date,-1,-1;last_edited_user "last_edited_user" false true false 255 Text 0 0,First,#,PCA_Collector_WFS\PCA Photos,last_edited_user,0,255;last_edited_date "last_edited_date" false true false 8 Date 0 0,First,#,PCA_Collector_WFS\PCA Photos,last_edited_date,-1,-1;GlobalID "GlobalID" false false false 38 GlobalID 0 0,First,#,PCA_Collector_WFS\PCA Photos,GlobalID,-1,-1", config_keyword="")

# Process: Append
arcpy.Append_management(inputs=r"C:\Users\temp\PCA_DATA.gdb\TEMP_PCA_Photos", target=PCA_Photos, schema_type="NO_TEST", field_mapping=r"ASSETID "ASSET ID" true true false 50 Text 0 0,First,#,C:\Users\temp\PCA_DATA.gdb\TEMP_PCA_Photos,ASSETID,0,50;COMMENT "COMMENT" true true false 50 Text 0 0,First,#,C:\Users\temp\PCA_DATA.gdb\TEMP_PCA_Photos,COMMENT,0,50", subtype="", expression="")

# Process: Delete (2)
arcpy.Delete_management(in_data=TEMP_PCA_Photos, data_type="")

