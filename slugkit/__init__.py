"""slugkit: tiny URL slug helper."""
import re

__all__ = ["slugify"]


def slugify(text, sep="-"):
    """Turn arbitrary text into a URL-safe slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s", sep, text)
    return text.strip(sep)
