#!/bin/sh
#only working on Apple operating systems with pbcopy
./aesthetic $(./sponge.pdf.exe $(./b $*)) | pbcopy
