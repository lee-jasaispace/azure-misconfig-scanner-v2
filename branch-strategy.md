# Git Branching Strategy for Misconfiguration Scanner

## Main Branches:
- **main**: Always contains the latest stable and documented version of the project.
- **dev**: Used for integrating daily task work. Regularly merged into `main` after validation.

## Feature/Task Branches:
- `feature/dayX-task`: e.g., `feature/day8-storage-policy`
- `bugfix/fix-dayX-policy-error`

## Workflow:
1. Create a feature branch from `dev`
2. Commit daily progress
3. Open a PR to `dev`
4. After review and validation, merge to `main`
