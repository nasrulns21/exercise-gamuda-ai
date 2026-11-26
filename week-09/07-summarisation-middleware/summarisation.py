def compact_history(messages: list[dict[str, str]], keep_recent: int = 4) -> list[dict[str, str]]:
    if keep_recent < 1:
        raise ValueError("keep_recent must be at least 1")
    if len(messages) <= keep_recent:
        return list(messages)
    older = messages[:-keep_recent]
    recent = messages[-keep_recent:]
    summary = " | ".join(message["content"] for message in older)
    return [{"role": "system", "content": f"Earlier conversation summary: {summary}"}, *recent]
