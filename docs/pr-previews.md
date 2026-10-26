# Pull-request website previews

GitHub Pages remains the production host at
https://ninelives21.github.io/Pankusdesk/.
Vercel is used separately for branch/PR review websites.

## Activation status

Repository configuration alone does not activate previews. The repository owner
must connect a Vercel project to `Ninelives21/Pankusdesk` through Vercel's GitHub
integration. Until that connection exists and a deployment succeeds, there is no
verified remote preview URL.

## One-time setup

1. Review and merge the preview-configuration PR. The existing GitHub Pages
   workflow is unchanged by this configuration.
2. In Vercel, import the existing `Ninelives21/Pankusdesk` GitHub repository into
   a project named `pankusdesk-previews`. Reuse that project if it already exists.
   Authorize the Vercel GitHub app for this repository. A ChatGPT Vercel connection
   and the Vercel GitHub app are separate connections; both may require owner
   authorization when setting up through ChatGPT.
3. Use these settings:

   | Setting | Value |
   | --- | --- |
   | Framework preset | Other |
   | Root directory | Repository root (`./`) |
   | Install command | Empty; overridden by `vercel.json` |
   | Build command | Empty; overridden by `vercel.json` |
   | Output directory | `.` |
   | Production branch | `main` |
   | Custom domain | None |
   | Environment variables/secrets | None needed for this static site |

   Do not add a paid plan, paid integration, or custom domain for this setup.
   Check the account's available plan and limits before the first deployment;
   deployment success and plan eligibility are not established by this file.
4. Keep Vercel's fork-deployment authorization protection enabled. Keep preview
   access protection enabled where available; reviewers may need to sign in.
   `noindex` discourages search indexing but is not access control.
5. Trigger a Preview deployment of the desired feature branch. Existing PRs may
   need a new push or a manual Preview deployment after the Git connection is
   established. For PR #4, use `feat/subject-study-exam-resources`.
6. Confirm Vercel posts a successful deployment/check and preview link on the PR.
   Open the actual deployment and complete the checks below before calling the
   setup active.

The repository currently contains roughly 612 MiB of tracked files. Use Git
integration rather than assuming a CLI source upload will fit the free-plan
upload limit. Do not remove learning assets to force a deployment through; if
hosting rejects the repository, record the actual limit/failure and reassess.

## Normal review workflow

- Push changes to a feature branch and open its PR.
- The connected Vercel GitHub integration creates the preview and posts its URL.
- Later pushes update the branch preview. Confirm the preview corresponds to the
  current PR head SHA, rather than a previous successful deployment.
- Review the rendered site using the link labelled Preview in the PR. Use the
  PR's latest deployment link; do not manufacture a URL from the branch name.
- Merge the PR after review. The existing Pages workflow publishes `main` to the
  live GitHub Pages URL.

`vercel.json` disables automatic Vercel Git deployments from `main`. Other
branches inherit Vercel's default automatic deployment behaviour. This is branch
deployment automation: a branch can receive a preview before it has an open PR.
It does not prevent someone from deliberately starting a manual deployment.
Do not assign the live site's domain to this preview project.

The GitHub integration manages deployment checks/comments. No additional Actions
workflow, deployment token, or per-PR setup is needed once connected. An initial
project import can create a Vercel deployment; its address is separate from the
GitHub Pages live site.

## Acceptance checks

On the real preview URL:

1. Open `/`, the Semester 1.1 dashboard, and all three subject landing pages.
2. Open a unit and confirm JSON content, CSS, JavaScript, and figures load.
3. For PR #4, open each End-Sem Revision Notes collection and return to its
   subject resources. Also open BEE's SE 1 questions and PYQs.
4. Verify desktop and mobile layouts and check for failed local asset requests.
5. Confirm preview responses include `X-Robots-Tag: noindex, nofollow` and that
   GitHub's deployment/check identifies the expected commit.
6. Make a subsequent branch update and verify its preview refreshes without
   creating/reconnecting another project.

The college pages already use `/` on non-GitHub hosts and `/Pankusdesk/` on
GitHub Pages. Keep `.html` routes: `cleanUrls` is explicitly false. A preview at
the origin root does not replace checks for the production `/Pankusdesk/` base
path. Local browser checks simulate routing; they do not certify a real Vercel
deployment or account-side settings.

## Maintenance and separation

- Keep `.github/workflows/static.yml` as the GitHub Pages production workflow.
- Keep the preview configuration on `main` so new feature branches inherit it.
  Older open branches need the configuration merged into them or equivalent
  project settings before relying on the configured behaviour.
- Use the Vercel project settings to inspect retention and remove obsolete
  preview deployments. Closing a PR is not a promise of immediate deletion.
- To stop future automatic previews, disconnect the Vercel Git integration or
  disable its Git deployments. Removing a project connection does not itself
  delete existing preview URLs.

## Provider documentation

- [GitHub integration and automatic PR links](https://vercel.com/docs/git/vercel-for-github)
- [Git branch deployment controls](https://vercel.com/docs/project-configuration/git-configuration)
- [Static-site build settings](https://vercel.com/docs/builds/configure-a-build)
- [Current platform limits](https://vercel.com/docs/limits)
