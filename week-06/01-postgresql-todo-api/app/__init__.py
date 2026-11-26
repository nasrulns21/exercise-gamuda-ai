"""PostgreSQL todo training API."""

import os

# Some managed Windows computers block SQLAlchemy's optional compiled extension.
# The pure-Python implementation provides the same behaviour for this exercise.
os.environ.setdefault("DISABLE_SQLALCHEMY_CEXT_RUNTIME", "1")
