# PDF Vector Store

Creates the second MongoDB Atlas vector index requested in the RAG exercise:

- Database: `test_db`
- Collection: `test_collection_pdf`
- Index: `test-index-pdf`
- Dimensions: `768`

Set `GEMINI_API_KEY` and `MONGODB_ATLAS_CLUSTER_URI`, then run `python create_index.py`. Place the supplied document at `diabetes.pdf` and run `python index_pdf.py` to split and store its pages. The account-backed Atlas result must be checked manually.
