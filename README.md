# PBMC3k First Reproduction

This is my first minimal reproduction project.

Goal:
1. Download and read a public single-cell expression dataset.
2. Run PCA and UMAP.
3. Cluster cells.
4. Save one result figure.
5. Learn how to read code, debug in VS Code, and write reproducible instructions.

## Project Structure
```text
pbmc3k-first-reproduction/
├─ README.md
├─ .gitignore
├─ src/
│  └─ run_pbmc3k.py
└─ results/
   └─ pbmc3k_umap_clusters.png