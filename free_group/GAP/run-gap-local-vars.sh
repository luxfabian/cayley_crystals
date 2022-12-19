#!/usr/bin/env bash

# Copy this file to \Users\<Username>\AppData\Local\GAP-4.12.1\runtime
# Adapt for your version of gap 

cd /cygdrive/c/$1
/opt/get-4.12.1/gap -b -q <<EOI

Read("$2");
quit;

EOI