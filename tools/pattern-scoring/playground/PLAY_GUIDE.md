# PLAY GUIDE — Illia's terminal loop (python patterns, sandboxed)

**This whole directory is a disposable copy.** The signed library is untouched at
`~/aura-pattern-library`. Break anything here freely.

## The loop, per pattern
```bash
cd ~/ai-lab/pattern-scoring/playground

cat cards/<name>.card.md      # 1. read the card FIRST: valid output, failure signature, attacks
python3 <file>                # 2. baseline run — must match the card's VALID OUTPUT
nano <file>                   # 3. attack: make ONE edit from the card's recipes (line numbers given)
python3 <file>                # 4. re-run, read output against the three-way rule
git checkout -- <file>        # 5. reset the pattern to default (ALWAYS, before next attack)
```

## The three-way rule (your rule, verbatim)
- bad input → **error raised** (traceback / explicit reject) ✅
- bad input → **handled correctly per the stated contract** (card says what the contract is) ✅
- bad input → **no error + silently wrong/confident output** ❌ INVALID — say it, Fable records it

## Safety nets
- `git status` — anything listed = you have unreset edits. `git checkout -- .` resets EVERYTHING.
- `git diff` — shows exactly what you changed, if you forget.
- Ruined beyond repair? The whole playground is rebuildable in one command (ask Fable).

## Verdicts
Tell Fable in chat ("power_analysis: attack 2 silent-wrong ❌") — every verdict lands in
`output/manual_audit_<date>.csv` with evidence. Fable keeps cards coming so you never wait.

## Baseline integrity (added 07-19 after a real incident)
The original untouched library state is tagged `pristine`. At any moment:
```bash
git diff pristine -- python/        # empty output = every pattern is truly original
git checkout pristine -- <file>     # nuclear reset of one file to the ORIGINAL, bypassing HEAD
```
Incident + rule: a Fable `git add -A` once committed an in-progress test edit into HEAD, making
`git checkout` "restore" the poisoned version. Fable now commits ONLY its own paths
(cards/ retrofit_demo/ PLAY_GUIDE.md .gitignore) — never `add -A` — and Illia's reset target
of record is the `pristine` tag, not HEAD.
