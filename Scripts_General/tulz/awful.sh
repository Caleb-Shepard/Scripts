#!/bin/sh
# only working on Apple operating systems with pbcopy
# run the sponge install script before using this
./aesthetic $(sponge $*) | pbcopy
