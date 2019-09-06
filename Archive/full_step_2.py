# -*- coding: utf-8 -*-
"""Generated by ArcGIS ModelBuilder on: 2019-08-29 15:07:47
All ModelBuilder functionality may not be exported. Edits may be required for equivalency with the original model.
"""

import arcpy

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

# Script parameters
MPA_USER_PCA_POLYGONS = arcpy.GetParameterAsText(0) or r"C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\MDOT MPA\Python tool\Transfer for David Starr\Transfer for David Starr\MPA\DODB12(1).sde\MPA_USER.PCA_POLYGONS"
ASPHALT_PCA = arcpy.GetParameterAsText(1) or r"C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\ASPHALT_PCA"
CONCRETE_PCA = arcpy.GetParameterAsText(2) or r"C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\CONCRETE_PCA"
PAVERS_PCA = arcpy.GetParameterAsText(3) or r"C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\PAVERS_PCA"
OTHER_PCA = arcpy.GetParameterAsText(4) or r"C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\OTHER_PCA"
# Local variables:
AREAS_PCA_Layer = "PCA_POLYGONS_Layer"
AREAS_PCA_Layer__3_ = AREAS_PCA_Layer
CONCRETE_PCA_Updates = r"C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\CONCRETE_PCA_Updates"
AREAS_PCA_Layer__4_ = AREAS_PCA_Layer__3_
AREAS_PCA_Layer__5_ = AREAS_PCA_Layer__3_
AREAS_PCA_Layer__6_ = AREAS_PCA_Layer__3_
AREAS_PCA_Layer__7_ = AREAS_PCA_Layer__3_
AREAS_PCA_Layer__8_ = AREAS_PCA_Layer__3_
AREAS_PCA_Layer1 = "PCA_POLYGONS_Layer1"
AREAS_PCA_Layer1__7_ = AREAS_PCA_Layer1
ASPHALT_PCA_Updates = r"C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\ASPHALT_PCA_Updates"
AREAS_PCA_Layer1__4_ = AREAS_PCA_Layer1__7_
AREAS_PCA_Layer1__8_ = AREAS_PCA_Layer1__7_
AREAS_PCA_Layer1__3_ = AREAS_PCA_Layer1__7_
AREAS_PCA_Layer1__5_ = AREAS_PCA_Layer1__7_
AREAS_PCA_Layer1__6_ = AREAS_PCA_Layer1__7_
PCA_POLYGONS_Layer3 = "PCA_POLYGONS_Layer3"
AREAS_PCA_Layer2__3_ = PCA_POLYGONS_Layer3
PAVERS_PCA_Updates = r"C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\PAVERS_PCA_Updates"
AREAS_PCA_Layer2__4_ = AREAS_PCA_Layer2__3_
AREAS_PCA_Layer2__5_ = AREAS_PCA_Layer2__3_
AREAS_PCA_Layer2__6_ = AREAS_PCA_Layer2__3_
AREAS_PCA_Layer2__7_ = AREAS_PCA_Layer2__3_
AREAS_PCA_Layer2__8_ = AREAS_PCA_Layer2__3_
Other_Type_of_Pavement_Condition_Assessment = r"Local Datasets\Other Type of Pavement Condition Assessment"
Assessment_Locations_Historic = Other_Type_of_Pavement_Condition_Assessment
Asphalt_Pavement_Condition_Assessment = r"Local Datasets\Asphalt Pavement Condition Assessment"
Concrete_Pavement_Condition_Assessment = r"Local Datasets\Concrete Pavement Condition Assessment"
Paver_Condition_Assessment = r"Local Datasets\Paver Condition Assessment"
Assessment_Locations_Historic__2_ = r"Local Datasets\Assessment Locations Historic"
OTHER_PCA_Updates = r"C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\OTHER_PCA_Updates"
PCA_POLYGONS_Layer3__3_ = AREAS_PCA_Layer2__4_
PCA_POLYGONS_Layer = AREAS_PCA_Layer__4_
PCA_POLYGONS_Layer1 = AREAS_PCA_Layer1__4_

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(in_features=MPA_USER_PCA_POLYGONS, out_layer=AREAS_PCA_Layer, where_clause="", workspace="", field_info="OBJECTID OBJECTID VISIBLE NONE;AREASQYD AREASQYD VISIBLE NONE;AREASQFT AREASQFT VISIBLE NONE;MATERIAL MATERIAL VISIBLE NONE;LOCATION LOCATION VISIBLE NONE;USE_ USE_ VISIBLE NONE;USE_CUST USE_CUST VISIBLE NONE;LEASED LEASED VISIBLE NONE;MAIN_RESP MAIN_RESP VISIBLE NONE;CONDITION CONDITION VISIBLE NONE;COND_DATE COND_DATE VISIBLE NONE;TYPE TYPE VISIBLE NONE;TERMINAL TERMINAL VISIBLE NONE;ASSETID ASSETID VISIBLE NONE;ASSESSOR ASSESSOR VISIBLE NONE;ASSESSMENT_COMMENTS ASSESSMENT_COMMENTS VISIBLE NONE;GLOBALID GLOBALID VISIBLE NONE;AREAACRES AREAACRES VISIBLE NONE;CREATED_USER CREATED_USER VISIBLE NONE;CREATED_DATE CREATED_DATE VISIBLE NONE;LAST_EDITED_USER LAST_EDITED_USER VISIBLE NONE;LAST_EDITED_DATE LAST_EDITED_DATE VISIBLE NONE;COND_LABEL COND_LABEL VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.AREA SHAPE.AREA VISIBLE NONE;SHAPE.LEN SHAPE.LEN VISIBLE NONE")

