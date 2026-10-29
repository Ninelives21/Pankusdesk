# College-only Vercel deployment

This configuration is for `pankusdesk-previews`. GitHub Pages continues to publish
repository files using the unchanged `.github/workflows/static.yml`. No original
page, data, image, academic resource, or renderer is modified or moved.

## Build

Run `python3 scripts/tools/build_vercel.py` from the repository root. Python's
standard library is the only dependency. `vercel.json` selects `_vercel_site` as
the sole deployment output, disables framework detection/install, and retains
explicit `.html` URLs. The build replaces only that generated directory.

The build includes every college HTML/JSON file, shared modern JS/CSS, and the
transitive local resources referenced by those files. It resolves site-root,
file-relative and subject-relative paths, copies linked PDFs and images without
alteration, and keeps the original directory layout. JSON metadata is preserved,
even when it describes offline source archives. An archive name in provenance
metadata does not make the archive a browsing dependency. Referenced Markdown
resources are retained; unreferenced notes, Python tools, backups, archives,
legacy pages and development files are excluded. The build rejects a college
dependency in the five excluded legacy trees and enforces a 350 MiB ceiling.
The generated homepage alone omits the legacy-site section/link.

MathJax continues to use the existing free jsDelivr URL, unchanged. No new hosting,
service, package, paid API or runtime function is introduced.

## Exact inventory at starting commit

Starting commit: `5cb7456a07382f00d18f93f7c850eedd254b438f`.
Sizes are sums of regular file lengths in bytes, without filesystem allocation,
compression, Git history or build cache. These are reproducible local inventories,
not measurements of Vercel's accumulated historical deployment storage.

| Scope | Files | Bytes |
| --- | ---: | ---: |
| Full tracked repository | 3,533 | 644,412,076 |
| Previous root content after the existing five `.vercelignore` tree exclusions | 1,105 | 282,281,076 |
| Generated college-only output | 927 | 270,693,436 |

The output reduces the previous Vercel-eligible source inventory by 11,587,640
bytes (4.105%); compared with the full repository, it saves 373,718,640 bytes
(57.994%). The existing `.vercelignore` already removed most legacy bytes. College
images/PDFs account for most remaining storage; none were recompressed or redrawn.
The build prints current source/output counts on every run. Source counts use
committed HEAD and will include these new build/configuration documents after
commit; the output counts are unaffected.

## Vercel dashboard configuration

In **pankusdesk-previews → Settings → Build and Deployment**:

- Root Directory: repository root (leave blank / `.`).
- Framework Preset: **Other**.
- Build Command: `python3 scripts/tools/build_vercel.py`.
- Output Directory: `_vercel_site`.
- Install Command: empty/disabled; no dependency installation is needed.
- Remove conflicting dashboard overrides. The committed `vercel.json` provides
  these settings for this project. Keep the existing Git connection and branch
  selection; do not change GitHub Pages or its workflow.

After review/merge, create a new deployment from this configuration and inspect
its build output before promoting it. No dashboard changes, production deployment,
merge, or historical deployment deletion were performed as part of this PR.

**Accumulated storage needs separate cleanup.** A smaller output does not release
storage held by previous deployments and cannot guarantee staying below 10 GB
with unlimited retained deployments. In the project's deployment retention/cleanup
settings, choose the shortest suitable retention offered on Hobby. Review and
manually delete obsolete preview deployments if automatic retention is unavailable
or insufficient; retain production and any needed rollback. Avoid unnecessary
redeployments. Confirm the resulting storage usage in Vercel before resuming
frequent previews. No paid plan is required by this build. Actual storage/quota
availability and existing dashboard overrides could not be inspected without a
Vercel connection.

## Validation

All three existing validators passed:

```sh
python3 scripts/tools/verify_college.py
python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py
python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py
```

Python syntax compilation and `git diff --check` passed. Every college HTML/JSON
file is present in output. Every output file except the intentionally transformed
homepage is byte-identical to its source.

Chromium checks used 1440×1000 desktop and 390×844 mobile viewports against the
built output. Checked Home, Semester 1.1, Calendar, Progress, BEE index, BEE Unit I,
BEE Unit I Short Notes, BEE End-Sem Notes, MAC Unit I and Chemistry Unit II;
loaded all images (including lazy images), expanded details, tested mobile menu,
requested same-origin rendered links and checked MathJax rendering. BEE End-Sem
Notes has 67 rendered math containers at both sizes, no broken images/resources,
and no horizontal page overflow. Desktop/mobile screenshots were inspected.
The six linked PDFs are retained unchanged. The static HTML audit checked 673
local references across the entire output.

Pre-existing issues preserved for separate review: Progress references a missing
`styles/new/pages/progress.css`, and links to missing Programming/Problem Solving
and Engineering Drawing course pages. The BEE Unit I, MAC Unit I and Chemistry
Unit II pages have horizontal overflow at 390px. No source content or layout was
changed to address these unrelated issues.
