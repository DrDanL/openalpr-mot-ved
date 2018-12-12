from openalpr import Alpr

alpr = Alpr("gb", "D:\dev\openalpr-mot-ved\openalpr.conf.user", "D:\dev\openalpr-mot-ved\runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
else:
    print("OpenALPR loaded successfully")

#Optionally specify the top N possible plates to return (with confidences).  Default is 10
alpr.set_top_n(1)

#Optionally, provide the library with a region for pattern matching.
#This improves accuracy by comparing the plate text with the regional pattern.
alpr.set_default_region("gb")
