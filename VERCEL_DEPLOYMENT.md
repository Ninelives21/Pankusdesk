# College-only Vercel deployment

This configuration is for `pankusdesk-previews`. GitHub Pages continues to publish
repository files through the unchanged `.github/workflows/static.yml`. The original
homepage, college content, legacy bookmark redirects and five retained legacy PDFs
are not edited, deleted or relocated by this build.

## Build and output boundary

Run `python3 scripts/tools/build_vercel.py` from the repository root. The build uses
only Python's standard library; no dependency installation is required.
`vercel.json` selects `_vercel_site` as the sole deployment output and keeps explicit
`.html` URLs (`cleanUrls: false`). Repeated builds replace only that generated folder.

The output contains `index.html`, `navbar_new.html`, every college HTML/JSON file,
all modern shared JS/CSS, and their transitive local browsing dependencies. Existing
site-root, file-relative and subject-relative paths are retained. Linked college
PDFs, images, fonts and Markdown notes are copied without alteration. All output
files, including the homepage, are byte-identical to source. The external link to
https://ninelives21.github.io/Pankusdesk-legacy/ remains on the Vercel homepage.
MathJax uses its existing free jsDelivr URL unchanged.

The build does not crawl that external site or copy the legacy redirect pages and
legacy PDFs retained for GitHub Pages bookmarks. No development tools, unreferenced
notes/audits, backups, source archives, editor settings or Git metadata are deployed.
JSON provenance records remain intact even when they name offline archives. A
source filename in provenance is not itself a download dependency.

An existing local dependency outside `college/`, `scripts/new/`, `styles/new/` or the
two root entry files fails the build for review, rather than silently pulling legacy
content into Vercel. The generated output has a 350 MiB size ceiling. This is a
regression budget, not a guarantee about accumulated Hobby deployment storage.
No drawings or assets are recompressed, regenerated or redrawn.

## Exact current size comparison

Baseline main: `5629b45e1e8c7d3b370275494a974efc9cb0ee93`, after PR #15 merged.
Sizes are sums of regular file byte lengths, without filesystem block allocation,
Git history, compression, build cache or historical Vercel deployments.

| Scope | Files | Bytes |
| --- | ---: | ---: |
| Latest main before this build configuration | 2,167 | 310,702,492 |
| Latest main after the five existing `.vercelignore` tree exclusions | 1,098 | 282,149,366 |
| Generated college-only output | 927 | 270,693,749 |

The output saves 40,008,743 bytes against the full current main source inventory,
or 11,455,617 bytes against the already-excluded Vercel-eligible source inventory.
These are local inventories, not a measurement of actual historical Vercel usage.

Each build prints the source input, input after the five legacy tree exclusions,
and generated output file counts and bytes. Its source counts include this PR's
new configuration/documents after they are committed, so those counts differ from
the before-configuration baseline above. A real checkout inventories tracked files;
a source archive falls back to a filesystem inventory excluding generated/scratch
folders. Archive validation never accidentally inventories a parent Git checkout.

## Vercel dashboard settings

In **pankusdesk-previews → Settings → Build and Deployment**, verify:

- Root Directory: repository root (blank / `.`).
- Framework Preset: **Other**.
- Build Command: `python3 scripts/tools/build_vercel.py`.
- Output Directory: `_vercel_site`.
- Install Command: empty/disabled; no package installation is needed.

The committed `vercel.json` declares the build/output configuration. Remove any
conflicting framework or command overrides if the project still uses them. Keep
the current Git connection and branch selection. GitHub Pages needs no settings or
workflow change. This PR does not alter dashboard settings or merge/deploy main.
Existing Git integration may create a preview deployment of the PR automatically.

After reviewing and merging this PR, deploy the updated main (or inspect the
Git-triggered production deployment). Verify the logs show this build command and
output directory. Redeploying an old deployment/source configuration will not apply
these changes.

## Existing storage must be cleaned up separately

A new, smaller deployment does not release storage belonging to previous ones.
Unlimited retained deployments can still exceed the Hobby allowance. Review
obsolete previews in Vercel and delete those no longer needed, keeping production
and required rollback deployments. Configure suitable retention if available on
Hobby; otherwise perform reviewed manual cleanup. If storage blocks new builds,
cleanup may be needed before deploying this configuration. Confirm usage in the
Vercel dashboard afterward. No paid plan, API or extra hosting is required.

No historical deployment was deleted and no claim is made that the account's
accumulated storage is now below 10 GB. Account usage, retention availability and
existing project overrides cannot be inspected through the available GitHub tools.

## Validation

Run the three existing validators from source root:

```sh
python3 scripts/tools/verify_college.py
python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py
python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py
```

All three passed on the updated source. Python syntax compilation, Vercel JSON
parsing, all college HTML/JSON presence, output/source byte identity, legacy-tree
exclusion and original GitHub Pages workflow/homepage integrity were checked.
Repeated builds must produce the same file paths and bytes, remove stale generated
files, and leave source files unchanged.

Chromium compared the latest source with `_vercel_site` at local static document
roots: all 46 current entry/college HTML pages at 390px mobile width and eight
representative routes at 1440px desktop width (108 page checks / 54 before-after
scenarios). Titles, headings, links, images, MathJax counts, mobile menus, overflow
and failure signatures matched in every scenario. BEE End-Sem Notes retained all
67 MathJax containers, with no failed local resources or missing rendered links.
The six college PDFs returned valid HTTP 200 PDF responses from both snapshots.
A static audit checked 673 local HTML references and found only the three known
Progress references listed below. Desktop/mobile screenshots were inspected.

Existing source issues are preserved and reported separately: Progress's missing
stylesheet and two course links, missing draft BEE short-note figures with fallback
handling, and mobile horizontal overflow in several long unit pages. A green build
or validator does not assert those unrelated source issues are fixed.
