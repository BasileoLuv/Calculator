#!/bin/bash
BUILD_DATE=$(grep build.date target/classes/build.properties | cut -d= -f2)
echo "$BUILD_DATE"