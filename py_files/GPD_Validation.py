import geopandas as gpd

# Import Ground Truth Points
# Import Detected Points

ground_truth = gpd.read_file(r'E:\SIB\Model_Validation\Validation_Model2_Sample\Ground Truth\GroundTruth\GT\groundTruth_vhrValidationV1.shp')
detected_points = gpd.read_file(r'E:\SIB\Model_Validation\Validation_Model2_Sample\Ground Truth\Detected\Model2a_Detected\model2a_VHRDetection.shp')

ground_truth = ground_truth.to_crs("EPSG:29902")
detected_points = detected_points.to_crs("EPSG:29902")
print(ground_truth.crs)

detected_points.plot(color='red')