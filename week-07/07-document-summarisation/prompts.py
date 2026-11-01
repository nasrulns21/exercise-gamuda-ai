FORMATS = {"report":"purpose, findings, risks, and actions", "meeting":"decisions, owners, and deadlines", "technical":"scope, method, results, and limitations"}
def build_prompt(document_type, text): return f"Summarise this {document_type} using {FORMATS[document_type]}:\n{text}"
def summarise(client, document_type, text): return client.generate(build_prompt(document_type, text))
