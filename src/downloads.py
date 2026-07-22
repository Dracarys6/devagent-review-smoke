from pathlib import Path


def resolve_download_path(download_root: Path, requested_path: str) -> Path:
    """Resolve a user-supplied path under the download root."""
    root = download_root.resolve()
    return (root / requested_path).resolve()
