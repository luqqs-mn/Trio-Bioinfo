# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: ASSIGNMENT 1
- Student name: AINURRULNAJWA BINTI SAHALAN, MUHAMMAD LUQMAN BIN MOHD AZMI, ABDUL RASYID BIN ABD GHANI
- Matric no: A24CS0223, A24CS0138, A24CS0030
- Group ID: G01
- AI level: 1
- Tools cited: Google. (2026). Gemini (Versi 22 November) [Model bahasa besar]. https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 22/11/2026
- Tool: Gemini
- Purpose: explain,hint, check code
- Prompt: Berdasarkan assignment 1 yang saya bekalkan saya, dapat bahagian def decision_counts . saya masukkan decision:ZERO_COUNT tapi dia kata tak declare
- Output: Ralat "not declared" atau NameError: name 'ZERO_COUNT' is not defined (atau DECISIONS) berlaku kerana pemalar (constant) ZERO_COUNT tersebut belum ditakrifkan di bahagian atas fail src/a1_triage.py.

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

- Verified by: ran pytest
- My change: Accepted the definition of ZERO_COUNT = 0 and DECISIONS at the top of the file to resolve the NameError and avoid ruff magic-number warnings, while ignoring IMPACT_ORDER and MEAN_DECIMALS since my task only covers decision_counts.
- Used in: assignment1_G01/src/a1_triage.py (decision_counts function and module-level constants)

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->

## Entry 2

- Date: 22/11/2026
- Tool: gemini
- Purpose: explain,hint, check code
- Prompt: Tolong checkkan code saya
- Output: Logik pengiraan di bahagian atas fungsi gene_summary dalam gambar tersebut sudah tepat, tetapi kamus summary[gene] belum lengkap kerana tiga kunci terakhir masih tertinggal.   Garis putus-putus di bawah pemboleh ubah rev, excl, dan mean_depth muncul kerana ketiga-tiga pemboleh ubah tersebut sudah dikira tetapi belum dimasukkan ke dalam kamus summary[gene].   Cara MelengkapkannyaTambahkan tiga baris kunci yang hilang di dalam kurungan { ... } pada summary[gene] seperti berikut:   Python        summary[gene] = {
            "total": total,
            "prioritize": prio,
            "review": rev,
            "exclude": excl,
            "mean_depth": mean_depth,
        }
Semakan TambahanPastikan pemalar MEAN_DECIMALS = 1 telah ditakrifkan di bahagian atas fail src/a1_triage.py supaya round(..., MEAN_DECIMALS) tidak menghasilkan ralat NameError.   Tekan Ctrl + S untuk menyimpan fail, kemudian jalankan ruff check src dan python -m pytest di terminal bagi memastikan tiada amaran atau kegagalan ujian.

- Verified by: ran pytest
- My change: Accepted the definition of ZERO_COUNT = 0 and DECISIONS at the top of the file to resolve the NameError and avoid ruff magic-number warnings, while ignoring IMPACT_ORDER and MEAN_DECIMALS since my task only covers decision_counts.
- Used in: assignment1_G01/src/a1_triage.py (decision_counts function and module-level constants)


## Entry 3 

- Date: 22/11/2026
- Tool: Gemini
- Purpose: explain, hint, check code
- Prompt: i am initiating this group assignment for variant triage. can you explain the overall of this assignment and suggest task division for 3 members? we are all newbies in python.
- Output: The AI broke down the assignment into plain terms, explaining the six rules, the required functions, and the documentation. It provided a fair task division for 3 people, assigning one member to core logic, one to summaries/ranking, and one to outputs/integration. It also explained how to set up the GitHub repository and how to resolve fatal git errors like "Could not resolve host: github.com" and "The term 'git' is not recognized".
- Verified by: successfully set up the shared GitHub repository, invited groupmates, and pushed the initial files.
- My change: used the task division to write the GROUP_CONTRACT.md. also shared the simplified explanation with my groupmates so everyone understood the goal before we started coding.
- Used in: GROUP_CONTRACT.md and project setup.

## Entry 4

- Date: 22/11/2026
- Tool: Gemini
- Purpose: check code, fix errors
- Prompt: here is my design.md and a1_triage.py. i tried to run python -m pytest but it failed on test_csv_text_starts_with_the_header. it says assert 'variant, gen...' == 'variant,gene...'. help me fix this.
- Output: The error is caused by the spacing in the results_to_csv function. using `", ".join(...)` adds a space after the comma, but standard CSV format requires no spaces, so it should be `",".join(...)`. The AI also provided the exact code for results_to_csv and build_report, and gave the mermaid code for the flowchart in design.md.
- Verified by: ran pytest and all 6 visible tests passed. ran ruff check src and all checks passed.
- My change: removed the spaces in the results_to_csv join function, implemented the CSV and report generation functions, and added the mermaid flowchart to the design document. 
- Used in: assignment1_G01/src/a1_triage.py (results_to_csv and build_report functions) and docs/design.md

## Entry 5

- Date: 22/11/2026
- Tool: Gemini
- Purpose: understand requirements, check code structure, and verify ruff compliance
- Prompt: i uploaded the assignment brief and my assigned role for Member 2 (classify_variant and triage for Rules 1-6). here are the starter stubs and existing constants in a1_triage.py. guide me on implementing both functions without magic numbers or mutating inputs.
- Output: Explained the inclusive boundary conditions, strict rule order (1 to 6), case-insensitive string normalization, and comma-free reason strings[cite: 2, 3, 4]. Showed how to unpack the existing DECISIONS tuple and use PRIORITY_IMPACTS to avoid ruff magic-number warnings while creating shallow dictionary copies in triage[cite: 4, 6].
- Verified by: ran python -m ruff check src with zero errors and ran python -m pytest tests/test_visible.py to confirm the visible triage tests pass[cite: 1].
- My change: adapted the logic to match the exact starter stub signatures, defined NON_PRIORITY_IMPACTS, implemented classify_variant and triage, and verified input non-mutation.
- Used in: assignment1_G01/src/a1_triage.py (classify_variant and triage functions)

## Entry 6

- Date: 22/11/2026
- Tool: Gemini
- Purpose: debug CLI tool errors and fix Git pathspec issues
- Prompt: i ran `ruff check src` and `git add src/a1_triage.py` in PowerShell from the root repository folder, but got `CommandNotFoundException` for ruff, `os error 2` on `src`, and `fatal: pathspec 'src/a1_triage.py' did not match any files`. help me fix these errors.
- Output: Identified that the starter code resides inside the `assignment1_G01/` subdirectory rather than the repository root, and explained how to invoke ruff via `python -m ruff check src` within the active Python environment. Also highlighted potential hidden-test bugs in `classify_variant` such as numeric strings from CSVs needing `int()` casting and reason strings needing to be comma-free[cite: 2, 4].
- Verified by: navigated into `assignment1_G01/`, ran `python -m ruff check src` and `python -m pytest tests/test_visible.py` with exit code 0, and confirmed `git status` tracked the file properly[cite: 1, 6].
- My change: updated my working directory to `assignment1_G01/`, verified explicit `int()` casting and comma-free reason formatting in `classify_variant`, and successfully staged and pushed the fixed module to `master`[cite: 2, 4].
- Used in: assignment1_G01/src/a1_triage.py and local CLI verification workflow

## Group signatures

- Signed: AINURRULNAJWA BINTI SAHALAN, A24CS0223, 22/11/2026
- Signed: MUHAMMAD LUQMAN BIN MOHD AZMI, A24CS0138, 22/11/2026
- Signed: ABDUL RASYID BIN ABD GHANI, A24CS0030, 22/11/2026