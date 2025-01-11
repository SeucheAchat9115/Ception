#!/bin/bash
echo "Creating virtual environment and installing dependencies"
python -m venv cp-venv
source cp-venv/bin/activate
echo "Venv created under cp-venv"
echo "Installing project using poetry"
poetry install
pre-commit install
echo "Project installed"
