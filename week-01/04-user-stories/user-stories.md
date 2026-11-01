# Training Portfolio User Stories

## US-01 — Browse work by week

As a JPSM reviewer, I want to browse exercises by training week so that I can assess the learning journey quickly.

**Acceptance criteria:** The root page links to Weeks 1–8; each week page lists its exercises; each link resolves to a reviewable folder.

**Estimate:** 3 story points

**Priority:** Must have

## US-02 — Trace an exercise to its source

As a trainer, I want each exercise to name the trainer-note source so that I can compare the implementation with the requirement.

**Acceptance criteria:** Every exercise README names the delivered week and exercise; duplicate exercises link to one completed implementation.

**Estimate:** 2 story points

**Priority:** Must have

## US-03 — Run an exercise independently

As a technical reviewer, I want exact setup and run commands so that I can reproduce an exercise on a clean machine.

**Acceptance criteria:** Each README lists prerequisites and commands; generated dependencies are excluded; missing environment variables fail safely.

**Estimate:** 5 story points

**Priority:** Must have

## US-04 — Verify completion evidence

As a programme administrator, I want a coverage matrix with evidence so that completion claims can be audited.

**Acceptance criteria:** Every exercise ID appears once; local verification and external checkpoints use distinct statuses; test results are recorded.

**Estimate:** 3 story points

**Priority:** Must have

## US-05 — Review safely on a phone

As a mobile reviewer, I want pages to work at 320px and with a keyboard so that the repository is accessible on common devices.

**Acceptance criteria:** Content does not disappear at 320px; interactive controls have labels and visible focus; tables can scroll horizontally.

**Estimate:** 5 story points

**Priority:** Should have

## US-06 — Protect credentials

As the student, I want secrets excluded from version control so that publishing the portfolio does not expose accounts.

**Acceptance criteria:** `.env` is ignored; examples contain placeholders only; repository verification reports credential-like values.

**Estimate:** 2 story points

**Priority:** Must have