# Process: Intersect (2)
arcpy.Intersect_analysis(in_features=r"'C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\MDOT MPA\Python tool\Transfer for David Starr\Transfer for David Starr\MPA\DODB12(1).sde\MPA_USER.PCA_POLYGONS' #;'C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\CONCRETE_PCA' #", out_feature_class=CONCRETE_PCA_Updates, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")

# Process: Add Join
arcpy.AddJoin_management(in_layer_or_view=AREAS_PCA_Layer, in_field="ASSETID", join_table=CONCRETE_PCA_Updates, join_field="ASSETID", join_type="KEEP_COMMON")

# Process: Conc Calc Date
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer__3_, field="MPA_USER.PCA_POLYGONS.COND_DATE", expression="!CONCRETE_PCA_Updates.LAST_EDITED_DATE_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Conc Calc Material
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer__3_, field="MPA_USER.PCA_POLYGONS.MATERIAL", expression="!CONCRETE_PCA_Updates.MATERIAL_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Conc Calc Assessment
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer__3_, field="MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS", expression="!CONCRETE_PCA_Updates.ASSESSMENT_COMMENTS_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Conc Calc Editor
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer__3_, field="MPA_USER.PCA_POLYGONS.ASSESSOR", expression="!CONCRETE_PCA_Updates.LAST_EDITED_USER_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Make Feature Layer (2)
arcpy.MakeFeatureLayer_management(in_features=MPA_USER_PCA_POLYGONS, out_layer=AREAS_PCA_Layer1, where_clause="", workspace="", field_info="OBJECTID OBJECTID VISIBLE NONE;AREASQYD AREASQYD VISIBLE NONE;AREASQFT AREASQFT VISIBLE NONE;MATERIAL MATERIAL VISIBLE NONE;LOCATION LOCATION VISIBLE NONE;USE_ USE_ VISIBLE NONE;USE_CUST USE_CUST VISIBLE NONE;LEASED LEASED VISIBLE NONE;MAIN_RESP MAIN_RESP VISIBLE NONE;CONDITION CONDITION VISIBLE NONE;COND_DATE COND_DATE VISIBLE NONE;TYPE TYPE VISIBLE NONE;TERMINAL TERMINAL VISIBLE NONE;ASSETID ASSETID VISIBLE NONE;ASSESSOR ASSESSOR VISIBLE NONE;ASSESSMENT_COMMENTS ASSESSMENT_COMMENTS VISIBLE NONE;GLOBALID GLOBALID VISIBLE NONE;AREAACRES AREAACRES VISIBLE NONE;CREATED_USER CREATED_USER VISIBLE NONE;CREATED_DATE CREATED_DATE VISIBLE NONE;LAST_EDITED_USER LAST_EDITED_USER VISIBLE NONE;LAST_EDITED_DATE LAST_EDITED_DATE VISIBLE NONE;COND_LABEL COND_LABEL VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.AREA SHAPE.AREA VISIBLE NONE;SHAPE.LEN SHAPE.LEN VISIBLE NONE")

# Process: Intersect (3)
arcpy.Intersect_analysis(in_features=r"'C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\MDOT MPA\Python tool\Transfer for David Starr\Transfer for David Starr\MPA\DODB12(1).sde\MPA_USER.PCA_POLYGONS' #;'C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\ASPHALT_PCA' #", out_feature_class=ASPHALT_PCA_Updates, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")

# Process: Add Join (2)
arcpy.AddJoin_management(in_layer_or_view=AREAS_PCA_Layer1, in_field="ASSETID", join_table=ASPHALT_PCA_Updates, join_field="ASSETID", join_type="KEEP_COMMON")

# Process: Asphalt Calc Date
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer1__7_, field="MPA_USER.PCA_POLYGONS.COND_DATE", expression="!ASPHALT_PCA_Updates.LAST_EDITED_DATE_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Asphalt Calc Material
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer1__7_, field="MPA_USER.PCA_POLYGONS.MATERIAL", expression="!ASPHALT_PCA_Updates.MATERIAL_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Asphalt Calc Assessment
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer1__7_, field="MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS", expression="!ASPHALT_PCA_Updates.ASSESSMENT_COMMENTS_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Asphalt Calc Editor
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer1__7_, field="MPA_USER.PCA_POLYGONS.ASSESSOR", expression="!ASPHALT_PCA_Updates.LAST_EDITED_USER_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Make Feature Layer (3)
arcpy.MakeFeatureLayer_management(in_features=MPA_USER_PCA_POLYGONS, out_layer=PCA_POLYGONS_Layer3, where_clause="", workspace="", field_info="OBJECTID OBJECTID VISIBLE NONE;AREASQYD AREASQYD VISIBLE NONE;AREASQFT AREASQFT VISIBLE NONE;MATERIAL MATERIAL VISIBLE NONE;LOCATION LOCATION VISIBLE NONE;USE_ USE_ VISIBLE NONE;USE_CUST USE_CUST VISIBLE NONE;LEASED LEASED VISIBLE NONE;MAIN_RESP MAIN_RESP VISIBLE NONE;CONDITION CONDITION VISIBLE NONE;COND_DATE COND_DATE VISIBLE NONE;TYPE TYPE VISIBLE NONE;TERMINAL TERMINAL VISIBLE NONE;ASSETID ASSETID VISIBLE NONE;ASSESSOR ASSESSOR VISIBLE NONE;ASSESSMENT_COMMENTS ASSESSMENT_COMMENTS VISIBLE NONE;GLOBALID GLOBALID VISIBLE NONE;AREAACRES AREAACRES VISIBLE NONE;CREATED_USER CREATED_USER VISIBLE NONE;CREATED_DATE CREATED_DATE VISIBLE NONE;LAST_EDITED_USER LAST_EDITED_USER VISIBLE NONE;LAST_EDITED_DATE LAST_EDITED_DATE VISIBLE NONE;COND_LABEL COND_LABEL VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;SHAPE.AREA SHAPE.AREA VISIBLE NONE;SHAPE.LEN SHAPE.LEN VISIBLE NONE")

# Process: Intersect
arcpy.Intersect_analysis(in_features=r"'C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\MDOT MPA\Python tool\Transfer for David Starr\Transfer for David Starr\MPA\DODB12(1).sde\MPA_USER.PCA_POLYGONS' #;'C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\PAVERS_PCA' #", out_feature_class=PAVERS_PCA_Updates, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")

# Process: Add Join (3)
arcpy.AddJoin_management(in_layer_or_view=PCA_POLYGONS_Layer3, in_field="ASSETID", join_table=PAVERS_PCA_Updates, join_field="ASSETID", join_type="KEEP_COMMON")

# Process: Paver Calc Date
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer2__3_, field="MPA_USER.PCA_POLYGONS.COND_DATE", expression="!PAVERS_PCA_Updates.LAST_EDITED_DATE_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Material
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer2__3_, field="MPA_USER.PCA_POLYGONS.MATERIAL", expression="!PAVERS_PCA_Updates.MATERIAL_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Assessment
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer2__3_, field="MPA_USER.PCA_POLYGONS.ASSESSMENT_COMMENTS", expression="!PAVERS_PCA_Updates.ASSESSMENT_COMMENTS_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Paver Calc Editor'
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer2__3_, field="MPA_USER.PCA_POLYGONS.ASSESSOR", expression="!PAVERS_PCA_Updates.LAST_EDITED_USER_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Append
arcpy.Append_management(inputs=r"'Local Datasets\Other Type of Pavement Condition Assessment';'Local Datasets\Asphalt Pavement Condition Assessment';'Local Datasets\Concrete Pavement Condition Assessment';'Local Datasets\Paver Condition Assessment'", target=Assessment_Locations_Historic__2_, schema_type="NO_TEST", field_mapping=r"AREASQYD "AREA SQUARE YARDS" true true false 8 Double 0 0,First,#;AREASQFT "AREA SQUARE FEET" true true false 8 Double 0 0,First,#;MATERIAL "MATERIAL" true true false 50 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Asphalt Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Concrete Pavement Condition Assessment,MATERIAL,0,50,Local Datasets\Paver Condition Assessment,MATERIAL,0,50;LOCATION "LOCATION" true true false 50 Text 0 0,First,#;USE_ "USE" true true false 50 Text 0 0,First,#;USE_CUST "USE CUSTOMER" true true false 50 Text 0 0,First,#;LEASED "LEASED" true true false 50 Text 0 0,First,#;MAIN_RESP "MAINTENANCE RESPONSIBILITY" true true false 50 Text 0 0,First,#;CONDITION "CONDITION" true true false 2 Short 0 0,First,#,Local Datasets\Asphalt Pavement Condition Assessment,CONDITION,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CONDITION,-1,-1,Local Datasets\Paver Condition Assessment,CONDITION,-1,-1;COND_DATE "COND_DATE" true true false 8 Date 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,CREATED_DATE,-1,-1;TYPE "TYPE" true true false 50 Text 0 0,First,#;TERMINAL "TERMINAL" true true false 15 Text 0 0,First,#;ASSETID "ASSET ID" true true false 50 Text 0 0,First,#;ASSESSOR "ASSESSOR" true true false 50 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_USER,0,50,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_USER,0,50,Local Datasets\Concrete Pavement Condition Assessment,CREATED_USER,0,50,Local Datasets\Paver Condition Assessment,CREATED_USER,0,50;ASSESSMENT_COMMENTS "ASSESSMENT_COMMENTS" true true false 1000 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Asphalt Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Concrete Pavement Condition Assessment,ASSESSMENT_COMMENTS,0,1000,Local Datasets\Paver Condition Assessment,ASSESSMENT_COMMENTS,0,1000;GLOBALID "GLOBALID" false false true 38 GlobalID 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,GlobalID,-1,-1,Local Datasets\Asphalt Pavement Condition Assessment,GLOBALID,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,GlobalID,-1,-1,Local Datasets\Paver Condition Assessment,GlobalID,-1,-1;AREAACRES "AREAACRES" true true false 8 Double 0 0,First,#;created_user "created_user" true true false 255 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Concrete Pavement Condition Assessment,CREATED_USER,0,255,Local Datasets\Paver Condition Assessment,CREATED_USER,0,255;created_date "created_date" true true false 8 Date 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Asphalt Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,CREATED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,CREATED_DATE,-1,-1;last_edited_user "last_edited_user" true true false 255 Text 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Asphalt Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Concrete Pavement Condition Assessment,LAST_EDITED_USER,0,255,Local Datasets\Paver Condition Assessment,LAST_EDITED_USER,0,255;last_edited_date "last_edited_date" true true false 8 Date 0 0,First,#,Local Datasets\Other Type of Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Asphalt Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Concrete Pavement Condition Assessment,LAST_EDITED_DATE,-1,-1,Local Datasets\Paver Condition Assessment,LAST_EDITED_DATE,-1,-1", subtype="", expression="")

# Process: Intersect (4)
arcpy.Intersect_analysis(in_features=r"'C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\MDOT MPA\Python tool\Transfer for David Starr\Transfer for David Starr\MPA\DODB12(1).sde\MPA_USER.PCA_POLYGONS' #;'C:\Users\dstarr\OneDrive - Johnson, Mirmiran & Thompson\Projects\temp\PCA_DATA.gdb\OTHER_PCA' #", out_feature_class=OTHER_PCA_Updates, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")

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

# Process: Conc Calc Cond
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer__3_, field="MPA_USER.PCA_POLYGONS.CONDITION", expression="!CONCRETE_PCA_Updates.CONDITION_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Calculate Field (2)
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer__4_, field="COND_LABEL", expression="Reclass(!MPA_USER.PCA_POLYGONS.CONDITION!)", expression_type="PYTHON3", code_block="def Reclass(field):
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

# Process: Asphalt Calc Cond
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer1__7_, field="MPA_USER.PCA_POLYGONS.CONDITION", expression="!ASPHALT_PCA_Updates.CONDITION_1!", expression_type="PYTHON_9.3", code_block="")

# Process: Calculate Field (3)
arcpy.CalculateField_management(in_table=AREAS_PCA_Layer1__4_, field="COND_LABEL", expression="Reclass(!MPA_USER.PCA_POLYGONS.CONDITION!)", expression_type="PYTHON3", code_block="def Reclass(field):
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

