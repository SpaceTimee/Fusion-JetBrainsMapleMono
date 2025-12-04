#!/usr/bin/fontforge

import sys
import fontforge

font = fontforge.open(path := sys.argv[1])

for lookup in font.gsub_lookups:
    if (info := font.getLookupInfo(lookup)) and any(feature[0] == "calt" for feature in info[2]):
        font.removeLookup(lookup)

font.generate(path)
font.close()