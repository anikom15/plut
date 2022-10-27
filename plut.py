#!/usr/bin/python3

#  Copyright 2022 W. M. Martinez
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License. 

import sys

phosphors = {'p1.cube': [0.218, 0.712],
             'p2.cube': [0.279, 0.534],
             'p3.cube': [0.523, 0.469],
             'p4.cube': [0.265, 0.285]}

XYZ_TO_sRGB = (( 3.2406255, -1.5372080, -0.4986286),
               (-0.9689307,  1.8758561,  0.0415175),
               ( 0.0557101, -0.2040211,  1.0569959))

for key, value in phosphors.items():
    phosphors[key].append(1 - value[0] - value[1])

def linear(rgb):
    return [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4
            for x in rgb]

def gamma(rgb):
    return [12.92 * x if x <= 0.0031308 else x ** (1 / 2.4) * 1.055 - 0.055
            for x in rgb]

def main(x, y, z, fileout):
    Min = None
    Max = None

    # Gain
    X = 1.0 / y * x
    Z = 1.0 / y * z
    Ygain = 1.0 / max([XYZ_TO_sRGB[i][0] * X
                     + XYZ_TO_sRGB[i][1]
                     + XYZ_TO_sRGB[i][2] * Z
                     for i in range(0, 3)]) 
    for line in main.lines:
        rgb = line.split(' ', 3)
        try:
            rgb = [float(x) for x in rgb]
        except:
            print(line, end='', file=fileout)
            continue
        rgb = linear(rgb)
        Y = Ygain * (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2])
        X = Y / y * x
        Z = Y / y * z
        rgb = gamma([XYZ_TO_sRGB[i][0] * X
                   + XYZ_TO_sRGB[i][1] * Y
                   + XYZ_TO_sRGB[i][2] * Z
                   for i in range(0, 3)])
        for c in rgb:
            Min = c if Min is None or Min > c else Min
            Max = c if Max is None or Max < c else Max
        print("%f %f %f" % (rgb[0], rgb[1], rgb[2]), file=fileout)
    print("Gain: %f" % Ygain, file=sys.stderr)
    if Min is not None:
        print("Min: %f" % Min, file=sys.stderr)
    if Max is not None:
        print("Max: %f" % Max, file=sys.stderr)

main.lines = []
for line in sys.stdin:
    main.lines.append(line)
for key, value in phosphors.items():
    with open(key, 'w') as f:
        print(key, file=sys.stderr)
        main(*value, f)
        print(file=sys.stderr)
