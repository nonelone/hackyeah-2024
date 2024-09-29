#!/bin/bash

podman build -t aegis .
podman run -p 5000:5000 aegis
