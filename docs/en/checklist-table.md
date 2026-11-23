# Control table

> Generated from `checklist/*.yaml`. Do not edit by hand; change the YAML and run `python scripts/render_checklist.py`.

**47 controls** in 9 domains: Level 1 (17 controls), Level 2 (+28), Level 3 (+2). Level 2 requires every Level 1 and Level 2 control (45).

Check type: **auto** (scanner), **declared** (company attests), **reviewed** (human reviewer).

## Domain 1: Transparency (TRN)

Users can understand, in plain language and without logging in, what data is kept, why, and for how long.

| ID | Level | Check | Control | Evidence | Mappings |
| --- | --- | --- | --- | --- | --- |
| `TRN-01` | 1 | auto | **Public privacy policy page**<br>The privacy policy is reachable without login from the home page and the sign-up page. | url, scan | GDPR Art. 12, Art. 13, Art. 14<br>ISO 27701 7.3 |
| `TRN-02` | 1 | declared | **Plain language, in Persian**<br>The document is written in plain Persian. Where the product serves other languages, a version in that language exists. | document | GDPR Art. 12 |
| `TRN-03` | 1 | declared | **Minimum document content**<br>The document states what data is collected, for what purpose, how long it is kept, who it is shared with, and how users exercise their rights. | document | GDPR Art. 13<br>ISO 27701 7.3 |
| `TRN-04` | 2 | reviewed | **Data inventory**<br>A current inventory of data categories, source, purpose, storage location and third parties exists and is reviewed at least yearly. A summary is public. | document, interview | GDPR Art. 30<br>ISO 27701 7.2 |
| `TRN-05` | 1 | auto | **Version number and change history**<br>The document has a version number, a last-updated date and a link to its change history. The link from the company's privacy page to its IOP-hosted document points to the current version. | url, scan | GDPR Art. 12 |
| `TRN-06` | 2 | reviewed | **Notice of material changes**<br>Material changes to data practice are announced to users at least 14 days before they take effect. | log-sample, document | GDPR Art. 13 |

## Domain 2: Consent and lawful basis (CON)

Every processing purpose has a documented basis, and consent is real and withdrawable.

| ID | Level | Check | Control | Evidence | Mappings |
| --- | --- | --- | --- | --- | --- |
| `CON-01` | 2 | reviewed | **A basis for every purpose**<br>Each processing purpose has a documented basis, for example consent or contract necessity. | document, interview | GDPR Art. 6<br>ISO 27701 7.2 |
| `CON-02` | 1 | declared | **Explicit, unbundled consent**<br>Consent is explicit, not bundled with terms of service, and never pre-ticked. | screenshot, document | GDPR Art. 7, Art. 4(11)<br>ISO 27701 7.2 |
| `CON-03` | 2 | reviewed | **Consent records**<br>Who consented, when, and to which version of the text is recorded. | log-sample, config | GDPR Art. 7(1) |
| `CON-04` | 1 | declared | **Withdrawal as easy as giving**<br>Users can withdraw consent as easily as they gave it. | screenshot, document | GDPR Art. 7(3) |
| `CON-05` | 2 | reviewed | **Sensitive data only with explicit consent**<br>Data revealing ethnic or racial origin, beliefs or religion, moral characteristics, or physical, mental or sexual status is processed only with explicit consent and a stated purpose. | document, interview | GDPR Art. 9<br>local (draft, pending legal review) |

## Domain 3: Minimization and retention (MIN)

Only necessary data is collected and kept only as long as needed. Deletion actually deletes.

| ID | Level | Check | Control | Evidence | Mappings |
| --- | --- | --- | --- | --- | --- |
| `MIN-01` | 1 | declared | **Collect only what is necessary**<br>Data is collected only as far as necessary for the stated purposes and is not reused for other purposes. | document | GDPR Art. 5(1)(b), Art. 5(1)(c)<br>ISO 27701 7.4<br>local (draft, pending legal review) |
| `MIN-02` | 2 | reviewed | **Retention schedule**<br>Each data category has a defined retention period, after which data is deleted or anonymized. | document, config | GDPR Art. 5(1)(e)<br>ISO 27701 7.4 |
| `MIN-03` | 2 | reviewed | **Deletion that actually deletes**<br>Deletion covers databases, file storage and backups (within a defined period). Reviewers sample deletion requests. | log-sample, test-result | GDPR Art. 17<br>ISO 27701 7.4 |
| `MIN-04` | 2 | reviewed | **No real personal data in test environments**<br>Test and development environments do not use real personal data, unless protected by controls equal to production. | interview, config | GDPR Art. 25, Art. 32 |

