#!/bin/bash
set -e

mkdir -p fonts/jetbrains fonts/maple merged_fonts

echo "🔽 Downloading JetBrains Mono..."
JETBRAINS_LATEST=$(curl -s https://api.github.com/repos/JetBrains/JetBrainsMono/releases/latest | jq -r '.assets[] | select(.name | test("JetBrainsMono-[0-9.]+.zip")) | .browser_download_url')
wget -O jetbrains-mono.zip "$JETBRAINS_LATEST"
unzip -o jetbrains-mono.zip -d fonts/jetbrains

echo "🔽 Downloading Maple Font..."
MAPLE_LATEST=$(curl -s https://api.github.com/repos/subframe7536/maple-font/releases/latest | jq -r '.assets[] | select(.name | test("MapleMonoNormal-CN-unhinted.zip")) | .browser_download_url')
wget -O maple-font.zip "$MAPLE_LATEST"
unzip -o maple-font.zip -d fonts/maple

echo "🎯 Merging JetBrains Mono & Maple Font..."
for style in Regular Bold Italic Medium Light Thin SemiBold ExtraLight ExtraBold; do
  JETBRAINS_FONT="fonts/jetbrains/fonts/ttf/JetBrainsMono-${style}.ttf"
  MAPLE_FONT="fonts/maple/MapleMonoNormal-CN-${style}.ttf"

  if [[ -f "$JETBRAINS_FONT" && -f "$MAPLE_FONT" ]]; then
    echo "Merging $JETBRAINS_FONT with $MAPLE_FONT..."
    pyftmerge "$MAPLE_FONT" "$JETBRAINS_FONT"
    mv merged.ttf "merged_fonts/JetBrainsMapleMono-${style}.ttf"
  fi
done

echo "✅ Font merging complete!"
