#!/bin/sh

arm-linux-gnueabi-as $1
arm-linux-gnueabi-ld a.out -o $2

rm a.out

