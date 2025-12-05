import fontforge
import sys

def strip_ligatures(font_path):
    print(f"Opening font: {font_path}")
    font = fontforge.open(font_path)
    
    lookups = font.gsub_lookups
    print(f"Found {len(lookups)} GSUB lookups via Python API.")
    
    to_remove = []
    
    for lookup in lookups:
        info = font.getLookupInfo(lookup)
        # info structure: (type, flags, feature_tuples)
        # feature_tuples: ((tag, script, lang), ...)
        if not info:
            continue
            
        features = info[2]
        for feature in features:
            tag = feature[0]
            if tag == 'calt':
                to_remove.append(lookup)
                break
    
    print(f"Found {len(to_remove)} 'calt' lookups to remove.")
    
    for lookup in to_remove:
        try:
            font.removeLookup(lookup)
        except Exception as e:
            print(f"Error removing lookup {lookup}: {e}")

    print(f"Generating font: {font_path}")
    font.generate(font_path)
    font.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fontforge -lang=py -script strip_ligas.py <font_path>")
        sys.exit(1)
        
    strip_ligatures(sys.argv[1])
