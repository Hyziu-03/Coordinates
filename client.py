from pyproj import Transformer

# CRS stands for Coordinate Reference System
# UTM stands for Universal Transverse Mercator
# WGS 84 stands for World Geodetic System 1984
# EPSG stands for European Petroleum Survey Group

epsg_codes = {
    "pseudo_mercator": 3857,
    "world_geodetic_system": 4326,
    "poland_cs2000": {
        "15_meridian": 2176,
        "18_meridian": 2177,
        "21_meridian": 2178,
        "24_meridian": 2179,
    },
    "poland_cs1992": 2180
}

print("Welcome to the CRS converter!")

print("Select the input CRS:")
print("[1] Pseudo-Mercator")
print("[2] World Geodetic System")
print("[3] Poland CS2000")
print("[4] Poland CS1992")
print("[5] Quit")

code = int(input("Enter your choice: "))
if(code == 1):
    code = epsg_codes["pseudo_mercator"]
elif(code == 2):
    code = epsg_codes["world_geodetic_system"]
elif(code == 3):
    code = epsg_codes["poland_cs2000"]
elif(code == 4):
    code = epsg_codes["poland_cs1992"]
elif(code == 5):
    exit()
else:
    print("Script received invalid input")

print("Select the output CRS:")
print("[1] Pseudo-Mercator")
print("[2] World Geodetic System")
print("[3] Poland CS2000")
print("[4] Poland CS1992")
print("[5] Quit")

output = int(input("Enter your choice: "))
if(output == 1):
    output = epsg_codes["pseudo_mercator"]
elif(output == 2):
    output = epsg_codes["world_geodetic_system"]
elif(output == 3):
    output = epsg_codes["poland_cs2000"]
elif(output == 4):
    output = epsg_codes["poland_cs1992"]
elif(output == 5):
    exit()
else:
    print("Script received invalid input")

longitude = float(input("Enter the longitude: "))
latitude = float(input("Enter the latitude: "))
transformer = Transformer.from_crs(input, output, always_xy=True)
coordinates = transformer.transform(longitude, latitude)
