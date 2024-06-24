#/bin/sh

fabric --update 
cp -R my_patterns/* patterns/
echo "Customised patterns copied successfully."
