import re


WRITE_KEYWORDS = re.compile(r"\b(insert|update|delete|drop|alter|truncate|create|grant|revoke|copy|call|do)\b", re.IGNORECASE)


def validate_read_only_sql(sql: str) -> str:
    cleaned = sql.strip().rstrip(";").strip()
    if not cleaned:
        raise ValueError("SQL is required")
    if ";" in cleaned:
        raise ValueError("Only a single SQL statement is allowed")
    if not re.match(r"^(select|with)\b", cleaned, re.IGNORECASE) or WRITE_KEYWORDS.search(cleaned):
        raise ValueError("Only read-only SELECT queries are allowed")
    return cleaned
