rm logs/*
rm -r results/
rm -r sikuli_captured
rm Sikuli_java_std*
rm *.xml
rm *.html
find . -iname '__pycache__' -type d -exec rm -r '{}' \;
find . -iname '.ruff_cache' -type d -exec rm -r '{}' \;
find . -iname '.pytest_cache' -type d -exec rm -r '{}' \;
echo "[!] Pastas de cache, arquivos de debug, todos foram limpos!"