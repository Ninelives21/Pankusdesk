# MAC Unit I — textbook-faithful rebuild

This delta replaces the previous summary-style Unit I topic content with the prescribed Grewal wording/sequence, filtered to the R25 Unit I syllabus.

- All retained worked textbook examples are collapsible dropdowns.
- Chapter-end textbook practice is intentionally not surfaced in this delta; that selection will be reviewed separately.
- No raw commercial textbook scans are copied into the public workspace.

## Apply

Dry run:

```bash
rsync -avhn mac-unit1-textbook-delta/ Pankusdesk/
```

Real sync:

```bash
rsync -avh mac-unit1-textbook-delta/ Pankusdesk/
```

## Verify

```bash
python3 Pankusdesk/college/1-1/matrices-calculus/kb/tools/verify_kb.py
```
