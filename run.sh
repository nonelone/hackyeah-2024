#!/bin/bash

podman build -t aegis .
podman run -d -p 5000:5000 aegis
