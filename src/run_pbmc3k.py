from pathlib import Path

import matplotlib.pyplot as plt
import scanpy as sc

# 自动找到项目根目录 & 结果目录
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "results"
OUTPUT_FIGURE = RESULTS_DIR / "pbmc3k_umap_clusters.png"


def load_data():
    """加载 Scanpy 自带的公开 PBMC3k 数据集（已经预处理好）"""
    adata = sc.datasets.pbmc3k_processed()
    return adata


def run_analysis(adata):
    """运行：PCA → 邻居计算 → UMAP → 聚类"""
    sc.tl.pca(adata, svd_solver="arpack")
    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
    sc.tl.umap(adata)
    sc.tl.leiden(adata, resolution=0.5, key_added="cluster")
    return adata


def save_plot(adata):
    """画 UMAP 图并保存到 results 文件夹"""
    RESULTS_DIR.mkdir(exist_ok=True)

    fig = sc.pl.umap(
        adata,
        color="cluster",
        legend_loc="on data",
        title="PBMC3k UMAP clusters",
        show=False,
        return_fig=True
    )

    fig.savefig(OUTPUT_FIGURE, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main():
    print("Loading PBMC3k data...")
    adata = load_data()

    print(f"Data shape: {adata.n_obs} cells x {adata.n_vars} genes")

    print("Running PCA, UMAP, and Leiden clustering...")
    adata = run_analysis(adata)

    print("Saving result figure...")
    save_plot(adata)

    print(f"Done: {OUTPUT_FIGURE}")


if __name__ == "__main__":
    main()