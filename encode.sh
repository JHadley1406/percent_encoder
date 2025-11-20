#!/bin/zsh

source ~/Projects/python/percent_encoder/.venv/bin/activate

python ~/Projects/python/percent_encoder/encoder.py $1

deactivate
