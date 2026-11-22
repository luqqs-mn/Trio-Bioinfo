# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: <ASSIGNMENT 1>
- Student name: <AINURRULNAJWA BINTI SAHALAN>
- Matric no: <A24CS0223>
- Group ID: <G01>
- AI level: <1>
- Tools cited: <Google. (2026). Gemini (Versi 22 November) [Model bahasa besar]. https://gemini.google.com>

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/ ] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: <22/11/2026>
- Tool: <Gemini>
- Purpose: <explain,hint, check code>
- Prompt: <Berdasarkan assignment 1 yang saya bekalkan saya, dapat bahagian def decision_counts . saya masukkan decision:ZERO_COUNT tapi dia kata tak declare>
- Output: <Ralat "not declared" atau NameError: name 'ZERO_COUNT' is not defined (atau DECISIONS) berlaku kerana pemalar (constant) ZERO_COUNT tersebut belum ditakrifkan di bahagian atas fail src/a1_triage.py.

Dalam Python, pemalar seperti ZERO_COUNT bukanlah kata kunci terbina dalam (built-in); ia mesti diisytiharkan terlebih dahulu di bahagian atas fail sebelum boleh digunakan di dalam fungsi.

Cara Membetulkannya
Tambahkan takrifan pemalar di bahagian atas fail src/a1_triage.py (tepat di bawah bahagian import dan sebelum mana-mana def):

Python
ZERO_COUNT = 0
DECISIONS = ("prioritize", "review", "exclude")
(Jika anda turut menggunakan IMPACT_ORDER dan MEAN_DECIMALS dalam fungsi lain, pastikan kedua-duanya juga ditakrifkan di bahagian atas itu:)

Python
IMPACT_ORDER = ("high", "moderate", "low", "modifier")
MEAN_DECIMALS = 1
Simpan fail (Ctrl + S) dan uji semula menggunakan ruff dan pytest di terminal:

PowerShell
ruff check src
python -m pytest
(Nota: Menggunakan pemalar ZERO_COUNT = 0 di bahagian atas fail seperti ini adalah cara yang tepat kerana ia mengelakkan amaran "magic number" daripada ruff sambil memastikan Python mengenali nama ZERO_COUNT tersebut.)>

- Verified by: <ran pytest>
- My change: <Accepted the definition of ZERO_COUNT = 0 and DECISIONS at the top of the file to resolve the NameError and avoid ruff magic-number warnings, while ignoring IMPACT_ORDER and MEAN_DECIMALS since my task only covers decision_counts.>
- Used in: <assignment1_G01/src/a1_triage.py (decision_counts function and module-level constants)>

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->

## Entry 2

- Date: <22/11/2026>
- Tool: <gemini>
- Purpose: <explain,hint, check code>
- Prompt: <Tolong checkkan code saya>
- Output: <Logik pengiraan di bahagian atas fungsi gene_summary dalam gambar tersebut sudah tepat, tetapi kamus summary[gene] belum lengkap kerana tiga kunci terakhir masih tertinggal.   Garis putus-putus di bawah pemboleh ubah rev, excl, dan mean_depth muncul kerana ketiga-tiga pemboleh ubah tersebut sudah dikira tetapi belum dimasukkan ke dalam kamus summary[gene].   Cara MelengkapkannyaTambahkan tiga baris kunci yang hilang di dalam kurungan { ... } pada summary[gene] seperti berikut:   Python        summary[gene] = {
            "total": total,
            "prioritize": prio,
            "review": rev,
            "exclude": excl,
            "mean_depth": mean_depth,
        }
Semakan TambahanPastikan pemalar MEAN_DECIMALS = 1 telah ditakrifkan di bahagian atas fail src/a1_triage.py supaya round(..., MEAN_DECIMALS) tidak menghasilkan ralat NameError.   Tekan Ctrl + S untuk menyimpan fail, kemudian jalankan ruff check src dan python -m pytest di terminal bagi memastikan tiada amaran atau kegagalan ujian.>

- Verified by: <ran pytest>
- My change: <Accepted the definition of ZERO_COUNT = 0 and DECISIONS at the top of the file to resolve the NameError and avoid ruff magic-number warnings, while ignoring IMPACT_ORDER and MEAN_DECIMALS since my task only covers decision_counts.>
- Used in: <assignment1_G01/src/a1_triage.py (decision_counts function and module-level constants)>

