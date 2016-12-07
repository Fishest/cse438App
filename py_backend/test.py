from flask import Flask, request, jsonify
import math
from test_db import *
import signal, sys

geocode = [['6170 Pershing Ave, St. Louis, MO 63112, USA', [38.649623, -90.299644]], ['605 Leland Ave, University City, MO 63130, USA', [38.65639840000001, -90.30617099999999]], ['Kemper Art Museum, 1 Brookings Dr, University City, MO 63130, USA', [38.6470653, -90.30263459999999]], ['Mallinckrodt Center', [38.6469085, -90.3111762]]]


ave_x = sum(geo[1][0] for geo in geocode) / len(geocode)
ave_y = sum(geo[1][1] for geo in geocode) / len(geocode)
print(ave_x, ave_y)
for i in range(len(geocode)):
    x = geocode[i]
    print(math.atan( (x[1][0] - ave_x) / (x[1][1] - ave_y + 0.0000000001) ) )
#sorted(geocode, key=lambda x: math.atan( (x[1][0] - ave_x) / (x[1][1] - ave_y + 0.0000000001) ) )
sorted(geocode, key=lambda x: x[0])
for i in range(len(geocode)):
    x = geocode[i]
    print(math.atan( (x[1][0] - ave_x) / (x[1][1] - ave_y + 0.0000000001) ) )
for i in range(len(geocode)):
    if geocode[i][0] == "Mallinckrodt Center":
        index = i
        break
print(geocode)
