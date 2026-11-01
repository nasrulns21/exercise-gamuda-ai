FORMATS = {"bullets":"concise bullet points", "takeaways":"five key takeaways", "qa":"questions and answers"}
def build_prompt(url, output_format): return f"Summarise {url} as {FORMATS[output_format]}. Cite only information present on the page."
def summarise(client, url, output_format): return client.generate(build_prompt(url, output_format))
