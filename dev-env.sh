#!/bin/bash

set -o allexport
source dev.env

[[ -f local.env ]] && source local.env

[[ -f venv/bin/activate ]] && source venv/bin/activate
