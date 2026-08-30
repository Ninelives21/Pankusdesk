# MAC textbook-question quick-link fix

This delta fixes the Unit I Textbook Questions quick links and stacks them vertically.

## What changed

- Quick-link URLs now explicitly target the current question-page path before adding the fragment ID. This avoids `<base href="/">` resolving a bare `#fragment` against the site root.
- Quick links are displayed one per row instead of wrapping horizontally.
- No textbook-question data or solutions are changed.

## Apply

Dry run:

```bash
rsync -avhn mac-question-links-fix-delta/ Pankusdesk/
```

Real sync:

```bash
rsync -avh mac-question-links-fix-delta/ Pankusdesk/
```
