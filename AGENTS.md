# PankusDesk — Instructions for Coding Agents

These instructions apply to the whole repository. PankusDesk is a GitHub Pages static educational website with a modern, data-driven `college/` section and legacy study resources. Treat the checked-out repository at the task's starting commit as the source of truth for implementation; never reconstruct its state from earlier chats, ZIP handoffs, or assumptions.

## 1. Operating contract

- Before editing, inspect the relevant files, current Git status, and existing project rules. Explain the intended change and scope when a task is ambiguous or substantial. A request for an opinion, plan, audit, or review is **read-only** unless the user expressly authorizes edits.
- Make the smallest coherent change that satisfies the task. Preserve unrelated files, user changes, dependency manifests, lockfiles, content, links, and identifiers. Never undertake opportunistic refactoring or bulk formatting.
- Work in the task's isolated cloud checkout. Do not create an extra Git worktree unless requested. Use a dedicated feature branch/pull request for proposed repository changes; **never directly push to, merge into, or deploy from `main` without explicit user authorization**. Do not enable auto-merge.
- Do not purchase services, add paid APIs, configure billable infrastructure, introduce secrets, or require a paid model endpoint. The site must remain usable as static GitHub Pages content unless a different architecture is approved.
- Never weaken, bypass, or delete a verifier/test to obtain a green result. Report pre-existing failures separately from regressions caused by the current task.

## 2. Source of authority — read what is relevant

For college content or architecture, consult these existing contracts instead of inventing new conventions:

1. `college/COLLEGE_BUILD_STANDARD.md` — normative college design/build contract.
2. `college/REFERENCE_IMPLEMENTATION.md` — reference implementation (BEE Unit I); copy patterns, not BEE-specific facts/counts.
3. `college/UNIT_BUILD_CHECKLIST.md` — applicable completion/ready checks.
4. `college/NOTEBOOK_REDRAW_STYLE.md` — technical drawing fidelity requirements, only when handling figure assets.
5. The target subject's `subject.json`, schemas, source manifests, coverage audits, relevant JSON and current renderers.

The current repository and explicit instructions for the task take precedence over stale historical examples. If rules appear inconsistent (including publication-state conventions), **report the conflict and ask before normalizing data or changing the contracts**. A passing validator does not establish academic or visual correctness.

## 3. Content fidelity and education-specific rules

- The official current syllabus defines scope; approved prescribed textbooks supply primary theory, with lecture/class material kept in its own provenance layer. Do not invent references, lectures, pages, years, marks, PYQ wording, solutions, source metadata, or syllabus coverage.
- Preserve the separate Text, Textbook Questions, and dated Unit Class Notes layers. The live textbook-led topic authority is typically `kb/data/topics.json`; don't replace it with a summary or merge class-note prose into it.
- Preserve stable IDs, anchors, source references, textbook-question links, semester/calendar links, and existing publication states unless a task specifically requires a verified change.
- Keep original mathematical values, notation, equations, derivations, and scientific meaning. Flag substantive source discrepancies instead of silently correcting them. When producing worked solutions, show reproducible steps and a clear final answer; mark PankusDesk-authored explanations separately from supplied source material.
- Use the shared study UI, renderers, CSS, MathJax conventions, and schema-based data contracts. Extend shared components rather than introducing subject-specific forks. Follow the project's `\dfrac` convention for authored mathematical fractions.
- For PYQ work, distinguish authentic historical questions from generated practice. Predictions are evidence-based *revision priorities*, never claims to know future exam questions. Preserve uncertainty and cite the actual papers/source records used.

## 4. Figure and NRS asset freeze (until explicitly lifted)

**The user is currently producing/redrawing technical figures separately. Do not generate, bulk-generate, trace, reinterpret, repair, replace, optimize, recolor, or overwrite drawings on your own.** Do not call image-generation services or create substitute diagrams to fill gaps. This temporary production restriction does not supersede `NOTEBOOK_REDRAW_STYLE.md` if a later explicit task authorizes drawing work.

