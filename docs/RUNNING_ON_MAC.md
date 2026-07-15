# Running this on a Mac (step by step, no prior knowledge assumed)

You'll end up double-clicking a file that opens the interactive portal in your browser.
The **demo report needs no internet and no extra installs** — the only thing you truly need
is Python. Live data (real numbers) comes later in Part F.

---

## Part A — Install the tools (one time)

### A1. Install VS Code
1. Go to **https://code.visualstudio.com** → click **Download for macOS**.
2. Open your **Downloads** folder, double-click the `.zip` → you get **Visual Studio Code.app**.
3. Drag **Visual Studio Code** into your **Applications** folder.
4. Open it from Applications (if macOS says "downloaded from the internet", click **Open**).

### A2. Check whether you already have Python
1. In VS Code top menu: **Terminal → New Terminal**. A panel opens at the bottom — you type commands there.
2. Click into that panel, type this exactly, press **Return**:
   ```
   python3 --version
   ```
3. **If you see `Python 3.x.x`** → skip to Part B.
4. **If you see `command not found`, or a popup offers "install command line developer tools"** →
   click **Install**, wait ~5–10 min, then run `python3 --version` again.
   - If no popup appeared, type `xcode-select --install`, press Return, click **Install**, wait, retry.
   - Still nothing? Download the installer from **https://www.python.org/downloads/macos/**, run it
     (Continue/Agree/Install), then **quit and reopen VS Code** and run `python3 --version` again.

---

## Part B — Get the code onto your Mac

The repository is **private**, so the smoothest way is to let VS Code sign you into GitHub.

### Option 1 (recommended): Clone with VS Code
1. Press **⇧⌘P** (Shift+Command+P) → type **`Git: Clone`** → press Return.
2. Paste this URL and press Return:
   ```
   https://github.com/JoshuAI-888/Financial-data-providers.git
   ```
   *(If it errors, open the repo page in your browser, click the green **Code** button, and copy the
   HTTPS URL it shows — the owner's capitalization must match.)*
3. Choose **Documents** as the location → **Select as Repository Destination**.
4. If it says **"Sign in to GitHub"**, click **Allow** → browser opens → **Authorize** → back to VS Code.
5. When asked **"Open the cloned repository?"** → click **Open**.

### Option 2 (fallback): Download a ZIP (no Git sign-in)
1. In your browser open the repo page on github.com.
2. Top-left, click the **branch dropdown** and choose **`claude/milford-fmp-data-strategy-5nhxlm`**.
3. Green **Code** button → **Download ZIP**.
4. Open **Downloads**, double-click the ZIP → drag the unzipped folder into **Documents**.
5. In VS Code: **File → Open Folder…** → select that folder → **Open**
   (if asked, click **Yes, I trust the authors**). Then skip to Part D.

---

## Part C — Make sure you're on the right branch (Option 1 only)

1. Look at the **bottom-left** of VS Code — a small branch icon with a name.
2. If it doesn't say `claude/milford-fmp-data-strategy-5nhxlm`, click it.
3. Choose **`origin/claude/milford-fmp-data-strategy-5nhxlm`** from the list.
4. Confirm the left sidebar shows folders `fmp_milford`, `docs`, `outputs`, `tests` and files `run.py`, `README.md`.

---

## Part D — Run it (demo mode — no internet needed)

1. **Terminal → New Terminal**.
2. The text before your cursor should end with **`Financial-data-providers`**. If not, run:
   ```
   cd ~/Documents/Financial-data-providers
   ```
   *(ZIP users: if the folder name has extra text on the end, run `cd ~/Documents/` then `ls` to see
   the exact name, then `cd ` followed by that exact name.)*
3. Run:
   ```
   python3 run.py
   ```
4. **Success looks like:**
   ```
   [demo] building synthetic dataset for 32 companies...
   [*] transforming metrics...
   [*] building role insights...
   [*] 16 insights across 5 roles
   [done] wrote outputs/milford_fmp_report.html  (486 KB, self-contained)  mode=DEMO
   ```

---

## Part E — Open the report

1. In the left sidebar, expand the **`outputs`** folder.
2. **Right-click** `milford_fmp_report.html` → **Reveal in Finder**.
3. In Finder, **double-click** `milford_fmp_report.html` → it opens in your browser.
4. Click the role tabs, toggle company chips, drag the sliders, click any number to see its
   calculation, and open the "What this means & how it earns alpha" box on any widget.

---

## Part F — (Optional) Run with REAL data and your API key

Demo data is synthetic. For real US-company numbers you need internet access to FMP + your key.

1. **Rotate your key first.** Treat any previously shared key as burned. Log into
   **financialmodelingprep.com → Dashboard → API**, generate a **new** key, copy it.
2. In VS Code: **File → New File**, then **File → Save**, name it exactly **`.env`** (with the leading
   dot), save it **inside the Financial-data-providers folder**. If macOS warns about the dot, click **Use "."**.
3. Put this one line in it (your new key) and save (⌘S):
   ```
   FMP_API_KEY=your_new_key_here
   ```
4. In the terminal (inside the project folder), run:
   ```
   python3 run.py --live
   ```
   It prints per-endpoint latency, pulls data, and rewrites the HTML with **real numbers**
   (badge changes DEMO → LIVE). Open it as in Part E.
   - Speed test only: `python3 run.py --live --probe-only`
   - Stay under the 250-calls/day free limit: `python3 run.py --live --limit-sectors 3`

`.env` is git-ignored, so your key is never committed.

---

## Troubleshooting (by symptom)

| Symptom | Fix |
|---|---|
| `python3: command not found` | Finish Part A2 (python.org installer), then quit + reopen VS Code. |
| `can't open file '.../run.py': No such file or directory` | Terminal isn't in the project folder. Run `cd ~/Documents/Financial-data-providers` (or `ls` to find the exact name). |
| `zsh: permission denied` / wrong path | Run `cd ~/Documents/` then `ls`, then `cd` to the exact folder name shown. |
| Blank browser page | Double-click the file in `outputs/` so it opens as a local file; try Chrome. |
| Git Clone "authentication" / "repository not found" | Repo is private — use **Option 2 (Download ZIP)**. |
| `--live` hangs / `http=000` / `403` | Network blocks FMP or key is wrong. Verify the new key; try a normal home network (not a locked-down VPN). |
| `BudgetExceeded` | Hit the 250 calls/day free limit. Wait a day (cache is reused) or use `--limit-sectors 3`. |
| VS Code suggests the "Python extension" | Optional nicety — not required to run this. |

---

See also: [SUPPORT.md](SUPPORT.md) (operations), [FAQ.md](FAQ.md), and the top-level `README.md`.
