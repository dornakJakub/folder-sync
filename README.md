# Folder-sync
## One way folder synchronization tool

Folder-sync is a one way folder synchronization tool, which makes exact replica of source folder and it's contents including file metadata. It does so periodically in interval set by user. Script is designed to use both, absolute and relative paths.

**usage:** main.py [-h] source_path destination_path sync_interval log_path

#### positional arguments:
  **source_path**       - Path to the source directory
  **destination_path**  - Path to the replica directory
  **sync_interval**     - Interval between synchronizations
  **log_path**          - Path to the file containing logs

#### options:
  **-h, --help**        - show help message


**Warning:** The script can run into error if there happens to be file without suffix in the replica folder and there occurs folder with the same path in the source folder. Though this insufficiency should be fixed soon.
