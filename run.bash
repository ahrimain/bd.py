echo "cheking .output"
if [ -d ./.output/ ]; then
    echo ".output exists"
else
    echo "no .output \n making .output"
    mkdir .output
    echo "made .output"
fi

echo "build index.html"
python3 run.py > .output/index.html