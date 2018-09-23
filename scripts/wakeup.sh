#!/bin/bash

MAC=$1
HOST=$2

wol -h ${HOST} ${MAC}