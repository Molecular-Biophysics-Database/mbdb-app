#! /bin/bash

# go to root of mbdb-app folder
cd ..

# load vocabularies
echo "loading vocabularies"
./nrp oarepo fixtures load

if [ $? != 0 ]; then
    echo "Failed to load vocabularies, exiting..."
    exit 1
fi

# rebuild models
echo "rebuilding models"
MODELS=(mst bli spr)

for mod in ${MODELS[@]}
do
    modname=mbdb-$mod
    ./nrp model add $modname \
       --use mbdb-model/models/oarepo/"${mod^^}".yaml \
       --config scripts/model_configs/$mod-config.yaml \
       --no-input

    ./nrp model compile $modname
    ./nrp model install $modname
    if [ $? != 0 ]; then
        echo "Failed to build model, exiting..."
        exit 1
    fi
    ./nrp oarepo fixtures load --no-system-fixtures $PWD/sample_data/$mod
done
