<div dir="rtl">

# پوشهٔ سند شرکت‌ها

هر شرکتی که به برنامه بپیوندد یک پوشه دارد: `company-docs/<شناسه-شرکت>/`

| فایل | کاربرد |
| --- | --- |
| `meta.yaml` | دامنه، اثبات مالکیت، تماس، سطح فعلی و فهرست نسخه‌ها |
| `privacy.fa.md` | سند فارسی با سربرگ ساختاریافته (front matter) |
| `privacy.en.md` | سند انگلیسی (اختیاری) |

- قالب خام: [templates/privacy-document.fa.md](../templates/privacy-document.fa.md)
- قواعد نسخه‌گذاری: [docs/fa/09-privacy-documents.md](../docs/fa/09-privacy-documents.md)
- `example-company` **ساختگی** است و فقط برای نشان دادن قالب ساخته شده.
- `scripts/validate.py` ساختار سند و جور بودن شماره‌های نسخه را بررسی می‌کند.

برای افزودن شرکت، یک Pull Request با پوشهٔ تازه بفرستید یا [فرم درخواست شرکت](../../../issues/new?template=company-application.yml).

</div>
