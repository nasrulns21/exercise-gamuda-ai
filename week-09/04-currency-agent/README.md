# Currency Exchange Tool Agent

Adds a current exchange-rate API tool to an agent. The default example requests the USD to MYR rate from the public Frankfurter API.

`currency_tool.py` keeps the HTTP client injectable so parsing can be tested without a live request. `agent.py` shows how the function is exposed to LangChain.
