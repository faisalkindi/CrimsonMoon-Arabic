#!/bin/bash
# Build + install IoStore triple for Crimson Moon Arabic mod. Usage: ./build_mod.sh <staging_dir> <ModName>
set -e
G="/f/SteamLibrary/steamapps/common/Crimson Moon/CrimsonMoonNG/Content/Paks"
S="$1"; N="${2:-zzz_Arabic_P}"; O="$(dirname "$0")/build"
/c/Users/Faisal/Ai/Tools/repak/repak.exe pack --version V11 --mount-point ../../../ --compression Oodle -p 2962377397 "$S" "$O/$N.pak" -q
cp "$G/global.ucas" "$O/$N.ucas"; cp "$G/global.utoc" "$O/$N.utoc"
cp "$O/$N.pak" "$O/$N.ucas" "$O/$N.utoc" "$G/"
/c/Users/Faisal/Ai/Tools/repak/repak.exe info "$O/$N.pak" | grep -E "seed|entries"
