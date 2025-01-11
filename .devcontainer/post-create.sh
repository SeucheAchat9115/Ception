#!/bin/bash
echo "Creating virtual environment and installing dependencies"
python -m venv .venv
source .venv/bin/activate
echo "Venv created under .venv"
echo "Installing project using poetry"
poetry install
pre-commit install
echo "Project installed"