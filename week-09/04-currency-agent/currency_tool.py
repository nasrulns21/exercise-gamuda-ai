from dataclasses import dataclass
import json
from typing import Callable
from urllib.request import urlopen


@dataclass(frozen=True)
class ExchangeRate:
    base: str
    quote: str
    rate: float
    date: str


def http_json(url: str) -> dict:
    with urlopen(url, timeout=15) as response:
        return json.load(response)


def fetch_exchange_rate(base: str, quote: str, client: Callable[[str], dict] = http_json) -> ExchangeRate:
    base = base.upper().strip()
    quote = quote.upper().strip()
    if len(base) != 3 or len(quote) != 3:
        raise ValueError("Currency codes must contain three letters")
    data = client(f"https://api.frankfurter.app/latest?from={base}&to={quote}")
    if quote not in data.get("rates", {}):
        raise ValueError(f"No rate returned for {base}/{quote}")
    return ExchangeRate(base, quote, float(data["rates"][quote]), data["date"])


if __name__ == "__main__":
    result = fetch_exchange_rate("USD", "MYR")
    print(f"1 {result.base} = {result.rate} {result.quote} ({result.date})")
