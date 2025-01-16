echo "cheking .output"
if [ -d ./.output/ ]; then
    echo ".output already exists"
    echo "removing"
    rm .output -r
fi
echo "making .output"
mkdir .output
echo "made .output"


echo "cheking pages"
if [ -d ./pages/ ]; then
    echo "pages exists"
else
    echo "no pages \n making pages"
    mkdir pages
    echo "made pages"
fi

echo "building"
mkdir .build
touch .build/pages
python3 run.py
rm .build -r