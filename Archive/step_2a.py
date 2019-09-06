#Script Parameter

arcpy.env.workspace = arcpy.GetParameterAsText(5)

#Local Variables
MPA_USER_PCA_POLYGONS = "MPA_USER.Geotechnical"

PAVERS_PCA_Updates = "PAVERS_PCA_Updates"
CONCRETE_PCA_Updates = "CONCRETE_PCA_Updates"
ASPHALT_PCA_Updates = "ASPHALT_PCA_Updates"
OTHER_PCA_Updates = "OTHER_PCA_Updates"

intersect_variable_paver = "'" + MPA_USER_PCA_POLYGONS + "'#;" + PAVERS_PCA_Updates + "#"
intersect_variable_concrete = "'" + MPA_USER_PCA_POLYGONS + "'#;" + CONCRETE_PCA_Updates + "#"
intersect_variable_asphalt = "'" + MPA_USER_PCA_POLYGONS + "'#;" + ASPHALT_PCA_Updates + "#"
intersect_variable_other = "'" + MPA_USER_PCA_POLYGONS + "'#;" + OTHER_PCA_Updates + "#"


#Process: Intersect Pavers
arcpy.Intersect_analysis(in_features=intersect_variable_paver, out_feature_class=PAVERS_PCA_Updates, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")

# Process: Intersect Concrete
arcpy.Intersect_analysis(in_features=intersect_variable_concrete, out_feature_class=CONCRETE_PCA_Updates, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")

# Process: Intersect Asphalt
arcpy.Intersect_analysis(in_features=intersect_variable_asphalt, out_feature_class=ASPHALT_PCA_Updates, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")

# Process: Intersect Other
arcpy.Intersect_analysis(in_features=intersect_variable_other, out_feature_class=OTHER_PCA_Updates, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")