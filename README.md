# Behavioral Data EFBP

This repository holds the human session data from the El Farol bar experiment and the code that turns those sessions into the paper figures. Raw play files are combined into one table of decisions, scores, and thresholds. An alternation index, trained on synthetic attendance series, labels each session as alternation, segmentation, mixed, or random. The notebooks then use those labels to plot representative games and to compare efficiency, inequality, and scores across group size and threshold.

## Directory structure

```
.
├── data/                  # raw sessions, combined tables, fitted index
│   └── indices/
├── images/exploratory/    # saved figures
├── notebooks/
│   ├── Preprocessing.ipynb
│   ├── generate_alternation_index.ipynb
│   ├── generate_alternation_index_simple.ipynb
│   ├── Fig2A.ipynb
│   ├── Fig2BandC.ipynb
│   └── Fig3.ipynb
├── src/                   # index, measures, and agent classes
│   ├── Classes/
│   ├── Config/
│   └── Utils/
└── requirements.txt
```

## How to run

From the repository root:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Open the notebooks from `notebooks/` so `../src` is on the path. Run them in this order:

1. `Preprocessing.ipynb` builds `data/multi-player.csv`.
2. `generate_alternation_index.ipynb` fits the index and writes it to `data/indices/`. `generate_alternation_index_simple.ipynb` is the same pipeline on a small sample.
3. `Fig2A.ipynb`, `Fig2BandC.ipynb`, and `Fig3.ipynb` read the saved MLP and write figures to `images/exploratory/`.
