# =====================================
# generator=datazen
# version=3.2.4
# hash=8f6d1d8a36bedb093be854f12bdb5200
# =====================================

"""
Useful defaults and other package metadata.
"""

DESCRIPTION = "Compile and render schema-validated configuration data."
PKG_NAME = "datazen"
VERSION = "3.2.4"

# datazen-specific content.
DEFAULT_TYPE = "yaml"
DEFAULT_MANIFEST = f"manifest.{DEFAULT_TYPE}"
DEFAULT_DIR = f"{PKG_NAME}-out"
DEFAULT_INDENT = 2
CACHE_SUFFIX = "_cache"
GLOBAL_KEY = "global"


def to_private(input_str: str) -> str:
    """Convert some input to a 'private' String."""

    return f"__{input_str}__"


ROOT_NAMESPACE = to_private("root")
