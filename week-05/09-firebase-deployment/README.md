# Firebase Hosting Deployment

**Source:** Trainer Notes, Week 5 Firebase deployment exercise.

## Local preparation

1. Build a selected Vite app with `npm run build`.
2. Copy this `firebase.json` to that app root or run Firebase with this directory as the configuration source.
3. Copy `.firebaserc.example` to `.firebaserc` and replace the placeholder project ID.
4. Run `npx firebase-tools login`, `npx firebase-tools use <project-id>`, then `npx firebase-tools deploy --only hosting`.

**Status:** External verification required. No login, project creation, deployment or live URL has been fabricated. These actions require the user's authenticated Firebase account and approval.