## Domain 4: User rights (RTS)

Users can access, correct, export and delete their data.

| ID | Level | Check | Control | Evidence | Mappings |
| --- | --- | --- | --- | --- | --- |
| `RTS-01` | 1 | declared | **Access request channel**<br>A public channel for requesting access to personal data exists and is described in the document. | url, document | GDPR Art. 15<br>ISO 27701 7.3<br>local (draft, pending legal review) |
| `RTS-02` | 2 | reviewed | **Process for access, correction, deletion and export**<br>A written process for access, correction, deletion and export with a response deadline (target: 30 days) exists and is followed. | document, log-sample | GDPR Art. 12(3), Art. 15, Art. 16, Art. 17, Art. 20<br>ISO 27701 7.3<br>local (draft, pending legal review) |
| `RTS-03` | 2 | reviewed | **Proportionate identity verification**<br>Requesters are verified as far as necessary, without collecting extra data. | document, interview | GDPR Art. 12(6) |
| `RTS-04` | 1 | declared | **Account deletion**<br>Users can delete their account in the product or by direct request. | screenshot, document | GDPR Art. 17 |
| `RTS-05` | 2 | reviewed | **Request log**<br>User rights requests are logged and anonymized statistics (count, response time) can be shown to reviewers. | log-sample | GDPR Art. 5(2) |

## Domain 5: Third parties (THP)

Users know who sees their data, why, and in which country.

| ID | Level | Check | Control | Evidence | Mappings |
| --- | --- | --- | --- | --- | --- |
| `THP-01` | 1 | auto | **Public subprocessor list**<br>A public list of third parties with access to personal data, with purpose and country for each. | url, document | GDPR Art. 13(1)(e), Art. 28<br>ISO 27701 7.5 |
| `THP-02` | 1 | auto | **Trackers and SDKs disclosed**<br>Third-party trackers and SDKs on the site and app (analytics, ads, maps, payments and so on) are disclosed. The scanner compares known trackers on the site with the document. | scan, document | GDPR Art. 13 |
| `THP-03` | 2 | reviewed | **Agreement with each processor**<br>A written agreement with each processor covers security and limits on use. | contract | GDPR Art. 28(3)<br>ISO 27701 7.5 |
| `THP-04` | 2 | reviewed | **Data location and cross-border transfers**<br>The country where personal data is stored and processed, and any cross-border transfers, are disclosed publicly. | document, config | GDPR Art. 44, Art. 45, Art. 46<br>ISO 27701 7.5 |
| `THP-05` | 2 | reviewed | **Yearly vendor review**<br>Vendors' privacy and security practices are reviewed at least yearly. | document | GDPR Art. 28(1) |

## Domain 6: Technical safeguards (SEC)

Personal data is protected against unauthorized access and disclosure by baseline technical controls.

| ID | Level | Check | Control | Evidence | Mappings |
| --- | --- | --- | --- | --- | --- |
| `SEC-01` | 1 | auto | **HTTPS and HSTS**<br>All pages and APIs are served over HTTPS only, with HSTS enabled. | scan | GDPR Art. 32<br>ASVS V9 |
| `SEC-02` | 1 | auto | **Baseline security headers**<br>Baseline security headers (such as content-type sniffing protection and framing protection) are set. | scan | GDPR Art. 32<br>ASVS V14 |
| `SEC-03` | 2 | reviewed | **Encryption at rest**<br>Stores holding personal data (databases, files, backups) are encrypted, and keys are kept separate from the data. | config, interview | GDPR Art. 32<br>ASVS V6 |
| `SEC-04` | 2 | reviewed | **Staff multi-factor authentication**<br>Staff access to production systems and user data requires multi-factor authentication. | config, screenshot | GDPR Art. 32<br>ASVS V2 |
| `SEC-05` | 2 | reviewed | **Least privilege and access reviews**<br>Access is role-based and limited to need, reviewed at least quarterly. Leavers' access is removed immediately. | log-sample, document | GDPR Art. 32<br>ASVS V4 |
| `SEC-06` | 2 | reviewed | **Access logging for personal data**<br>Access to personal data is logged, logs are protected and reviewed. | log-sample, config | GDPR Art. 32<br>ASVS V7 |
| `SEC-07` | 2 | reviewed | **Secure password storage**<br>User passwords are stored using a suitable password hashing algorithm (such as argon2id, bcrypt or scrypt) with salts, never in plain text or fast hashes. | config, interview | GDPR Art. 32<br>ASVS V2 |
| `SEC-08` | 1 | auto | **Vulnerability disclosure channel**<br>A security.txt file or equivalent page with a contact for vulnerability reports exists. | scan, url | GDPR Art. 32 |
| `SEC-09` | 2 | reviewed | **Encrypted, restore-tested backups**<br>Backups are encrypted and restores are tested at least yearly. | test-result, document | GDPR Art. 32 |
| `SEC-10` | 3 | reviewed | **Yearly independent penetration test**<br>An independent penetration test is performed yearly and a summary of results and remediation is given to the auditor. | test-result | GDPR Art. 32 |

