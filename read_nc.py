"""Simple NetCDF (.nc) reader example.

Usage:
    python read_nc.py /path/to/file.nc
"""

from __future__ import annotations

import argparse
from pathlib import Path

import xarray as xr


def read_nc_file(file_path: str) -> xr.Dataset:
    """Read a NetCDF file and return an xarray Dataset."""
    return xr.open_dataset(file_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Read and preview a NetCDF file.")
    parser.add_argument("nc_file", type=Path, help="Path to .nc file")
    args = parser.parse_args()

    dataset = read_nc_file(str(args.nc_file))
    print("=== Dataset Overview ===")
    print(dataset)
    print("\n=== Variables ===")
    print(list(dataset.data_vars))


if __name__ == "__main__":
    main()
