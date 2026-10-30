---
updated: "2026-06-11"
layout: lecture
lang: en
permalink: /en/foundations/git/
title: "Git"
no_comments: true
---

> Part of [Computer Science Fundamentals](../cs/) · [Foundations overview](../)

**Git** is a distributed version control tool. It takes a series of "snapshots" of your project, letting you go back to any past version at any time, see who changed each line of code and when, and collaborate safely with others. It is core infrastructure for [engineering practice](../engineering-practice/) and [reproducibility](../reproducibility/).

## Intuition

Think of Git as a "save-game system" for code:

- Each `commit` is **a save point**: it records the state of every file at this moment, together with a note saying "what I changed".
- Want to try a bold change? Open a `branch` — like saving to a parallel slot. If it goes wrong, throw it away at any time without touching the main line.
- Broke something? `checkout` any earlier save point.
- When several people collaborate, each works on their own branch and the work is combined at the end with `merge` — Git stitches everyone's changes together for you.

Compared with manually copying `project_final_v2_really_final.zip` by date, Git keeps the history **clear, traceable and never lost**.

## Key points

Git has three key areas:

- **Working directory**: the files you are currently editing.
- **Staging area**: use `git add` to pick the changes you want in the next commit.
- **Repository (repo)**: use `git commit` to record them permanently.

The most common command loop:

```bash
git status                 # see which files changed
git add .                  # put the changes in the staging area
git commit -m "Fix out-of-bounds bug in window slicing"   # save and write a note
git log --oneline          # view the history
git push                   # push to a remote (e.g. GitHub)
```

Branches and collaboration:

```bash
git branch feature-kun     # create a branch
git checkout feature-kun   # switch to it (or git switch)
git merge feature-kun      # merge it back into the main branch
git pull                   # fetch other people's latest changes
```

## An example

A typical "trial and error" workflow:

```bash
# The code on the main branch is fine; I want to try a new loss function
git checkout -b try-new-loss      # create and switch to an experiment branch

# ... edit code, run experiments ...
git add train.py
git commit -m "Experiment: switch to Huber loss"

# Didn't work out — abandon the whole branch
git checkout main
git branch -D try-new-loss        # the main branch is untouched

# If it works, merge it in
# git checkout main && git merge try-new-loss
```

`git diff` also shows exactly which lines changed:

```bash
git diff HEAD~1 train.py    # compare with the previous commit
```

## Why it matters for time series forecasting

When doing research like **KUN / Kernel U-Net**, Git directly supports the credibility of your results:

- **Traceable experiments**: every experiment curve corresponds to a commit. Six months later, to reproduce a best result, just `git checkout <that commit>` to get back the exact code from that time.
- **Clear comparisons**: "Does adding downsampling actually help?" Run an A/B test with branches, and `git diff` makes it obvious at a glance.
- **Collaboration without stepping on toes**: people editing different modules don't interfere with each other, and conflicts at merge time can be traced.
- **Support for reproduction**: recording the code version (commit hash) together with the configuration and random seed forms a complete [reproducibility](../reproducibility/) record.

Practical tip: use `.gitignore` to exclude large datasets, model weights, `__pycache__` and the like — **Git manages code, not gigabytes of data.**

## Summary

- Git = version control + collaboration system for code; the core actions are `add` → `commit` → `push`.
- Three areas: working directory / staging area / repository; branches let you experiment safely.
- Write a clear "what changed" for every commit — only then is the history valuable.
- It is the foundation of [engineering practice](../engineering-practice/) and [reproducibility](../reproducibility/) — **without version control, there is no such thing as a trustworthy experiment.**

---

[← Computer Science Fundamentals](../cs/) · [Foundations overview](../)
