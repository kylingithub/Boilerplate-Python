# use uv to create a virtual environment and install the dependencies
uv venv
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt

source .venv/bin/activate