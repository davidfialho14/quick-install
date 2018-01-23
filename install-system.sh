#!/usr/bin/env bash
set -e

VENV="venv"
PIP="${VENV}/bin/pip"
PYTHON="venv/bin/python"

cd $(dirname $0)

if [ ! -d "${VENV}" ]; then
    sudo apt-get install -yqq python3-pip python3-venv
    python3 -m venv ${VENV}
    ${PIP} install wheel
    ${PIP} install -r requirements.txt
    ${PIP} install . --upgrade
    echo ""
fi

sudo ${PYTHON} quick_installer/cli.py system
