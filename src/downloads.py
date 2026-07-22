from pathlib import Path


def resolve_download_path(download_root: Path, requested_path: str) -> Path:
    """Resolve a user-supplied path while keeping it inside the download root."""
    root = download_root.resolve()
    candidate = (root / requested_path).resolve()

    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError("requested path escapes the download root") from exc

    return candidate
