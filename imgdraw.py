import sys
from PIL import Image

imgfile = ""

try:
    imgfile = sys.argv[1]
except:
    print("Usage: see README")
    sys.exit()

map = Image.open(imgfile)
map = map.resize((map.size[0]*5,map.size[1]*5))
