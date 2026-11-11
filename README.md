# Tattoo of the World

**An illustrated atlas of the world's tattoo traditions** — fifteen living (and
frozen) styles, from the Pazyryk ice mummies of the Altai and Japanese irezumi
to Māori tā moko and the flash sheets of American ports. A static site in a
vintage tattoo-parlor style, published on GitHub Pages.

**Live site:** https://dmitrylelee.github.io/tattooftheworld/

## The fifteen traditions

| # | Tradition | Region |
|---|-----------|--------|
| 1 | Pazyryk Ice Tattoos | Altai · Siberia |
| 2 | Irezumi | Japan |
| 3 | Tā moko | Aotearoa · New Zealand |
| 4 | Tatau (pe'a & malu) | Samoa |
| 5 | Enata Patterns (patu tiki) | Marquesas Islands |
| 6 | Sak Yant | Thailand |
| 7 | Chin Face Tattoos | Myanmar |
| 8 | American Traditional | United States |
| 9 | Batok | Philippines |
| 10 | Atayal Ptasan | Taiwan |
| 11 | Amazigh Tattoos | North Africa |
| 12 | Dayak Tattoos | Borneo |
| 13 | Ainu Sinuye | Hokkaidō · Japan |
| 14 | Kakiniit | The Arctic |
| 15 | Vory Tattoos | Russia |

## What's on the site

- **The Voyage of the Needle** — a world chart on the index with numbered pins
  and a dashed expedition route linking all fifteen traditions
- **The Flash Sheet** — the card grid of traditions, styled like designs pinned
  to a parlor wall
- **Five Thousand Years of Ink** — a chronology from Ötzi (c. 3300 BC) to the
  modern revivals
- **15 illustrated essays** (`styles/*.html`) — history, field notes, classic
  motifs, and a masonry gallery of captioned plates (~115 images)
- **About & credits** (`about.html`) — project notes and a full image ledger

## Structure

```
index.html          the flash sheet, map and timeline
about.html          project notes, image credits and licences
styles/*.html       one illustrated essay per tradition
assets/style.css    the vintage parlor stylesheet
assets/social-card.png  Open Graph / social preview image
tools/build.py      the static generator (all content lives here)
```

## Images & licences

All photographs and artworks are hot-linked from
[Wikimedia Commons](https://commons.wikimedia.org/) via `Special:FilePath` and
are public domain or Creative Commons licensed. Every plate links back to its
Commons file page with full author and licence information; a complete ledger
is on the [About page](https://dmitrylelee.github.io/tattooftheworld/about.html).

## Editing content

Everything — texts, facts, motifs, image lists, map pin positions, the
timeline — lives in `tools/build.py`. To change or add a tradition:

```bash
# edit the STYLES list (and MAP_PINS for the map), then regenerate:
python3 tools/build.py
```

The script rewrites `index.html`, `about.html` and `styles/*.html`. No
dependencies beyond Python 3. If you change `assets/style.css`, bump `VERSION`
in the script to bust browser caches.

## Design

Typefaces: [Rye](https://fonts.google.com/specimen/Rye) (woodtype display) and
[IM Fell English](https://fonts.google.com/specimen/IM+Fell+English) (antique
print body, the Fell Types digitised by Igino Marini). Palette: aged paper,
ink black, oxblood red, faded indigo. No frameworks, no JavaScript, no
tracking.
