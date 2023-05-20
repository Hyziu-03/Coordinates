from epsg_codes import epsg_codes
from pyproj import Transformer

print("Welcome to the CRS converter!")

def main():
    while (True):
        print("* * * * * * * *")
        print("Select the input CRS:")
        print("[1] Pseudo-Mercator")
        print("[2] World Geodetic System")
        print("[3] Poland CS2000")
        print("[4] Poland CS1992")
        print("[5] Quit")

        try:
            code = int(input("Enter your choice: "))

            if (code == 1):
                code = epsg_codes["pseudo_mercator"]
            elif (code == 2):
                code = epsg_codes["world_geodetic_system"]
            elif (code == 3):
                code = epsg_codes["poland_cs2000"]
            elif (code == 4):
                code = epsg_codes["poland_cs1992"]
            elif (code == 5):
                exit()
            else:
                print("Script received invalid input ❌")
                continue

            print("Select the output CRS:")
            print("[1] Pseudo-Mercator")
            print("[2] World Geodetic System")
            print("[3] Poland CS2000")
            print("[4] Poland CS1992")
            print("[5] Quit")

            output = int(input("Enter your choice: "))

            if (output == 1):
                output = epsg_codes["pseudo_mercator"]
            elif (output == 2):
                output = epsg_codes["world_geodetic_system"]
            elif (output == 3):
                output = epsg_codes["poland_cs2000"]
            elif (output == 4):
                output = epsg_codes["poland_cs1992"]
            elif (output == 5):
                exit()
            else:
                print("Script received invalid input ❌")
                continue

            if (code == output):
                print("Input CRS is the same as output CRS ❌")
                continue

        except ValueError:
            print("Script received invalid input ❌")
            continue

        try:
            latitude = float(input("Enter the latitude: "))
            longitude = float(input("Enter the longitude: "))

        except ValueError:
            print("Script received invalid input ❌")
            continue

        transformer = Transformer.from_crs(code, output, always_xy=True)
        coordinates = transformer.transform(longitude, latitude)
        print(f"The transformed coordinates are: {coordinates}")

if __name__ == "__main__":
    main()
