#! /bin/bash

# got to the root of the mbdb-app
cd ..

# load vocabularies
echo "loading vocabularies"
./nrp oarepo fixtures load

if [ $? != 0 ]; then
    echo "Failed to load vocabularies, exiting..."
    exit 1
fi

# rebuild models
echo "loading sample data"
MODELS=(mst bli spr)

for mod in ${MODELS[@]}
do
    ./nrp oarepo fixtures load --no-system-fixtures $PWD/sample_data/$mod
done
