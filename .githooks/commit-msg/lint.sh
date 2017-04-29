#!/usr/bin/env bash

echo $@
./node_modules/.bin/conventional-changelog-lint --edit
