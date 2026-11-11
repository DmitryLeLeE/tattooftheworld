# Tattoo of the World

An illustrated atlas of the world's tattoo traditions — ten living styles, from
Japanese irezumi and Māori tā moko to the flash sheets of American ports —
published as a static site on GitHub Pages.

**Live site:** https://dmitrylelee.github.io/tattooftheworld/

## What's inside

- `index.html` — the "flash sheet": a grid of all ten traditions
- `styles/*.html` — one illustrated essay per tradition (history, field notes, motifs, plates)
- `about.html` — project notes, image credits and licences
- `assets/style.css` — the vintage parlor stylesheet (aged paper, woodtype, sepia plates)
- `tools/build.py` — the static generator

## Images

All photographs and artworks are hot-linked from
[Wikimedia Commons](https://commons.wikimedia.org/) via `Special:FilePath`
and are public domain or Creative Commons licensed. Every plate links back to
its Commons file page with full author and licence information.

## Editing content

The content lives in one place — the `STYLES` list in `tools/build.py`
(texts, facts, motifs, image filenames). To add or change a tradition:

```bash
# edit tools/build.py, then regenerate:
python3 tools/build.py
```

The script rewrites `index.html`, `about.html` and `styles/*.html`.
No dependencies beyond Python 3.

## Design

Typefaces: [Rye](https://fonts.google.com/specimen/Rye) (woodtype display) and
[IM Fell English](https://fonts.google.com/specimen/IM+Fell+English) (antique
print body). Palette: aged paper, ink black, oxblood red, faded indigo.
No frameworks, no JavaScript, no tracking.
