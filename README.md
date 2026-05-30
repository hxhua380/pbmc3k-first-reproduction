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

## Output Check

After running the script, check that the output figure exists:

python -c "from pathlib import Path; p=Path('results/pbmc3k_umap_clusters.png'); assert p.exists(), 'Output figure does not exist'; print(p)"

Check that the image is not an empty or broken file:

python -c "from pathlib import Path; p=Path('results/pbmc3k_umap_clusters.png'); assert p.stat().st_size > 50000, f'Image too small: {p.stat().st_size} bytes'; print('image size looks OK:', p.stat().st_size)"

## VS Code Debugging Notes

Useful breakpoint locations:

- adata = load_data()
    - pause before loading the dataset
- adata = run_analysis(adata)
    - pause before PCA, UMAP, and clustering
- print("Saving result figure...")
    - pause after analysis and before saving the figure

Useful Debug Console commands:

adata.n_obs
adata.n_vars
list(adata.obsm.keys())
list(adata.obsp.keys())
adata.obsm["X_umap"].shape
adata.obs["cluster"].value_counts()

What these mean:

- adata.n_obs: number of cells
- adata.n_vars: number of genes
- adata.obsm["X_umap"].shape: UMAP coordinate matrix shape
- adata.obs["cluster"].value_counts(): number of cells in each cluster

## Troubleshooting Notes

A script can print Done even when the output figure is wrong.

In this project, an empty figure was created when the script saved the current Matplotlib canvas with plt.savefig(...).

The fix was to ask Scanpy to return the figure explicitly:

fig = sc.pl.umap(..., show=False, return_fig=True)
fig.savefig(OUTPUT_FIGURE, dpi=150, bbox_inches="tight")
plt.close(fig)