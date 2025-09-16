#!/bin/bash -e

# Generate html docs
make clean
make html

# Package into a .war file
cd maven && mvn clean package
