# Iran Open Privacy (IOP)

An open, community-run privacy standard and verification program for Iranian digital products.

**Status: draft 0.1.** The standard, checklist and process are open for public comment. No company has been verified yet. The primary language of this project is Persian; this page is a short English summary. See [README.md](README.md) for the full Persian version.

## The problem

Iranian users have no reliable way to tell which products respect their data. Privacy policies are long, unversioned and unverifiable. Badges without evidence are theater.

## The idea

1. A **public standard**: 47 checkable controls in 9 domains, mapped to GDPR, ISO 27701 and OWASP ASVS, with local-law mappings marked as drafts pending legal review.
2. **Company privacy documents** hosted in this repository: Markdown with structured front matter, semantic versions, immutable history, and an Atom change feed.
3. **Three levels, named by what is actually proven** (never "certified" unless a paid, accredited auditor is involved):

| Level | Name | What it means | How |
|---|---|---|---|
| 1 | Declared (اظهارشده) | The company published a document and passes automated checks | Scanner, monthly re-scan, expires in 12 months |
| 2 | Verified (تأییدشده) | Evidence was reviewed by independent people | 2 random community reviewers plus 1 maintainer sign-off, annual, public report |
| 3 | Continuously Verified (تأیید مستمر) | Ongoing, paid, accredited audit | Not offered until a legal entity and an auditor exist |

4. **Everything is open**: code (AGPL-3.0), standard and checklists (CC BY-SA 4.0), reports (CC BY 4.0).

## What we are not

Not a government body, not a regulator, not a law firm, not a security audit. A Level 1 or 2 result is not legal advice and not a guarantee.

## Repository map

- `docs/fa/`: the full documentation (Persian)
- `docs/en/`: overview and checklist table (English)
- `checklist/`: the 47 controls as YAML
- `schemas/`: JSON Schemas
- `templates/`: privacy document templates
- `company-docs/`: company documents (one example, fictional)
- `scripts/`: validator, table renderer, link checker
- `governance/`: maintainers and conflict-of-interest register
- `announcement/`: public announcement texts

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). You may contribute under a pseudonym. Useful right now:

- Review the checklist and propose changes
- Apply to be a reviewer (pseudonymous is fine)
- Apply as a pilot company (Iranian startup or SaaS)
- Help with legal review of the local-law mappings

## Validate locally

```
pip install pyyaml jsonschema
python scripts/validate.py
python scripts/render_checklist.py --check
python scripts/check_links.py
```

## Contact

contact@iranopenprivacy.org. Security issues about this project: see [SECURITY.md](SECURITY.md).