## Domain 7: Incidents (INC)

If something goes wrong, the company is prepared and tells users honestly.

| ID | Level | Check | Control | Evidence | Mappings |
| --- | --- | --- | --- | --- | --- |
| `INC-01` | 1 | declared | **Incident reporting contact**<br>A contact for reporting privacy or security incidents is published. | url, document | GDPR Art. 33 |
| `INC-02` | 2 | reviewed | **Written incident response plan**<br>A written plan with roles and steps exists and is exercised at least yearly. | document, interview | GDPR Art. 33 |
| `INC-03` | 2 | reviewed | **Notifying affected users**<br>Users affected by a breach are notified within 72 hours of confirmation, with what data, what risk and what action is needed. | document, log-sample | GDPR Art. 34 |
| `INC-04` | 2 | reviewed | **Post-incident review**<br>A review follows every serious incident and a summary is published. | document | GDPR Art. 33(5) |

## Domain 8: Governance (GOV)

Someone in the company owns privacy, and decisions about data are made deliberately.

| ID | Level | Check | Control | Evidence | Mappings |
| --- | --- | --- | --- | --- | --- |
| `GOV-01` | 2 | reviewed | **Named privacy owner**<br>A specific person is responsible for privacy and their name or role is in the document. | document, interview | GDPR Art. 37, Art. 38, Art. 39<br>ISO 27701 7.2 |
| `GOV-02` | 2 | reviewed | **Staff training**<br>Staff are trained on privacy and security at onboarding and yearly. | document, log-sample | GDPR Art. 39(1)(b), Art. 32(4) |
| `GOV-03` | 2 | reviewed | **Privacy review before new features**<br>A privacy review is done and recorded before launching a feature that changes how data is used. | document, interview | GDPR Art. 25, Art. 35<br>ISO 27701 7.4 |
| `GOV-04` | 1 | declared | **Disclosure of data sale or ad sharing**<br>The document states clearly whether personal data is sold or shared for advertising. A "no" must also be explicit. | document | GDPR Art. 13(1)(e) |
| `GOV-05` | 3 | reviewed | **Scheduled control reviews**<br>The company reviews its own controls on a schedule (at least quarterly) and records results for the auditor. | document, log-sample | GDPR Art. 24 |

## Domain 9: Local context (LOC)

What cannot be copied from foreign standards: data location, requests from third parties and authorities, and local obligations. This domain has not yet had legal review.

> **Status: draft, not yet reviewed by a lawyer.**

| ID | Level | Check | Control | Evidence | Mappings |
| --- | --- | --- | --- | --- | --- |
| `LOC-01` | 1 | declared | **Data location disclosed**<br>The document states in which country and with which hosting provider personal data is stored. | document | GDPR Art. 13(1)(f)<br>local (draft, pending legal review) |
| `LOC-02` | 2 | reviewed | **Policy for third-party and authority data requests**<br>A written, published policy explains how requests for user data from third parties and authorities are handled: who decides, what documentation is required, and whether the user is informed where permitted. | document, interview | local (draft, pending legal review) |
| `LOC-03` | 2 | reviewed | **Disclosure of local obligations that limit privacy**<br>If a legal or regulatory obligation requires the company to retain or disclose data, this is stated in plain language to users. | document | local (draft, pending legal review) |
