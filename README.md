# argo-delivery
Single commit, single repo environment promotion following the continuous delivery philosophy.

## Aim
The aim of this repo is to try and model an application delivery model on continuous delivery principles. This means the following:
- One commit promoted from dev into production
- Ability to easily rollback on failure

In addition, I wanted to test out how to do the following:
- Automated smoke tests and promotion
- Manual gate to prove that it's possible