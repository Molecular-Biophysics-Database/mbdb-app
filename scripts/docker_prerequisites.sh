#!/bin/bash
set -e

echo "Installing docker prerequisites..."

apt-get update
apt-get install -y --no-install-recommends \
    wkhtmltopdf \
    fonts-dejavu \
    fonts-liberation \
    libxrender1 \
    libxext6 \
    libfontconfig1 \
    ca-certificates

apt-get clean
rm -rf /var/lib/apt/lists/*
