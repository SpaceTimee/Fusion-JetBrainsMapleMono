import sys
from fontTools.ttLib import TTFont

maple_font = TTFont(sys.argv[1])
jetbrains_font = TTFont(sys.argv[2])

for glyph in jetbrains_font.getGlyphNames():
    # if glyph in maple_font['glyf'].glyphs:
    maple_font['glyf'].glyphs[glyph] = jetbrains_font['glyf'].glyphs[glyph]
    # if maple_font['glyf'].glyphs[glyph].isComposite():
    #     maple_font['glyf'].glyphs[glyph].expand(jetbrains_font['glyf'])
    if glyph in jetbrains_font['hmtx'].metrics:
        maple_font['hmtx'].metrics[glyph] = jetbrains_font['hmtx'].metrics[glyph]

maple_font.save('merged.ttf')