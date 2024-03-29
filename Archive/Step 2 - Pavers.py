# -*- coding: utf-8 -*-
"""Generated by ArcGIS ModelBuilder on: 2019-09-06 14:31:29
All ModelBuilder functionality may not be exported. Edits may be required for equivalency with the original model.
"""

import arcpy

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

# Local variables:
PCA_POLYGONS_Layer3 = "PCA_POLYGONS_Layer3"
AREAS_PCA_Layer2__3_ = PCA_POLYGONS_Layer3
AREAS_PCA_Layer2__4_ = AREAS_PCA_Layer2__3_
AREAS_PCA_Layer2__5_ = AREAS_PCA_Layer2__3_
AREAS_PCA_Layer2__6_ = AREAS_PCA_Layer2__3_
AREAS_PCA_Layer2__7_ = AREAS_PCA_Layer2__3_
AREAS_PCA_Layer2__8_ = AREAS_PCA_Layer2__3_
PCA_POLYGONS_Layer3__3_ = AREAS_PCA_Layer2__4_

# Process: Make Feature Layer (3)
arcpy.MakeFeatureLayer_management(in_features="", out_layer=PCA_POLYGONS_Layer3, where_clause="", workspace="", field_info="OBJECTID OBJECTID VISIBLE NONE;AREASQYD AREASQYD VISIBLE NONE;AREASQFT AREASQFT VISIBLE NONE;MATERIAL MATERIAL VISIBLE NONE;LOCATION LOCATION VISIBLE NONE;USE_ USE_ VISIBLE NONE;USE_CUST USE_CUST VISIBLE NONE;LEASED LEASED VISIBLE NONE;MAIN_RESP MAIN_RESP VISIBLE NONE;CONDITION CONDITION VISIBLE NONE;COND_DATE COND_DATE VISIBLE NONE;TYPE TYPE VISIBLE NONE;TERMINAL TERMINAL VISIBLE NONE;ASSETID ASSETID VISIBLE NONE;ASSESSOR ASSESSOR VISIBLE NONE;ASSESSMENT_COMMENTS ASSESSMENT_COMMENTS VISIBLE NONE;GLOBALID GLOBALID VISIBLE NONE;AREAACRES AREAACRES VISIBLE NONE;CREATED_USER CREATED_USER VISIBLE NONE;CREATED_DATE CREATED_DATE VISIBLE NONE;LAST_EDITED_USER LAST_EDITED_USER VISIBLE NONE;LAST_EDITED_DATE LAST_EDITED_DATE VISIBLE NONE;COND_LABEL COND_LABEL VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.AREA SHAPE.AREA VISIBLE NONE;SHAPE.LEN SHAPE.LEN VISIBLE NONE")

# Process: Add Join (3)
arcpy.AddJoin_management(in_layer_or_view=PCA_POLYGONS_Layer3, in_field="ASSETID", join_table="MPA_USER.Historic_Pavement_Assessments", join_field="ASSETID", join_type="KEEP_COMMON")

# Process: Paver Calc Date
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer2__3_, field="MPA_USER.PCA_POLYGONS.COND_DATE", expression="!PAVERS_PCA_Updates.LAST_EDITED_DATE_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Material
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer2__3_, field="MPA_USER.PCA_POLYGONS.MATERIAL", expression="!PAVERS_PCA_Updates.MATERIAL_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Assessment
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer2__3_, field="MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS", expression="!PAVERS_PCA_Updates.ASSESSMENT_COMMENTS_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Editor'
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer2__3_, field="MPA_USER.PCA_POLYGONS.ASSESSOR", expression="!PAVERS_PCA_Updates.LAST_EDITED_USER_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Cond
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer2__3_, field="MPA_USER.PCA_POLYGONS.CONDITION", expression="!PAVERS_PCA_Updates.CONDITION_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Calculate Field
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer2__4_, field="COND_LABEL", expression="Reclass(!MPA_USER.PCA_POLYGONS.CONDITION!)", expression_type="PYTHON3", code_block="def Reclass(field):
  if field == 5:
    return "Good"
  elif field == 4:
    return "Good" 
  elif field == 3:
    return "Fair"  
  elif field == 2:
    return "Poor"
  elif field == 1:
    return "Poor"")

