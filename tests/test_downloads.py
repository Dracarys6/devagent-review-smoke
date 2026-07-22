from pathlib import Path

import pytest

from downloads import resolve_download_path


def test_resolves_path_inside_download_root(tmp_path: Path) -> None:
    assert resolve_download_path(tmp_path, "reports/result.txt") == (
        tmp_path / "reports/result.txt"
    )


def test_rejects_path_outside_download_root(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="escapes"):
        resolve_download_path(tmp_path, "../secrets.txt")
