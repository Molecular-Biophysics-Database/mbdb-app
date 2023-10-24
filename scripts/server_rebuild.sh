#! /bin/bash

# stop and remove docker containers (curtesy of Michal Maly)

OUT=$(docker ps --all)

while IFS= read -r LINE; do
	ID=$(echo "$LINE" | awk -F" " '{ print $1 }')
	if [ "$ID" == "CONTAINER" ]; then
		continue;
	fi

	echo "Stopping container ${ID}..."
	docker stop "$ID"
	if [ $? != 0 ]; then
		echo "WARN: Failed to stop container ${ID}. Manual intervention is required..."
		continue
	fi

	echo "Removing container ${ID}..."
	docker rm "$ID"
	if [ $? != 0 ]; then
		echo "WARN: Failed to remove container ${ID}. Manual intervention is required..."
		continue
	fi
done <<< "$OUT"

echo "Done removing all Docker containters. If the script reported any warning, you will have to remove the problematic containers by hand..."

# go to root of the mbdb-app folder
cd ..

# remove old requirements if present
rm -Rdf .venv sites/mbdb-site/.venv sites/mbdb-site/requirements.txt .assets node_modules

# remove old models
#echo "removing models"
#ls -d models/*/ | xargs sudo rm -Rd

# rebuild server
echo "rebuilding server"

./nrp build
if [ $? != 0 ]; then
    echo "Failed to build server, exiting..."
    exit 1
fi


./nrp develop
if [ $? != 0 ]; then
    echo 'Failed to develop the server, exiting...'
    exit 1
fi