- A missing image referenced from a `draft` or `scaffold` unit may be an intentional pending redraw. Record the reference and affected pages; do not assume it is a bug or falsely mark it fixed. For a `ready` unit, report missing or broken figure references as a release-blocking issue.
- When asked to integrate **user-approved** assets, use the supplied binary unchanged, preserve its identity/filename unless authorized, check the intended asset folder and every known consumer (including shared theory/short-note references), and verify browser paths. Do not silently replace an already-approved shared image.
- Image-location checks prove only that the asset loads. Never claim technical/semantic correctness of arrows, polarity, labels, circuit topology, dot/cross symbols, axes, or spatial relationships without a separate verified comparison with the authoritative source.
- Do not add raw textbook scans or private notebook photographs to the public repository by default. Ask about publication rights if the source or permitted use is unclear.

## 5. Development and validation

- GitHub Pages currently publishes static repository files via `.github/workflows/static.yml` on pushes to `main`. No Node, Jekyll/Ruby, database, or package installation is required for ordinary work. Do not replace the deployment approach without approval.
- From repository root, run these baseline checks for relevant college changes (and report the exact results):

  ```sh
  python3 scripts/tools/verify_college.py
  python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py
  python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py
  ```

- Parse modified JSON; syntax-check modified JavaScript/Python; verify affected paths, anchors, and source references. Use a local static server with the **repository root** as document root when HTTP/browser verification is needed: `python3 -m http.server 8000 --bind 127.0.0.1`. Confirm that it serves the correct checkout; do not kill unrelated processes or assume servers persist across cloud tasks.
- For layout, interaction, rendering, or image-placement changes, perform browser/screenshot checks where available and report if they were **not** performed. Check site behavior with the GitHub Pages `/Pankusdesk/` base path where affected. Do not report a page as visually verified solely because HTTP requests returned 200.
- Before changing publication status to `ready`, apply the full source, figure, visual, link, and academic gates in `college/UNIT_BUILD_CHECKLIST.md`. Never promote a unit solely because the automated scripts pass.

### Manual review checklist for every PR and Vercel preview

- Give the user a short **Before you merge — try these checks** checklist in both the PR description and final chat handoff. Normally include 2–4 checks: basic page/navigation sanity plus 1–2 checks specific to the change. This is a user-performed acceptance checklist, not a table of automated PASS/FAIL results.
- Each unchecked item must give a clickable preview page/resource link (or exact navigation steps), the action to perform, and the visible expected result in plain language. Provide the Vercel preview URL and commit it represents. Leave user checkboxes unchecked; agent testing does not complete the user's review.
- For layout/navigation changes, include desktop and phone checks. Include MathJax, images, PDFs or question anchors only where relevant. Refresh links and checks after PR changes/new previews. If preview access is unavailable, explicitly mark the preview pending and supply useful steps without inventing URLs or claiming validation.
- Documentation-only PRs should give 1–2 concrete document review steps with GitHub links and explain that no website behavior changes; do not require unrelated browser checks.
- Report agent-run validators and browser checks briefly in a separate validation note. Run the three existing validators for relevant college changes as required above. Keep known issues/pending checks separate, and do not merge automatically.

## 6. Task completion report and handoff

Provide a concise report containing:

1. **What changed**, why, and the exact files modified.
2. **Validation performed**: commands and PASS/FAIL, affected URLs/paths, and browser checks actually executed.
3. **Open issues**: pre-existing defects, unresolved source ambiguities, pending drawings, and untested behavior, clearly separated from newly introduced problems.
4. **Review instructions**: how the user can inspect the result, with a branch/PR link if one was created.

If instructed to *plan*, *audit*, *explain*, or *review only*, do not change code, assets, project settings, branches, or remote state. Request explicit approval before destructive operations, restructuring shared assets, changing publishing rules, modifying authoritative source content, or merging a pull request.
