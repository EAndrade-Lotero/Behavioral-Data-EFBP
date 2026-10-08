'''Folders used by the notebooks. Paths are anchored at the repo root, not the working directory.'''
from pathlib import Path

# src/Config/config.py -> repository root
ROOT = Path(__file__).resolve().parents[2]

PATHS = {
    'index_path': ROOT / 'data' / 'indices',  # fitted alternation-index models
    'human_data': ROOT / 'data',  # session CSVs read by the figure notebooks
    'exploratory_figures': ROOT / 'images' / 'exploratory',
    'focal_regions_path': ROOT / 'data' / 'focal_regions',
    'empirical_focal_regions_path': ROOT / 'data' / 'empirical_focal_regions',
}

for folder in PATHS.values():
    folder.mkdir(parents=True, exist_ok=True)
