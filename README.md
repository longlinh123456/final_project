# DATA1010 Final Project Group A

## Installation

Please install `uv` (follow instructions at <https://docs.astral.sh/uv/getting-started/installation>).

To create the virtual environment and install the libraries (i.e. when first cloning this repo), run `uv sync`.
Use the virtual environment (located in `.venv`, available after `uv sync`) in this library when developing/running the notebook.

## Committing

`ruff` and `nbdev` are installed to clean and format the Jupyter notebook before committing.

Stage changed files before committing.
The commit may fail; this is because the pre-commit hooks modified the notebook. You should stage the modifications made by the hooks and then commit again.

## Dataset

In order to ensure consistency and reproducibility, do not pull data from the Google form. Instead, use the snapshot of the dataset saved as `dataset.csv`.

## Libraries

You may install additional libraries using `uv` (i.e. `uv add <library name>`) and import them as normal in the notebook.

Further information about `uv` may be found at <https://docs.astral.sh/uv>.
