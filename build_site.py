"""Wrap supernova-pato.html (written for claude.ai, which adds the page skeleton) into a
standalone index.html for GitHub Pages."""
from pathlib import Path

root = Path(__file__).parent
body = (root / "supernova-pato.html").read_text(encoding="utf-8")

head = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<style>
:root { color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); box-sizing: border-box; }
body { margin: 0; font: 14px system-ui, -apple-system, "Segoe UI", sans-serif; }
img { max-width: 100%; }
[hidden] { display: none !important; }
</style>
</head>
<body>
"""

(root / "index.html").write_text(head + body + "\n</body>\n</html>\n", encoding="utf-8")
print("wrote index.html")
