# -*- coding: utf-8 -*-
"""Generated by ArcGIS ModelBuilder on: 2019-09-03 13:43:35
All ModelBuilder functionality may not be exported. Edits may be required for equivalency with the original model.
"""

import arcpy

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

# Local variables:
merged_PCA_Updates_SpatialJo__2_ = "merged_PCA_Updates_SpatialJo"
merged_PCA_Updates_SpatialJo = merged_PCA_Updates_SpatialJo__2_
Count = "0"

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(in_layer_or_view=merged_PCA_Updates_SpatialJo__2_, selection_type="NEW_SELECTION", where_clause="Join_Count >= 2", invert_where_clause="")

