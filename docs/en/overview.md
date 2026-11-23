# IOP overview (English)

This is a short English companion to the Persian documentation in `docs/fa/`. Persian is the source of truth. If the two differ, the Persian text wins until the English is corrected.

## Principles

- **Name levels by what is proven.** "Declared" is not "certified".
- **Evidence over promises.** Every control states what evidence shows it is met.
- **Open by default.** Standard, checklists, company documents, versions and reports are public. Raw evidence is not copied and not published.
- **Independent and neutral.** Independent of any government and of any company we verify.
- **Safety of contributors first.** Pseudonymous participation is allowed; maintainers know reviewer identities, reviewers sign with keys.

## Levels

| Level | Controls | Review | Validity |
|---|---|---|---|
| 1 Declared | 17 | Automated scanner, monthly re-scan | 12 months |
| 2 Verified | 45 (L1 + L2) | 2 random reviewers + 1 maintainer, public report | 12 months |
| 3 Continuously Verified | 47 | Paid accredited auditor, quarterly spot checks | Not offered yet |

Seven controls can be checked automatically (TRN-01, TRN-05, THP-01, THP-02, SEC-01, SEC-02, SEC-08).

## Company privacy documents and versions

- The company proves domain ownership (DNS TXT record or `/.well-known/iop.txt`).
- The document is Markdown with YAML front matter, stored in Git.
- Versions follow semver: patch (wording), minor (additive or clarifying), major (change in data, purpose, sharing or retention).
- A major change marks the status "Changed since verified". Without re-verification within 30 days the company drops to Declared.
- Old versions are immutable and public. Attestations name the exact version and its sha256 hash.
- Each company has an Atom feed of changes. The trust page is generated from the structured fields.

## If a company fails

Findings stay private. The company has 60 days to fix them. No public report is published unless the company was granted a level and later loses it. Revocation is always public. We publish only aggregate counts of refusals.

## Conflicts of interest

Reviewers are assigned randomly. Anyone connected to a company in the last 24 months is excluded. Fees (once an entity exists) are pooled, not paid per review. Maintainers' own companies are not eligible for Level 2 or above. A public conflict register is kept in `governance/CONFLICTS.md`.

## Legal position (summary)

Iran has no comprehensive data protection law as of this writing (a bill has been in draft since 2018). The Electronic Commerce Law (2003) has provisions on personal data messages. Local-law mappings in this project are drafts pending review by two lawyers (one Iranian IT/e-commerce, one for foreign sanctions and fiscal hosting). See `docs/fa/12-legal-notes.md`.

## Roadmap (26 weeks, about 5 hours per week)

Standard and checklist draft, validator and templates, public comment, pilots with 3 companies, first Level 2 report, then decide on a legal entity. Security-as-a-service is a separate project to start only after 10 companies reach Level 2.
