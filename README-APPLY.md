# Apply this delta

From the folder that contains both `mac-shared-study-ui-delta/` and `Pankusdesk/`:

```bash
rsync -avhn mac-shared-study-ui-delta/ Pankusdesk/
```

Then:

```bash
rsync -avh mac-shared-study-ui-delta/ Pankusdesk/
```

Verification from inside `Pankusdesk/`:

```bash
python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py
python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py
python3 scripts/tools/verify_college.py
```
