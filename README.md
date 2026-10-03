# T.Ex Detective – build APK přes GitHub

## Postup (jde to celé z mobilu)
1. GitHub → **New repository** (např. `tex-app`), nech ho Public nebo Private.
2. **Add file → Upload files**: nahraj `main.py`, `buildozer.spec`, `.gitignore`, `README.md` → Commit.
3. **Add file → Create new file**, do názvu napiš přesně
   `.github/workflows/build.yml` (lomítka vytvoří složky),
   vlož obsah souboru `build.yml` → Commit.
4. Záložka **Actions** → „Build APK“ → běží (první build 30–60 min).
5. Po dokončení otevři běh → dole **Artifacts → TEx-apk** → stáhni a nainstaluj APK.
6. Když build spadne, stáhni artifact **buildozer-log** a pošli ho Claudovi.

## Po instalaci
Ruční povolení oprávnění: Nastavení → Aplikace → T.Ex → Oprávnění
(Fotky a videa, Kamera, Mikrofon, Poloha).
