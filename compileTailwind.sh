#! /bin/bash
ln -s .venv/var/instance/assets/node_modules .
npx tailwindcss -i ./ui/branding/semantic-ui/less/tailwindcss/input.css -o ./ui/branding/semantic-ui/less/tailwindcss/output.css $@