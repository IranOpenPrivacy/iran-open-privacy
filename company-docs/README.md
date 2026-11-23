<div dir="rtl">

# پوشهٔ سند شرکت‌ها

هر شرکت شرکت‌کننده یک پوشه دارد: `company-docs/<شناسه-شرکت>/`

| فایل | کاربرد |
| --- | --- |
| `meta.yaml` | دامنه، اثبات مالکیت، تماس، سطح فعلی و فهرست نسخه‌ها |
| `privacy.fa.md` | سند فارسی با فرونت‌مَتر ساختاریافته |
| `privacy.en.md` | سند انگلیسی (اختیاری) |

- قالب خام: [templates/privacy-document.fa.md](../templates/privacy-document.fa.md)
- قواعد نسخه‌گذاری: [docs/fa/09-privacy-documents.md](../docs/fa/09-privacy-documents.md)
- `example-company` **ساختگی** است و فقط برای نمایش قالب.
- `scripts/validate.py` ساختار و سازگاری نسخه‌ها را می‌سنجد.

برای افزودن شرکت: یک Pull Request با پوشهٔ جدید یا [فرم درخواست شرکت](../../../issues/new?template=company-application.yml).

</div>
