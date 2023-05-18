from pyproj import CRS
from pyproj.aoi import AreaOfInterest
from pyproj.database import query_utm_crs_info
# from pyproj import Transformer

# Defining EPSG codes

# wgs84_code = 4326
# utm_north_america_code = 26917

# crs = CRS.from_epsg(wgs84_code)
# epsg = crs.to_epsg()
# print(f"The chosen code is EPSG:{epsg}")

# authority = crs.to_authority()
# code = authority[0] + ":" + authority[1]
# print(f"The chosen code is {code}")

# Desribing the CRS

utm_crs_list = query_utm_crs_info(
    datum_name = "WGS 84",
    area_of_interest = AreaOfInterest(
        west_lon_degree = -93.581543,
        south_lat_degree = 42.032974,
        east_lon_degree = -93.581543,
        north_lat_degree = 42.032974,
    ),
)

auth = utm_crs_list[0].auth_name
code = utm_crs_list[0].code
print(f"The chosen code is {auth}:{code}")

crs_name = utm_crs_list[0].name
print(f"The chosen CRS is {crs_name}")

is_deprecated = utm_crs_list[0].deprecated
if(is_deprecated):
    print("This CRS is deprecated. It is advised not to use it")

projection_method = utm_crs_list[0].projection_method_name
print(f"The projection method is {projection_method}")

# Transforming coordinates

# longitude = -80
# latitude = 50
# transformer = Transformer.from_crs(wgs84_code, utm_north_america_code, always_xy=True)
# coords = transformer.transform(longitude, latitude)
print(f"The coordinates are as follows: {coords}")

geodetic_cts = CRS.from_epsg(3857).geodetic_crs
projection = Transformer.from_crs(crs.geodetic_crs, crs)
print(f"Projection data: {projection}")
x = 12
y = 15
transformed = projection.transform(x, y)
print(f"Transformed coordinates: {transformed}")
