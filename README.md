# Exercise Gamuda AI

This private repository documents my Gamuda AI training exercises for personal learning evidence and JPSM review. Work is organised by training week, with an [exercise checklist](EXERCISE-COVERAGE.md) that distinguishes completed local work from exercises requiring an external service.

## Repository structure

| Week | Topics | Main exercises |
| --- | --- | --- |
| [Week 1](week-01/) | HTML, CSS, and JavaScript basics | Tables, team-member data, and capstone user stories |
| [Week 2](week-02/) | JavaScript control flow and React components | Conditions, switch statements, functions, JSX, product cards, and user cards |
| [Week 3](week-03/) | React component communication | Restaurant menu mini-project and Week 2 component cross-references |
| [Week 4](week-04/) | React state, routing, events, and conditional rendering | State exercises, router patterns, keyboard interactions, and Lottie challenge |
| [Week 5](week-05/) | Effects, APIs, Python, deployment, and FastAPI | Four React apps, four Python exercises, Firebase config, and Library API |
| [Week 6](week-06/) | PostgreSQL, routers, and full-stack integration | Todo CRUD, router exercises, and React/FastAPI book manager |
| [Week 7](week-07/) | Generative AI and prompt engineering | Translation, parameter/role experiments, parsing, and summarisation |
| [Week 8](week-08/) | Multimodal analytics | Image UI and four-mode video analysis prompts |
| [Week 9](week-09/) | RAG, AI agents, and MCP | PDF chatbot, agent memory, middleware, remote search, and read-only database tools |

## How to use this repository

Each week has its own README and every trainer-note exercise is separated into a numbered folder. My earlier submissions are retained beside the completed exercise folders and labelled clearly.

Repository-level checks:

```powershell
npm install
npm test
npm run verify
```

Local secrets are intentionally excluded. Where an exercise needs an API key or database password, copy the relevant `.env.example` file to `.env` and provide your own value.

## Notes

- The trainer slides were used only as a reference and are not included in this repository.
- Virtual environments, dependencies, build outputs, caches, and local secret files are excluded.
- The original exercise folders remain unchanged; numbered folders contain the completed trainer-note exercises.
- Firebase, MongoDB Atlas, live PostgreSQL, Tavily, LangSmith, and live Gemini calls remain explicit external checkpoints because they require an authorised account or service.

