# Exercise Inventory

This inventory records how the completed exercise files were organised for the repository.

The complete trainer-note requirement map is maintained in [`EXERCISE-COVERAGE.md`](../EXERCISE-COVERAGE.md). Existing student work remains traceable, while completed versions are organised in numbered weekly folders.

| Repository location | Original source | Training topic |
| --- | --- | --- |
| `week-01/html-css` | `Week 2` HTML and CSS files | HTML and CSS fundamentals |
| `week-01/javascript-basics` | `Week 2/index.html` | JavaScript variables, objects, arrays, and team member data |
| `week-02/javascript-control-flow` | `Week 2` control-flow and function files | Original student work retained for conditions, switch statements, and functions |
| `week-02/react-components` | `Week 2/my-project` | Original student Vite/React project retained for JSX and reusable components |
| `week-05/python-basics` | `Python` | Python temperature converter |
| `week-05/fastapi-introduction` | `Week 5/Backend` | FastAPI introduction |
| `week-05/useeffect-react` | `Week 5/useeffect-react` | `useEffect` and side effects |
| `week-05/news-aggregator` | `Week 5/news-aggregator` | API integration and data fetching |
| `week-06/postgresql-crud-api` | `PostgreSQL` root Python files | FastAPI authentication demo with PostgreSQL configuration and commented CRUD examples |
| `week-07` | `Week 7` | Generative AI, translation, and prompt engineering |
| `week-08` | `Week 8` | Video analytics |
| `week-09/original-work` | `Week 9` | Original RAG and tool-calling Python exercises, excluding `.env` |

## Excluded material

- Trainer notes and slides: reference material only.
- `.env` files: may contain API keys or other private values.
- `.venv`, `venv`, `node_modules`, `.next`, `dist`, `build`, `__pycache__`, and `.git`: machine-specific, generated, dependency, cache, or nested repository data.
- Empty folders, zero-byte files, incomplete templates, and broken integration examples: no completed exercise content to document.
- `Fail Halal` and `Penulisan Pro Threads`: not directly mapped to a weekly exercise in the supplied trainer notes, so they remain outside this exercise repository.

## Copy adjustments

The copied PostgreSQL exercise now reads its database password from the `DB_PASSWORD` environment variable. The original source file was not changed.

Two Week 5 import paths were normalised to match the lowercase filenames on case-sensitive systems. The original source files were not changed.

