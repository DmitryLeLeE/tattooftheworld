#!/usr/bin/env python3
"""Tattoo of the World — static site generator.

Edit the STYLES data below, then run:  python3 tools/build.py
Pages are written to the repository root (index.html, about.html, styles/*.html).
Images are hot-linked from Wikimedia Commons via Special:FilePath.
"""
import html
import pathlib
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "Tattoo of the World"
VERSION = "2"  # bump when assets/style.css changes, to bust browser caches


def commons(filename: str, width: int = 1000) -> str:
    return ("https://commons.wikimedia.org/wiki/Special:FilePath/"
            + urllib.parse.quote(filename) + f"?width={width}")


def commons_page(filename: str) -> str:
    return ("https://commons.wikimedia.org/wiki/File:"
            + urllib.parse.quote(filename.replace(" ", "_")))


# ---------------------------------------------------------------- content ---

STYLES = [
    {
        "slug": "japan",
        "region": "Japan",
        "name": "Irezumi",
        "native": "入れ墨 · 和彫り (wabori)",
        "card": "Full-body suits of koi, dragons and peonies, worked by hand with tebori needles.",
        "lede": ("In Japan the tattoo became a garment: a single composition of water, "
                 "wind, flowers and legend, cut to the shape of a jacket and worn for life."),
        "paragraphs": [
            ("Japanese tattooing is ancient — clay figures with incised faces go back "
             "millennia — but irezumi as we know it flowered in the Edo period "
             "(1603–1868). Woodblock prints of the <em>Suikoden</em>, a Chinese epic of "
             "outlaw heroes, swept the cities in the early 1800s; its heroes were drawn "
             "covered in tattoos, and firemen, labourers and palanquin bearers wanted "
             "the same skin. The print masters and the tattoo masters shared motifs, "
             "composition and even names: a tattooist is a <em>horishi</em> — a carver."),
            ("A classical body suit is one picture, not a collection. A background of "
             "wind bars and waves ties together koi carp (perseverance), dragons "
             "(wisdom and power), tigers, peonies, cherry blossom and figures from "
             "legend. The suit keeps a strict border — stopping at the wrists, the "
             "collar and above the knee — so that a kimono, or a rolled sleeve, hides "
             "it completely. Concealment is part of the form."),
            ("Tradition works by hand. In <em>tebori</em>, the master drives a rake of "
             "needles bound to a bamboo or steel handle with a steady rock of the "
             "wrist. The ink is sumi, the same carbon black used for calligraphy, "
             "which heals into a blue-grey that machine black rarely matches. A back "
             "piece can take years of weekly sittings, and the client traditionally "
             "earns the final signature panel only on completion."),
            ("The Meiji government banned tattooing in 1872 as the country opened to "
             "the West, and the craft survived underground — which welded it, in the "
             "public mind, to the yakuza. The ban fell in 1948, but many bathhouses "
             "and hot springs still turn tattooed guests away. Meanwhile the style "
             "itself has become one of the most imitated visual languages in world "
             "tattooing: every \"Japanese sleeve\" done in London or São Paulo is a "
             "quotation of Edo."),
        ],
        "facts": [
            ("Flowered", "Edo period, 1603–1868"),
            ("Technique", "Tebori — hand-poked needle rake"),
            ("Ink", "Sumi carbon black, heals blue-grey"),
            ("Canvas", "Body suit with strict garment borders"),
            ("Banned", "1872–1948"),
        ],
        "motifs": ["koi", "dragon", "tiger", "peony", "cherry blossom", "waves & wind bars", "Suikoden heroes"],
        "images": [
            {"file": "Japanese Tattoo by Kimbei or Stillfried.jpg",
             "caption": "Studio portrait of a tattooed man, hand-coloured albumen print, Japan, c. 1870s–1890s.",
             "credit": "Kusakabe Kimbei or Raimund von Stillfried — public domain"},
            {"file": "Beato, Felice (1834 – 1907) - Tattooed japanese men - ca. 1870.jpg",
             "caption": "Tattooed men, hand-coloured photograph by Felice Beato, c. 1870.",
             "credit": "Felice Beato — public domain"},
            {"file": "Irezumi Full Back.jpg",
             "caption": "A traditional full-back irezumi: the heroes Lu Zhishen and Shi Jin of the Suikoden. Tattoo work by Sujang.",
             "credit": "Photo via Wikimedia Commons"},
            {"file": "Japan Tattoo 1890s.jpg",
             "caption": "Tattooed man, Japan, 1890s.",
             "credit": "Public domain"},
            {"file": "Japanese Irezumi by Baron Stillfried.jpg",
             "caption": "Portrait of a man with irezumi, Baron Raimund von Stillfried, 1870s.",
             "credit": "Raimund von Stillfried — public domain"},
            {"file": "Kusakabe Kimbei - 153. Japanese Tattoo.jpg",
             "caption": "Japanese tattoo, albumen print by Kusakabe Kimbei.",
             "credit": "Kusakabe Kimbei — public domain"},
            {"file": "Espalda de hombre japonés tatuado.jpg",
             "caption": "The back of a tattooed Japanese man.",
             "credit": "Via Wikimedia Commons"},
            {"file": "Japanese postman. Image from book of 1902.jpg",
             "caption": "A tattooed Japanese postman, from a book of 1902.",
             "credit": "Public domain"},
            {"file": "Roshi Ensei lifting a heavy beam.jpg",
             "caption": "Rōshi Ensei lifting a heavy beam — a tattooed Suikoden hero by Utagawa Kuniyoshi, c. 1827. Prints like this made the style.",
             "credit": "Utagawa Kuniyoshi — public domain"},
            {"file": "Senkaji Chao wringing out hin loincloth.jpg",
             "caption": "Senkaji Chō, another of Kuniyoshi's tattooed Suikoden heroes.",
             "credit": "Utagawa Kuniyoshi — public domain"},
            {"file": "Marukin at Sanja Matsuri 3.jpg",
             "caption": "Irezumi shown openly at the Sanja Matsuri festival, Tokyo.",
             "credit": "Via Wikimedia Commons"},
            {"file": "Irezumi, l'art japonais du tatouage.jpg",
             "caption": "Irezumi — the Japanese art of tattooing.",
             "credit": "Via Wikimedia Commons"},
        ],
    },
    {
        "slug": "new-zealand",
        "region": "Aotearoa · New Zealand",
        "name": "Tā moko",
        "native": "tā moko · Māori",
        "card": "Carved spirals of ancestry and rank — a face that can be read like a signature.",
        "lede": ("Tā moko is not decoration but identity made visible: lineage, rank and "
                 "deeds carved into the skin in spirals that belong to one person only."),
        "paragraphs": [
            ("The Māori brought tattooing with them across Polynesia, and on Aotearoa "
             "it took a turn found almost nowhere else: the skin was not only "
             "punctured but carved. The <em>uhi</em> — a chisel of albatross bone — "
             "cut grooves that healed into ridges, so that a full facial moko had "
             "texture as well as line. The tattooist, the <em>tohunga tā moko</em>, "
             "was a tapu specialist, paid in treasures and fed by others while the "
             "work healed."),
            ("A moko is a document. The spirals and curves of the face are arranged in "
             "zones that speak of descent on the mother's and father's side, of rank, "
             "of standing within the hapū. Chiefs who signed the Treaty of Waitangi in "
             "1840 drew their moko as their signature — the most literal proof that a "
             "face pattern was understood as a name. Women traditionally wore the "
             "<em>moko kauae</em> on lips and chin."),
            ("Colonisation nearly extinguished the practice: missionary pressure, "
             "musket wars and the grim trade in preserved tattooed heads "
             "(<em>mokomokai</em>) made moko dangerous to wear. By the early twentieth "
             "century the full male facial moko had all but disappeared, surviving "
             "mainly in the portraits of painters like Gottfried Lindauer and in the "
             "chin moko of elder women."),
            ("Since the Māori renaissance of the 1980s, tā moko has returned as a "
             "living taonga — a treasure. Artists revived the forms, and today moko "
             "kauae are worn by members of parliament and broadcasters on the "
             "national news. The distinction matters here more than anywhere: moko "
             "belongs to whakapapa, to genealogy. Māori-style patterns worn by "
             "outsiders are called <em>kirituhi</em> — skin art — a courtesy of "
             "separation the tradition itself asks for."),
        ],
        "facts": [
            ("People", "Māori of Aotearoa"),
            ("Tool", "Uhi — albatross-bone chisel"),
            ("Form", "Carved grooves, healed ridges"),
            ("Meaning", "Genealogy, rank, personal identity"),
            ("Today", "Revived; moko kauae worn in public life"),
        ],
        "motifs": ["koru spiral", "pūhoro flank lines", "moko kauae (chin)", "zoned facial fields"],
        "images": [
            {"file": "Gottfried Lindauer - Tamati Waka Nene - Google Art Project.jpg",
             "caption": "Tāmati Wāka Nene, chief of Ngāpuhi, portrait by Gottfried Lindauer, 1890.",
             "credit": "Gottfried Lindauer — public domain"},
            {"file": "Tohunga-ta-moko at Work – Gottfried Lindauer.jpg",
             "caption": "The tohunga-tā-moko at work: moko carved into a man's face. Gottfried Lindauer.",
             "credit": "Gottfried Lindauer — public domain"},
            {"file": "MaoriChief1784.jpg",
             "caption": "Portrait of a Māori man with full facial moko, after Sydney Parkinson, 1784.",
             "credit": "After Sydney Parkinson — public domain"},
            {"file": "Hinepare.jpg",
             "caption": "Hinepare of Ngāti Kahungunu, with moko kauae, by Gottfried Lindauer.",
             "credit": "Gottfried Lindauer — public domain"},
            {"file": "Eruera Maihi Patuone, by Gottfried Lindauer.jpg",
             "caption": "Eruera Maihi Patuone, by Gottfried Lindauer.",
             "credit": "Gottfried Lindauer — public domain"},
            {"file": "Mrs Paramena, by Gottfried Lindauer.jpg",
             "caption": "Mrs Paramena, wearing moko kauae, by Gottfried Lindauer.",
             "credit": "Gottfried Lindauer — public domain"},
            {"file": "Wiremu Kingi, by Gottfried Lindauer.jpg",
             "caption": "Wiremu Kīngi of Te Āti Awa, by Gottfried Lindauer.",
             "credit": "Gottfried Lindauer — public domain"},
            {"file": "Maori chief, tattooed face, wearing dog-mat cape, green mere and earring, ca. 1870.jpg",
             "caption": "A chief with full facial moko, photograph, c. 1870.",
             "credit": "Public domain"},
            {"file": "Tawhiao Maori King 1880s.jpg",
             "caption": "King Tāwhiao, the second Māori King, 1880s.",
             "credit": "Public domain"},
            {"file": "Tā moko c1880.jpg",
             "caption": "Tā moko, photograph, c. 1880.",
             "credit": "Public domain"},
            {"file": "Self-portrait by Te Pehi Kupe.png",
             "caption": "Te Pēhi Kupe's self-portrait, 1826 — he drew his own moko from memory, without a mirror: proof it was known like a name.",
             "credit": "Te Pēhi Kupe — public domain"},
            {"file": "Māori traditional tattooing instrument with albatross bone blades.jpg",
             "caption": "Uhi — traditional tattooing instruments with albatross-bone blades.",
             "credit": "Via Wikimedia Commons"},
            {"file": "MaoriMoko.png",
             "caption": "The zones of the male facial moko, diagram.",
             "credit": "Via Wikimedia Commons"},
        ],
    },
    {
        "slug": "samoa",
        "region": "Samoa",
        "name": "Tatau",
        "native": "pe'a (men) · malu (women)",
        "card": "The unbroken Polynesian line — and the word the whole world borrowed: tatau.",
        "lede": ("Every tattoo on earth carries a Samoan word. Tatau — the sound of the "
                 "mallet on the comb — became 'tattoo' when Cook's crews brought it home "
                 "in 1769."),
        "paragraphs": [
            ("Samoa is the tradition that never broke. While missionaries suppressed "
             "tattooing across most of the Pacific, the Samoan <em>tufuga tā tatau</em> "
             "— master tattooists of hereditary guilds like the Sulu'ape family — kept "
             "working through the colonial era to the present day, with the same "
             "tools: a comb of bone or boar tusk lashed to a turtle-shell plate, "
             "struck with a mallet, and ink traditionally made from burnt candlenut "
             "soot."),
            ("The men's tattoo, the <em>pe'a</em>, runs from mid-torso to the knees — "
             "dense fields of straight black lines, zones and canoe motifs, laid out "
             "by eye without a stencil. It is finished over days or weeks of sessions "
             "attended by family, and to abandon it halfway, remaining <em>pe'a "
             "mutu</em>, is a lasting shame. The women's <em>malu</em> is lighter: an "
             "open lacework on the thighs, named for its central diamond motif of "
             "shelter and protection."),
            ("Receiving the tatau is a social act. It marks readiness to serve the "
             "family and village — to make the kava, to speak, to sit among the "
             "chiefs. The pain is the point as much as the pattern: borne quietly, "
             "with a relative holding the skin taut, it is proof of the endurance the "
             "design announces."),
            ("From Samoa and its neighbours the lines radiate outward — to Tonga, "
             "Tahiti, the Marquesas whose dense geometry astonished the first "
             "Europeans, and Hawai'i. The modern 'tribal' style of the 1990s is a "
             "distant, simplified echo of this family of patterns; the originals "
             "remain precise legal-social documents, applied by hand to the sound "
             "the word still remembers."),
        ],
        "facts": [
            ("Word", "'Tattoo' ← Samoan/Polynesian tatau, 1769"),
            ("Tools", "Bone comb, mallet, candlenut-soot ink"),
            ("Men", "Pe'a — waist to knees"),
            ("Women", "Malu — thigh lacework"),
            ("Lineage", "Unbroken guilds of tufuga tā tatau"),
        ],
        "motifs": ["straight-line fields", "canoe (va'a)", "flying fox", "malu diamond", "centipede (atualoa)"],
        "images": [
            {"file": "Traditional Samoan Tattoo - back.jpg",
             "caption": "A traditional Samoan pe'a, waist to below the knees, seen from behind.",
             "credit": "CloudSurfer — CC BY 3.0"},
            {"file": "Samoan tatau - tattooing circa 1895 - photo Thomas Andrew.jpg",
             "caption": "A tufuga tā tatau and his assistant at work with traditional tools, c. 1895. Photo: Thomas Andrew.",
             "credit": "Thomas Andrew — public domain"},
            {"file": "Back view Samoan male tatau - photo Thomas Andrew - 1890s.jpg",
             "caption": "Back view of a Samoan pe'a, 1890s. Photo: Thomas Andrew.",
             "credit": "Thomas Andrew — public domain"},
            {"file": "Samoan Tattoo - front detail.jpg",
             "caption": "Front detail of a pe'a.",
             "credit": "CloudSurfer, via Wikimedia Commons"},
            {"file": "Samoan Malu.jpg",
             "caption": "A Samoan woman's malu — the open lacework of the thigh.",
             "credit": "RunningToddler, via Wikimedia Commons"},
            {"file": "Taber photo (S. Francisco) - Samoan warrior - n. 8294 - Copyright 1894.jpg",
             "caption": "A Samoan warrior with pe'a, Taber photo, 1894.",
             "credit": "Public domain (1894)"},
        ],
    },
    {
        "slug": "thailand",
        "region": "Thailand",
        "name": "Sak Yant",
        "native": "สักยันต์ · yantra tattooing",
        "card": "Sacred geometry and Khmer script, tattooed by monks and charged with protective magic.",
        "lede": ("Sak yant is a tattoo that is also an amulet: a geometric yantra, hand-poked "
                 "by a monk or an ajarn, blessed with a breath of incantation."),
        "paragraphs": [
            ("The practice runs deep in mainland Southeast Asia — Thailand, Cambodia, "
             "Laos, Myanmar — blending Buddhist devotion, Hindu iconography and older "
             "animist magic. The designs are <em>yantra</em>: diagrams of power written "
             "in Khom, an old Khmer script, arranged in grids, spires and mandalas. "
             "Soldiers of Siam wore them into battle as armour against blades and "
             "bullets; truck drivers and kickboxers wear them today for much the same "
             "reasons."),
            ("Each yant has a job. The <em>gao yord</em>, nine Buddha-peaks, crowns "
             "the nape and is usually the first. The <em>paed tidt</em> wheel guards "
             "all eight directions of travel. The twin tigers give fearlessness; "
             "Hanuman gives daring; the gecko charms. Around the images run rows of "
             "<em>khata</em> — compressed Pali incantations — which carry the actual "
             "charge. An unfinished or unblessed yant is just a drawing."),
            ("The tattoo is made with a <em>khem sak</em>, a long steel rod sharpened "
             "to a split point, poked by hand at speed. The master — a monk or a lay "
             "<em>ajarn</em> — finishes by blowing the blessing into the fresh ink. "
             "The bearer accepts rules in exchange for the protection: precepts of "
             "conduct that keep the yant 'awake'. Break them, and the magic quietly "
             "leaves."),
            ("At Wat Bang Phra monastery west of Bangkok, thousands gather every "
             "March for the <em>wai khru</em> festival to recharge their tattoos; "
             "devotees fall into trance, taking on the animals they wear. The "
             "tradition is alive enough to have its own tourist economy and its own "
             "debates — about foreigners wearing Buddha images, and about what a "
             "blessing means when it is bought."),
        ],
        "facts": [
            ("Where", "Thailand, Cambodia, Laos, Myanmar"),
            ("Script", "Khom (old Khmer) khata incantations"),
            ("Tool", "Khem sak — split-point steel rod"),
            ("Makers", "Monks and lay masters (ajarn)"),
            ("Festival", "Wai khru at Wat Bang Phra, each March"),
        ],
        "motifs": ["gao yord nine peaks", "paed tidt eight directions", "twin tigers", "Hanuman", "khata script rows"],
        "images": [
            {"file": "Sak Yant Tattoo performed in thailand.jpg",
             "caption": "Sak yant on a back: the upper tattoo made by traditional hand-poke method.",
             "credit": "Ryaninuk — CC BY-SA 3.0"},
            {"file": "Sak-yant-gow-yord.jpg",
             "caption": "Gao yord, the nine-peak yant, at the nape — usually the first sak yant received.",
             "credit": "Mikhailovich — CC BY 3.0"},
            {"file": "Yant-tattoo.jpg",
             "caption": "A devotee of Wat Bang Phra covered in yant tattoos.",
             "credit": "Photo: Spencer Littlewood — public domain"},
            {"file": "Yant Paed Tidt.jpg",
             "caption": "Yant paed tidt — the eight-directions yant, protection wherever you travel.",
             "credit": "Photo: Spencer Littlewood — public domain"},
            {"file": "Yant-tattoos2.jpg",
             "caption": "Yant tattoos across a back.",
             "credit": "Via Wikimedia Commons"},
            {"file": "Sak Yant Chiang Mai.jpg",
             "caption": "Sak yant work in Chiang Mai.",
             "credit": "Via Wikimedia Commons"},
            {"file": "404 Sak Yant Tattoo (16).jpg",
             "caption": "Sak yant, 2006.",
             "credit": "Lychiang, via Wikimedia Commons"},
            {"file": "420 Sak Yant Tattoo (32).jpg",
             "caption": "Sak yant with khata script rows, 2006.",
             "credit": "Lychiang, via Wikimedia Commons"},
            {"file": "Thai tattoo Chiang Mai 2005 058.jpg",
             "caption": "Traditional tattooing, Chiang Mai, 2005.",
             "credit": "Via Wikimedia Commons"},
            {"file": "Needles Wat Bang Phra.JPG",
             "caption": "The khem sak rods at Wat Bang Phra monastery.",
             "credit": "Via Wikimedia Commons"},
            {"file": "Wat-bang-phra.jpg",
             "caption": "Wat Bang Phra, the monastery of the tattoo festival.",
             "credit": "Via Wikimedia Commons"},
        ],
    },
    {
        "slug": "usa",
        "region": "United States",
        "name": "American Traditional",
        "native": "old school · sailor tattoo",
        "card": "Bold will hold: anchors, swallows and roses from the sailor ports of two world wars.",
        "lede": ("Thick black outlines, five flat colours, and a promise in the trade's own "
                 "words: bold will hold. The flash sheet on the parlor wall is this style's "
                 "scripture — and this site's design."),
        "paragraphs": [
            ("American traditional grew in port towns and navy yards. Sailors had "
             "carried tattoo customs home since the Pacific voyages of the 1700s, and "
             "by the Civil War era professional artists worked the waterfronts. In "
             "1891 Samuel O'Reilly of New York patented the first electric tattoo "
             "machine, built on Edison's autographic pen — and speed changed "
             "everything. Designs standardised into <em>flash</em>: sheets of "
             "ready-to-wear images pinned to the wall, picked by number."),
            ("The iconography is a sailor's diary. A swallow for 5,000 nautical "
             "miles — and for coming home, as swallows do. An anchor for stability or "
             "an Atlantic crossing; a full-rigged ship for rounding Cape Horn; "
             "<em>HOLD FAST</em> on the knuckles to keep grip on the rigging; a pig "
             "and a rooster on the feet against drowning. Roses, daggers, hearts "
             "marked MOM — love and luck in five pigments that would survive decades "
             "of sun and salt."),
            ("The style's grammar was set by working artists with navy clientele: "
             "heavy outline laid first, black shading, then red, green, yellow, "
             "brown. No gradients a healed tattoo couldn't keep. Norman 'Sailor "
             "Jerry' Collins, working from Honolulu's Hotel Street through the "
             "Second World War, fused the American line with Japanese composition "
             "he admired across the Pacific, and trained the generation — Ed Hardy "
             "among them — that carried the style into the tattoo renaissance."),
            ("Driven near-underground by mid-century bans (New York City outlawed "
             "tattooing outright from 1961 to 1997), old school returned as the "
             "backbone of the modern craft. Its rules still teach apprentices what "
             "a tattoo must do: read across a room, and hold for a lifetime."),
        ],
        "facts": [
            ("Machine", "Patented by Samuel O'Reilly, 1891"),
            ("Palette", "Black outline + red, green, yellow, brown"),
            ("Canon", "Flash sheets, picked off the wall"),
            ("Key figure", "Sailor Jerry Collins, Honolulu"),
            ("Rule", "Bold will hold"),
        ],
        "motifs": ["swallow", "anchor", "rose", "dagger & heart", "ship in full sail", "HOLD FAST knuckles"],
        "images": [
            {"file": "Tattooed sailor aboard the USS New Jersey.jpg",
             "caption": "A much-tattooed sailor aboard the USS New Jersey, 1944. Photo by Charles Fenno Jacobs.",
             "credit": "U.S. Navy / National Archives — public domain"},
            {"file": "Sailor tattoos - \"Hold Fast\" with swallows.jpg",
             "caption": "HOLD FAST across the knuckles, with swallows — U.S. Navy, 2020.",
             "credit": "U.S. Navy / Levingston M. Lewis — public domain"},
            {"file": "US Navy eagle tattoo in traditional style.jpg",
             "caption": "An eagle in traditional style, aboard USS Theodore Roosevelt.",
             "credit": "U.S. Navy — public domain"},
            {"file": "Person's hand with tattoo of skull, anchor, and life preserver.jpg",
             "caption": "Skull, anchor and life preserver on a sailor's hand.",
             "credit": "U.S. Navy — public domain"},
            {"file": "Man in uniform with rose tattoo on arm.jpg",
             "caption": "A rose in traditional style on a sailor's arm.",
             "credit": "U.S. Navy — public domain"},
            {"file": "160517-N-XX333-001 (27147696875).jpg",
             "caption": "Navy ink, photographed aboard USS Springfield, 2016.",
             "credit": "U.S. Navy — public domain"},
            {"file": "Sailor Jerry Ad (5189229064) (cropped).jpg",
             "caption": "Sailor Jerry flash — swallows, ships and roses in the classic grammar.",
             "credit": "Photo: Paul Sableman, via Wikimedia Commons"},
        ],
    },
    {
        "slug": "philippines",
        "region": "Philippines",
        "name": "Batok",
        "native": "batok · batek · Kalinga",
        "card": "Mountain-province geometry tapped in with a thorn — kept alive by the mambabatok of Buscalan.",
        "lede": ("In the Cordillera mountains of Luzon, tattoos were earned: centipedes and "
                 "eagles for warriors, ladders and rice bundles for abundance, tapped into "
                 "the skin with a pomelo thorn."),
        "paragraphs": [
            ("When Spanish ships reached the Visayas in the 1500s they called the "
             "islands <em>Las Islas de los Pintados</em> — the isles of the painted "
             "ones — because the people they met were tattooed from head to foot. "
             "Colonisation and conversion erased most of that lowland tradition; it "
             "survived in the mountains of northern Luzon, among peoples the empire "
             "never fully reached — Kalinga, Bontoc, Ifugao."),
            ("Batok is tapped, not poked: a thorn from a pomelo or calamansi tree set "
             "in a short stick, struck with a second stick, driving soot from cooking "
             "fires under the skin. The patterns are geometric and local — "
             "<em>gayaman</em>, the centipede guide of warriors; the python's skin; "
             "ladders, rice bundles, and the stepped chest pieces that marked a "
             "Kalinga man who had taken heads in defence of his village. For women, "
             "arm tattoos marked beauty, fertility and standing."),
            ("The tradition narrowed to a single village and very nearly to a single "
             "pair of hands. Apo Whang-od Oggay of Buscalan, born around 1917, "
             "learned batok as a teenager and kept practising when every other "
             "mambabatok had stopped. Rediscovered by documentary-makers in the "
             "2000s, she became a national icon — a Vogue cover at 106 — and her "
             "village a pilgrimage: travellers hike the rice terraces to receive her "
             "three-dot signature."),
            ("Because the craft passes only within the bloodline, Whang-od trained "
             "her grandnieces Grace Palicas and Elyang Wigan, and dozens of young "
             "Buscalan tattooists now work the thorn. The revival runs on tourism, "
             "with everything that brings — but the sound in the village is the old "
             "one: tap, tap, tap."),
        ],
        "facts": [
            ("Where", "Kalinga, Cordillera, Luzon"),
            ("Tool", "Pomelo thorn, tapped; soot ink"),
            ("Earned by", "Warriors' deeds; women's coming of age"),
            ("Keeper", "Apo Whang-od of Buscalan, b. c. 1917"),
            ("Heirs", "Grace Palicas, Elyang Wigan & Buscalan youth"),
        ],
        "motifs": ["gayaman centipede", "python scales", "ladder & rice bundle", "stepped chest piece", "three-dot signature"],
        "images": [
            {"file": "Whang-od tattooing.jpg",
             "caption": "Apo Whang-od, mambabatok of Buscalan, tapping a batok tattoo, 2016.",
             "credit": "Mawg64 — CC BY-SA 4.0"},
            {"file": "Young Kalinga woman of Patiquian, Bontoc, showing arm tattoos (1906).png",
             "caption": "A young Kalinga woman showing arm tattoos, 1906.",
             "credit": "Public domain (1906)"},
            {"file": "Whang-od and a recently tattooed visitor..jpg",
             "caption": "Whang-od and a freshly tattooed visitor, Buscalan.",
             "credit": "Via Wikimedia Commons"},
            {"file": "Ink road (Apo Whang-od) 13.jpg",
             "caption": "On the ink road to Buscalan: batok in progress.",
             "credit": "Photo: Lee, via Wikimedia Commons"},
            {"file": "Ink road (Apo Whang-od) 32.jpg",
             "caption": "The thorn and the tapping stick at work.",
             "credit": "Photo: Lee, via Wikimedia Commons"},
            {"file": "Ink road (Apo Whang-od) 20.jpg",
             "caption": "Soot ink, mixed from the cooking fire.",
             "credit": "Photo: Lee, via Wikimedia Commons"},
            {"file": "The Last Tattooed Woman of Kalinga.jpg",
             "caption": "A tattooed elder of Kalinga.",
             "credit": "Via Wikimedia Commons"},
            {"file": "Lakay Wanawan - Kalinga people (c.1912).png",
             "caption": "Lakay Wanawan of the Kalinga, with warrior's chest piece, c. 1912.",
             "credit": "Public domain"},
            {"file": "Tingian woman of Balbalasan, Bontoc, showing tattoos on forearms (1906).png",
             "caption": "A Tingian woman showing forearm tattoos, 1906.",
             "credit": "Public domain"},
            {"file": "Isneg tattoos (1929).png",
             "caption": "Isneg tattoo patterns, recorded 1929.",
             "credit": "Public domain"},
            {"file": "Arm tattoos of (37) Ibaloi woman; Northern Kalinga woman (38,39); and Northern Kalinga man (40).png",
             "caption": "Arm tattoos of Ibaloi and Kalinga women and men, recorded 1929.",
             "credit": "Public domain"},
        ],
    },
    {
        "slug": "north-africa",
        "region": "North Africa",
        "name": "Amazigh Tattoos",
        "native": "ⵜⴰⵎⴰⵣⵉⵖⵜ · Berber women's tattoos",
        "card": "Chin, brow and hands marked with palm, diamond and dot — the oldest ink of the Maghreb.",
        "lede": ("Across the Atlas mountains and the Maghreb plains, Amazigh women wore "
                 "tattoos the way the land wears its marks: a palm on the chin, a diamond "
                 "on the brow, dots at the corner of the eye."),
        "paragraphs": [
            ("The Imazighen — the free people, whom outsiders called Berbers — carried "
             "a tattoo tradition measured in millennia, worn almost entirely by "
             "women. The marks sat where clothing never covered: the chin, the "
             "forehead, cheeks, the backs of hands, ankles. A vertical chin line "
             "called <em>siyala</em>, palm fronds, diamonds, chevrons and crosses — "
             "the same vocabulary woven into carpets and painted on pottery across "
             "the region."),
            ("The marks worked. They protected against the evil eye, carried "
             "fertility and healing (a dot at the temple against headache, marks "
             "over an ailing joint), identified tribe and region, and recorded a "
             "woman's passages — betrothal, marriage, children. Applied around "
             "puberty by older women with soot and needle, they were medicine, "
             "jewellery and record in one."),
            ("Islamic orthodoxy regards tattooing as forbidden, and for centuries the "
             "practice lived in negotiation with that judgment — sometimes relaxed, "
             "sometimes enforced. Through the twentieth century, urbanisation, "
             "schooling and religious revival steadily ended new tattoos; many older "
             "women were even persuaded to regret theirs. The last fully tattooed "
             "generation — women now in their eighties and nineties in the Atlas and "
             "Aurès — are the tradition's final primary sources."),
            ("Documentation has become the afterlife of the practice: photographers "
             "and granddaughters recording faces while they remain, and a young "
             "Amazigh diaspora re-wearing the symbols — sometimes in ink, more often "
             "in silver — as a statement of identity in a region still arguing about "
             "its Amazigh roots."),
        ],
        "facts": [
            ("People", "Imazighen (Berbers) of the Maghreb"),
            ("Worn by", "Women — face, hands, ankles"),
            ("Key mark", "Siyala — the vertical chin line"),
            ("Purpose", "Protection, fertility, tribe, passage"),
            ("Status", "Ending with the last tattooed generation"),
        ],
        "motifs": ["siyala chin line", "palm frond", "diamond (eye)", "chevrons", "temple dots"],
        "images": [
            {"file": "COLLECTIE TROPENMUSEUM Berbervrouw met gezichtstatoeages en traditionele sieraden TMnr 20017653.jpg",
             "caption": "Amazigh woman with facial tattoos and traditional jewellery, Morocco, 1970. Photo: Frits Cowan.",
             "credit": "Collectie Wereldmuseum (Tropenmuseum) — CC BY-SA 3.0"},
            {"file": "A Bedouin woman, Tunis, Tunisia-LCCN2001699406.jpg",
             "caption": "A Bedouin woman with facial tattoos, Tunis, c. 1899. Photochrom print.",
             "credit": "Library of Congress — public domain"},
            {"file": "Tatouages amazigh.jpg",
             "caption": "Amazigh tattoo designs of Algeria and Tunisia, recorded by E.-G. Gobert, 1924.",
             "credit": "E.-G. Gobert, via Wikimedia Commons"},
            {"file": "COLLECTIE TROPENMUSEUM Berbervrouw uit de Midden Atlas TMnr 10028644.jpg",
             "caption": "Amazigh woman of the Middle Atlas, Morocco.",
             "credit": "Collectie Wereldmuseum (Tropenmuseum) — CC BY-SA 3.0"},
            {"file": "COLLECTIE TROPENMUSEUM Tunesische Berbervrouw. TMnr 60032650.jpg",
             "caption": "Tunisian Amazigh woman with facial tattoos.",
             "credit": "Collectie Wereldmuseum (Tropenmuseum) — CC BY-SA 3.0"},
            {"file": "COLLECTIE TROPENMUSEUM Berberse tapijtknoopster uit Zemmour TMnr 10028617.jpg",
             "caption": "A carpet-knotter of Zemmour — the same diamonds in wool and on skin.",
             "credit": "Collectie Wereldmuseum (Tropenmuseum) — CC BY-SA 3.0"},
            {"file": "A Bedouin woman Tunis Tunisia.jpg",
             "caption": "A Bedouin woman of Tunis with chin and brow marks, photochrom, c. 1899.",
             "credit": "Public domain"},
            {"file": "Abb. 317. Berberin aus südlichen Algier.jpg",
             "caption": "Amazigh woman of southern Algeria, early photograph.",
             "credit": "Public domain"},
            {"file": "A Tattooed Girl. (1836) - TIMEA.jpg",
             "caption": "'A tattooed girl', engraving, 1836.",
             "credit": "Public domain"},
            {"file": "Kabylenweib.jpg",
             "caption": "A Kabyle woman, historical photograph.",
             "credit": "Public domain"},
        ],
    },
    {
        "slug": "borneo",
        "region": "Borneo",
        "name": "Dayak Tattoos",
        "native": "Iban · Kayan · Kenyah",
        "card": "The bunga terung rosette on the shoulders of travellers — ink as a map of journeys.",
        "lede": ("Among the Dayak peoples of Borneo, tattoos were a travelogue: each "
                 "journey, skill and deed earned its mark, until a life could be read "
                 "off the skin."),
        "paragraphs": [
            ("Borneo's longhouse peoples — Iban, Kayan, Kenyah, Ngaju and others — "
             "built one of the great tattoo cultures of the world. Designs were "
             "carved in relief on wooden blocks, inked with soot, stamped on the "
             "skin and then worked in with two sticks: a needle set in one, tapped "
             "with the other — the hand-tap method that modern revivalists across "
             "the world still call 'Borneo style'."),
            ("For Iban men the sequence began with the <em>bunga terung</em>, the "
             "eggplant flower, one rosette on each shoulder — the mark of "
             "<em>bejalai</em>, the journey a young man makes into the world to gain "
             "knowledge and standing. Throat pieces, dog-dragons (<em>aso</em>), "
             "scorpions and hornbills followed particular achievements; in the old "
             "head-taking era, hand tattoos announced the gravest deed of all. "
             "Kayan and Kenyah women bore the finest work — dense lace from knuckle "
             "to thigh, applied over years, a mark of endurance and status."),
            ("The patterns are a shared vocabulary with Dayak carving and beadwork: "
             "curling fern shoots, the aso dragon-dog that guards against spirits, "
             "hornbill heads for the upper world. Missionaries and colonial "
             "administrations discouraged the practice through the twentieth "
             "century, and by its end full traditional coverage had become rare."),
            ("Revival came from both directions: urban Dayak artists reclaiming "
             "hand-tap technique and longhouse iconography, and the global craft "
             "adopting Borneo rosettes and scrollwork — often loosely. On the "
             "island itself the bunga terung is again a common sight on young "
             "shoulders: the journey mark, for a generation whose bejalai may be "
             "a flight to Kuala Lumpur rather than a river passage."),
        ],
        "facts": [
            ("Peoples", "Iban, Kayan, Kenyah, Ngaju"),
            ("Method", "Hand-tap; carved block stencils"),
            ("First mark", "Bunga terung — journey rosette"),
            ("Women's work", "Dense Kayan forearm-to-thigh lace"),
            ("Meaning", "Journeys, deeds, protection"),
        ],
        "motifs": ["bunga terung rosette", "aso dragon-dog", "fern scroll", "hornbill", "throat piece"],
        "images": [
            {"file": "COLLECTIE TROPENMUSEUM Getatoeëerde Dajak Borneo TMnr 10002836.jpg",
             "caption": "Sawang Kalong, a tattooed Dayak man of the Kahayan river, Borneo, 1920–1925. Photo: Jean Demmeni.",
             "credit": "Collectie Wereldmuseum (Tropenmuseum) — CC BY-SA 3.0"},
            {"file": "Dayak Types, Borneo.jpg",
             "caption": "Three Dayak men, engraving, Popular Science, 1890.",
             "credit": "Popular Science, 1890 — public domain"},
            {"file": "COLLECTIE TROPENMUSEUM Het aanbrengen van een tatoeage door een Dajak West-Borneo. TMnr 60031303.jpg",
             "caption": "Applying a tattoo by hand-tap, West Borneo.",
             "credit": "Collectie Wereldmuseum (Tropenmuseum) — CC BY-SA 3.0"},
            {"file": "COLLECTIE TROPENMUSEUM Portret van een getatoeëerde Ot Danum Dajak man uit het Kahajan gebied van Midden-Borneo. TMnr 60046429.jpg",
             "caption": "A tattooed Ot Danum Dayak man of the Kahayan region, Central Borneo.",
             "credit": "Collectie Wereldmuseum (Tropenmuseum) — CC BY-SA 3.0"},
            {"file": "COLLECTIE TROPENMUSEUM Tatoeëring van de handrug van een Dajak meisje Borneo TMnr 60051448.jpg",
             "caption": "Tattooing the back of a Dayak girl's hand, Borneo.",
             "credit": "Collectie Wereldmuseum (Tropenmuseum) — CC BY-SA 3.0"},
            {"file": "COLLECTIE TROPENMUSEUM Portret van een Boekat Dajak meisje Borneo. TMnr 60045280.jpg",
             "caption": "A Bukat Dayak girl, Borneo.",
             "credit": "Collectie Wereldmuseum (Tropenmuseum) — CC BY-SA 3.0"},
        ],
    },
    {
        "slug": "ainu",
        "region": "Hokkaidō · Japan",
        "name": "Ainu Sinuye",
        "native": "シヌイェ · mouth tattoo (anchi-piri)",
        "card": "The smile tattooed around women's lips — a northern tradition the empire tried to erase.",
        "lede": ("Among the Ainu of Hokkaidō, Sakhalin and the Kurils, a woman's tattoo "
                 "began in childhood as a dot on the lip and grew, year by year, into the "
                 "broad smile-shaped mark of adulthood."),
        "paragraphs": [
            ("The Ainu, the indigenous people of Japan's far north, kept a tattoo "
             "tradition entirely of women, made by women. The <em>sinuye</em> began "
             "with a small mark on a girl's upper lip, enlarged over years until, by "
             "marriageable age, a full tattoo framed the mouth — with matching bands "
             "and interlace on the forearms and hands. The pigment was birch-bark "
             "soot, cut into the skin and wiped with an antiseptic brew of ash "
             "bark."),
            ("The mouth tattoo made a woman complete: ready for marriage, protected "
             "against illness-spirits entering by the lips, and recognisable to her "
             "ancestors in the world after death. Untattooed, a woman risked going "
             "unrecognised. The tattooist was an aunt or grandmother, and the craft "
             "passed down the female line with its chants and taboos."),
            ("The Japanese state outlawed Ainu tattooing twice — in 1799 and again in "
             "1871 — as part of assimilation policy that also banned the language "
             "and earrings of men. Women kept tattooing in secret for decades; the "
             "last women with full traditional sinuye died in the late twentieth "
             "century. Photographs from the Meiji era to the 1950s preserve the "
             "form the law tried to erase."),
            ("Today, as Ainu identity is publicly reclaimed — the people were "
             "recognised as indigenous by Japan only in 2008 and by law in 2019 — "
             "the tattoo returns mostly as image: drawn on for dance performances "
             "and festivals, studied by descendants, and occasionally re-inked for "
             "good by Ainu women taking the old mark into a new century."),
        ],
        "facts": [
            ("People", "Ainu — Hokkaidō, Sakhalin, Kurils"),
            ("Worn by", "Women; tattooed by women"),
            ("Mark", "Mouth tattoo, arm bands & interlace"),
            ("Pigment", "Birch-bark soot"),
            ("Banned", "1799 and 1871, by assimilation edicts"),
        ],
        "motifs": ["mouth tattoo", "forearm interlace", "braid bands", "protective dots"],
        "images": [
            {"file": "Ainu woman with mouth tattoos and live bear.jpg",
             "caption": "An Ainu woman with mouth tattoo, photographed with a bear cub.",
             "credit": "Via Wikimedia Commons — public domain"},
            {"file": "TatouageAinou.png",
             "caption": "Ainu tattooing of the mouth and hands, historical illustration.",
             "credit": "Via Wikimedia Commons — public domain"},
            {"file": "Ainuschönheit (Sammlung Bälz).jpg",
             "caption": "An Ainu woman with sinuye, from the Bälz collection.",
             "credit": "Public domain"},
            {"file": "Ainu-woman-1930-2.jpg",
             "caption": "Ainu woman with mouth tattoo, 1930.",
             "credit": "Public domain"},
            {"file": "Tamoto Kenzō - Ainu Women.jpg",
             "caption": "Ainu women, photograph by Tamoto Kenzō, Meiji era.",
             "credit": "Tamoto Kenzō — public domain"},
            {"file": "HirasawaByozanFemme.png",
             "caption": "An Ainu woman, painting by Hirasawa Byōzan.",
             "credit": "Hirasawa Byōzan — public domain"},
            {"file": "Ainu woman (from a book Published in 1931) P.81.png",
             "caption": "Ainu woman with full mouth tattoo and hand marks, 1931.",
             "credit": "Public domain"},
        ],
    },
    {
        "slug": "russia",
        "region": "Russia",
        "name": "Vory Tattoos",
        "native": "наколки · thieves' tattoos",
        "card": "Stars, cupolas and epaulettes — the coded service record of the Soviet prison world.",
        "lede": ("In the Gulag and the prison camps after it, tattoos became a closed "
                 "written language: rank, sentence, defiance and biography, inked in "
                 "code that other prisoners could read at a glance."),
        "paragraphs": [
            ("Russian criminal tattooing crystallised in the Soviet camp system, "
             "where millions passed through barracks that mixed professional "
             "thieves with everyone else. Among the <em>vory v zakone</em> — "
             "thieves-in-law, the criminal aristocracy — tattoos functioned as "
             "documents: a cathedral with cupolas counted convictions, one dome "
             "per sentence; eight-pointed stars on the collarbones or knees "
             "declared rank and refusal ('I kneel to no one'); an epaulette on "
             "the shoulder marked criminal officer class."),
            ("The code was enforced. A tattoo claimed status, and a claim had to "
             "be backed — wearing unearned stars in the camps invited brutal "
             "correction, including forcible removal. Cats for thieves, rings on "
             "the fingers spelling out articles of conviction, Lenin on the chest "
             "(folk wisdom held that guards would not shoot at the leader): every "
             "image was a sentence in an argot of defiance against the state."),
            ("The ink itself was camp-made — burnt boot heel and urine, worked in "
             "with sharpened guitar string — and the health risks were part of the "
             "price. Major Danzig Baldaev, a prison warden's son working in "
             "Leningrad's Kresty prison, spent decades secretly drawing and "
             "cataloguing thousands of these tattoos; his archive, published as "
             "the <em>Russian Criminal Tattoo Encyclopaedia</em>, is the "
             "tradition's unlikely monument."),
            ("The old code loosened after the Soviet collapse: the market economy "
             "reshuffled the underworld, and by the 2000s tattoos in Russia were "
             "increasingly just tattoos. But the visual language — stark blue-black "
             "line, church domes, stars, barbed wire counting years — escaped into "
             "world culture, quoted in cinema and fashion, its grammar studied by "
             "the criminologists it was invented to evade."),
        ],
        "facts": [
            ("Where", "Soviet Gulag & prison system"),
            ("Caste", "Vory v zakone — thieves-in-law"),
            ("Grammar", "Domes = sentences; stars = rank"),
            ("Ink", "Soot of burnt rubber, guitar-string needle"),
            ("Archive", "Danzig Baldaev's encyclopaedia"),
        ],
        "motifs": ["eight-pointed stars", "cathedral cupolas", "epaulettes", "finger rings", "barbed wire"],
        "images": [
            {"file": "Tattooed former Soviet prisoner.jpg",
             "caption": "A former Soviet prisoner with camp tattoos.",
             "credit": "www.pvz.lt, via Wikimedia Commons"},
            {"file": "Russian Criminal Tattoo - Epaulette.png",
             "caption": "An epaulette tattoo — the mark of criminal 'officer class'.",
             "credit": "Yeghishedaviti — CC BY-SA 4.0"},
            {"file": "Jewish Russian Criminal Tattoo.jpg",
             "caption": "A prison tattoo recorded by Danzig Baldaev for his encyclopaedia of the genre.",
             "credit": "Danzig Baldaev, via Wikimedia Commons"},
        ],
    },
]

# ------------------------------------------------------------------ assets ---

SWALLOW_L = """<svg class="swallow swallow-l" viewBox="0 0 120 90" aria-hidden="true"><path d="M8 12 C34 2 58 10 66 30 C70 40 70 48 66 56 C78 50 94 50 112 60 C92 62 80 68 72 78 C70 86 66 88 62 84 C60 80 60 74 62 68 C50 74 36 74 26 66 C38 64 46 58 50 50 C38 54 24 50 16 40 C28 42 38 38 44 30 C32 30 18 24 8 12 Z" fill="currentColor"/><circle cx="56" cy="24" r="2.6" fill="var(--paper)"/></svg>"""
SWALLOW_R = SWALLOW_L.replace('swallow-l', 'swallow-r')

DIVIDER = """<div class="divider" aria-hidden="true"><span class="rule"></span><svg viewBox="0 0 44 24" class="div-mark"><path d="M22 2 L26 10 L34 12 L26 14 L22 22 L18 14 L10 12 L18 10 Z" fill="currentColor"/><circle cx="4" cy="12" r="1.8" fill="currentColor"/><circle cx="40" cy="12" r="1.8" fill="currentColor"/></svg><span class="rule"></span></div>"""

CSS = """/* Tattoo of the World — vintage parlor stylesheet */
:root{
  --paper:#e8dbba; --paper-deep:#ddcc9e; --paper-dark:#cdb989;
  --ink:#241b12; --ink-soft:#4a3c2a;
  --oxblood:#8c2f26; --indigo:#2e4756; --ochre:#9c7021;
  --frame:3px solid var(--ink);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{
  background:var(--paper);
  background-image:
    radial-gradient(ellipse at 50% 0%, rgba(255,250,230,.5), rgba(0,0,0,0) 60%),
    radial-gradient(ellipse at 50% 100%, rgba(120,90,40,.18), rgba(0,0,0,0) 55%);
  color:var(--ink);
  font-family:"IM Fell English",Georgia,serif;
  font-size:1.1rem; line-height:1.65;
}
body::after{/* paper grain */
  content:""; position:fixed; inset:0; pointer-events:none; z-index:999;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)' opacity='.05'/%3E%3C/svg%3E");
}
a{color:var(--oxblood)}
a:hover{color:var(--indigo)}
a:focus-visible,button:focus-visible{outline:3px solid var(--oxblood);outline-offset:2px}
img{max-width:100%;display:block}
.wrap{max-width:1060px;margin:0 auto;padding:0 20px}

/* small caps label */
.sc{font-family:"IM Fell English SC",Georgia,serif;letter-spacing:.08em}

/* header / nav */
.masthead{border-bottom:var(--frame);background:rgba(221,204,158,.6)}
.masthead .wrap{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:12px 20px;flex-wrap:wrap}
.brand{font-family:"Rye",serif;font-size:1.25rem;color:var(--ink);text-decoration:none}
.brand:hover{color:var(--oxblood)}
nav.crumbs{display:flex;gap:18px;flex-wrap:wrap}
nav.crumbs a{text-decoration:none;font-family:"IM Fell English SC",serif;font-size:1.05rem}

/* hero */
.hero{text-align:center;padding:64px 20px 36px;position:relative;overflow:hidden}
.hero .over{font-family:"IM Fell English SC",serif;font-size:1.2rem;letter-spacing:.14em;color:var(--ink-soft)}
.hero h1{
  font-family:"Rye",serif;font-weight:400;color:var(--ink);
  font-size:clamp(2.6rem,9vw,6.2rem);line-height:.95;margin:.18em 0 .1em;
  text-shadow:3px 3px 0 var(--paper-dark);
}
.hero h1 .of{display:block;font-size:.38em;letter-spacing:.3em;color:var(--oxblood);text-shadow:none;margin:.5em 0 .3em}
.hero .sub{max-width:52ch;margin:14px auto 0;font-style:italic;color:var(--ink-soft);font-size:1.15rem}
.hero .est{margin-top:20px;display:inline-block;border:2px solid var(--oxblood);color:var(--oxblood);
  padding:4px 18px;font-family:"IM Fell English SC",serif;letter-spacing:.12em;transform:rotate(-1.4deg)}
.swallow{position:absolute;width:110px;color:var(--indigo);opacity:.9;top:70px}
.swallow-l{left:max(12px,8vw)}
.swallow-r{right:max(12px,8vw);transform:scaleX(-1)}
@media(max-width:760px){.swallow{width:64px;top:30px;opacity:.55}}

/* divider ornament */
.divider{display:flex;align-items:center;gap:12px;max-width:520px;margin:30px auto;color:var(--oxblood)}
.divider .rule{flex:1;height:0;border-top:2px solid currentColor;position:relative}
.divider .rule::after{content:"";position:absolute;left:0;right:0;top:2px;border-top:1px solid currentColor}
.div-mark{width:44px;flex:none}

/* flash-sheet grid */
.sheet{padding:10px 0 70px}
.sheet-title{text-align:center;font-family:"Rye",serif;font-weight:400;font-size:1.7rem;margin-bottom:8px}
.sheet-note{text-align:center;font-style:italic;color:var(--ink-soft);margin-bottom:34px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:30px}
.card{
  position:relative;text-decoration:none;color:var(--ink);background:var(--paper-deep);
  border:var(--frame);box-shadow:0 0 0 1px var(--paper),0 0 0 2px var(--ink),6px 7px 0 rgba(36,27,18,.28);
  padding:12px;display:flex;flex-direction:column;
}
.card:hover{background:#e3d4ab}
.card:hover .card-name{color:var(--oxblood)}
.card .ph{border:2px solid var(--ink);overflow:hidden;aspect-ratio:4/5;background:var(--paper-dark)}
.card .ph img{width:100%;height:100%;object-fit:cover;filter:sepia(.35) saturate(.75) contrast(1.05)}
.card-region{margin-top:12px;font-family:"IM Fell English SC",serif;font-size:.98rem;color:var(--indigo);letter-spacing:.1em}
.card-name{font-family:"Rye",serif;font-size:1.45rem;line-height:1.15;margin:2px 0 6px}
.card-blurb{font-size:.98rem;font-style:italic;color:var(--ink-soft);line-height:1.45}
.card .corner{position:absolute;width:9px;height:9px;background:var(--oxblood);transform:rotate(45deg)}
.card .c1{top:-5px;left:-5px}.card .c2{top:-5px;right:-5px}.card .c3{bottom:-5px;left:-5px}.card .c4{bottom:-5px;right:-5px}
.grid .card:nth-child(even){transform:rotate(.6deg)}
.grid .card:nth-child(3n){transform:rotate(-.7deg)}
.grid .card:hover{transform:rotate(0)}

/* photo frieze under the hero */
.frieze{display:flex;justify-content:center;align-items:center;gap:0;padding:18px 10px 8px;overflow:hidden}
.frieze .shot{flex:0 1 150px;min-width:0;background:var(--paper-deep);border:3px solid var(--ink);padding:7px;
  box-shadow:0 0 0 1px var(--paper),0 0 0 2px var(--ink),5px 6px 0 rgba(36,27,18,.3)}
.frieze .shot img{width:100%;aspect-ratio:3/4;object-fit:cover;border:2px solid var(--ink);
  filter:sepia(.4) saturate(.7) contrast(1.05)}
.frieze .shot:nth-child(1){transform:rotate(-3deg) translateY(8px)}
.frieze .shot:nth-child(2){transform:rotate(2deg)}
.frieze .shot:nth-child(3){transform:rotate(-1.5deg) translateY(-6px);flex-basis:170px}
.frieze .shot:nth-child(4){transform:rotate(1deg) translateY(6px)}
.frieze .shot:nth-child(5){transform:rotate(3deg)}
.frieze .shot:nth-child(6){transform:rotate(-2deg) translateY(10px)}
.frieze .shot:nth-child(7){transform:rotate(1.8deg) translateY(-4px)}
@media(max-width:860px){.frieze .shot:nth-child(n+5){display:none}}
@media(max-width:560px){.frieze .shot:nth-child(n+4){display:none}}

/* style page */
.poster{border-bottom:var(--frame);text-align:center;padding:46px 20px 30px}
.poster .region{font-family:"IM Fell English SC",serif;color:var(--indigo);font-size:1.15rem;letter-spacing:.14em}
.poster h1{font-family:"Rye",serif;font-weight:400;font-size:clamp(2.2rem,7vw,4.2rem);margin:.1em 0;text-shadow:2px 2px 0 var(--paper-dark)}
.poster .native{font-style:italic;color:var(--oxblood);font-size:1.15rem}
.lede{max-width:56ch;margin:26px auto 0;font-size:1.3rem;font-style:italic;line-height:1.55;color:var(--ink-soft)}

.article{display:grid;grid-template-columns:minmax(0,65ch) 240px;gap:48px;justify-content:center;padding:44px 0 10px}
@media(max-width:900px){.article{grid-template-columns:minmax(0,65ch);justify-content:center}}
.article .body p{margin-bottom:1.2em}
.article .body p:first-of-type::first-letter{
  font-family:"Rye",serif;font-size:3.1em;float:left;line-height:.82;padding:.06em .12em 0 0;color:var(--oxblood);
}
aside.notes{border:var(--frame);background:var(--paper-deep);padding:18px;height:fit-content;
  box-shadow:4px 5px 0 rgba(36,27,18,.25)}
aside.notes h2{font-family:"Rye",serif;font-weight:400;font-size:1.15rem;margin-bottom:12px;color:var(--oxblood)}
aside.notes dl{font-size:.98rem}
aside.notes dt{font-family:"IM Fell English SC",serif;color:var(--indigo);margin-top:10px}
aside.notes dd{margin:0}
.motifs{margin-top:16px;border-top:2px solid var(--ink);padding-top:12px}
.motifs h2{font-family:"Rye",serif;font-weight:400;font-size:1.15rem;color:var(--oxblood);margin-bottom:8px}
.motifs ul{list-style:none;display:flex;flex-wrap:wrap;gap:6px}
.motifs li{border:1.5px solid var(--ink-soft);padding:1px 9px;font-size:.9rem;font-style:italic;background:var(--paper)}

/* gallery — masonry of pinned plates */
.gallery{padding:26px 0 56px}
.gallery h2{text-align:center;font-family:"Rye",serif;font-weight:400;font-size:1.6rem;margin-bottom:6px}
.gallery .count{text-align:center;font-style:italic;color:var(--ink-soft);margin-bottom:30px}
.plates{columns:3 300px;column-gap:34px}
figure.plate{width:100%;margin:0 0 34px;break-inside:avoid;background:var(--paper-deep);border:var(--frame);padding:12px;
  box-shadow:0 0 0 1px var(--paper),0 0 0 2px var(--ink),6px 7px 0 rgba(36,27,18,.28)}
figure.plate:nth-child(3n+1){transform:rotate(-1deg)}
figure.plate:nth-child(3n+2){transform:rotate(.7deg)}
figure.plate:nth-child(5n){transform:rotate(1.3deg)}
figure.plate::before{content:"";display:block;width:12px;height:12px;border-radius:50%;
  background:var(--oxblood);box-shadow:inset -2px -2px 2px rgba(0,0,0,.35);margin:-4px auto 8px}
/* lead plate on style pages */
.lead-plate{display:flex;justify-content:center;padding:36px 20px 0}
.lead-plate figure.plate{width:min(560px,100%);margin:0;transform:rotate(-.6deg)}
.lead-plate figure.plate img{max-height:72vh;object-fit:cover;width:100%}
figure.plate img{border:2px solid var(--ink);width:100%;height:auto;filter:sepia(.3) saturate(.8) contrast(1.04);background:var(--paper-dark)}
figure.plate figcaption{margin-top:10px;font-size:.92rem;line-height:1.45}
figure.plate .credit{display:block;margin-top:6px;font-family:"IM Fell English SC",serif;font-size:.85rem;color:var(--ink-soft)}

/* prev-next */
.voyage{border-top:var(--frame);display:flex;justify-content:space-between;gap:16px;padding:22px 0 60px;flex-wrap:wrap}
.voyage a{text-decoration:none;font-family:"IM Fell English SC",serif;font-size:1.1rem}
.voyage .dest{display:block;font-family:"Rye",serif;font-size:1.3rem;color:var(--ink)}
.voyage a:hover .dest{color:var(--oxblood)}

/* about page */
.credits{max-width:65ch;margin:0 auto;padding:40px 0 60px}
.credits h2{font-family:"Rye",serif;font-weight:400;font-size:1.5rem;margin:30px 0 12px;color:var(--oxblood)}
.credits p{margin-bottom:1em}
.credits ul{margin:0 0 1em 1.2em}
.credits li{margin-bottom:.5em}

/* footer */
footer{border-top:var(--frame);background:rgba(221,204,158,.6)}
footer .wrap{padding:26px 20px;text-align:center;font-size:.95rem;color:var(--ink-soft)}
footer .foot-brand{font-family:"Rye",serif;color:var(--ink);font-size:1.05rem}
"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rye&family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/style.css?v={v}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23e8dbba'/%3E%3Cpath d='M16 4 L19 13 L28 16 L19 19 L16 28 L13 19 L4 16 L13 13 Z' fill='%238c2f26'/%3E%3C/svg%3E">
</head>
<body>
"""


def masthead(root: str, active: str = "") -> str:
    return f"""<header class="masthead"><div class="wrap">
<a class="brand" href="{root}index.html">Tattoo of the World</a>
<nav class="crumbs" aria-label="Site">
<a href="{root}index.html#sheet">The flash sheet</a>
<a href="{root}about.html">About &amp; credits</a>
<a href="https://github.com/DmitryLeLeE/tattooftheworld">GitHub</a>
</nav></div></header>"""


def footer(root: str) -> str:
    return f"""<footer><div class="wrap">
<span class="foot-brand">Tattoo of the World</span><br>
An illustrated atlas of tattoo traditions. Photographs via
<a href="https://commons.wikimedia.org/">Wikimedia Commons</a> — see
<a href="{root}about.html">credits &amp; licences</a>.
</div></footer></body></html>"""


def fig(img: dict, width: int = 760) -> str:
    cap = img["caption"]
    return f"""<figure class="plate">
<a href="{commons_page(img['file'])}"><img src="{commons(img['file'], width)}" alt="{html.escape(cap)}" loading="lazy"></a>
<figcaption>{cap}
<span class="credit"><a href="{commons_page(img['file'])}">{img['credit']}</a></span></figcaption>
</figure>"""


def build_index() -> str:
    cards = []
    for s in STYLES:
        hero = s["images"][0]
        cards.append(f"""<a class="card" href="styles/{s['slug']}.html">
<span class="corner c1"></span><span class="corner c2"></span><span class="corner c3"></span><span class="corner c4"></span>
<span class="ph"><img src="{commons(hero['file'], 480)}" alt="{html.escape(hero['caption'])}" loading="lazy"></span>
<span class="card-region">{s['region']}</span>
<span class="card-name">{s['name']}</span>
<span class="card-blurb">{s['card']}</span>
</a>""")
    total = sum(len(s["images"]) for s in STYLES)
    frieze_picks = []
    for s in STYLES:
        if len(s["images"]) > 1:
            frieze_picks.append(s["images"][1])
    frieze = "".join(
        f'<span class="shot"><img src="{commons(img["file"], 360)}" alt="" loading="lazy"></span>'
        for img in frieze_picks[:7])
    page = HEAD.format(title=SITE, root="", v=VERSION,
                       desc="An illustrated atlas of the world's tattoo traditions — from Japanese irezumi to Samoan tatau.")
    page += masthead("")
    page += f"""<section class="hero">
{SWALLOW_L}{SWALLOW_R}
<p class="over">An illustrated atlas of ink on skin</p>
<h1>Tattoo<span class="of">— of the —</span>World</h1>
<p class="sub">Ten living traditions, from the hand-carved moko of Aotearoa to the
flash sheets of American ports — their tools, their meanings, and the people who keep them.</p>
<span class="est">Ink on skin since c. 3300 BC</span>
</section>
<div class="frieze" aria-hidden="true">
{frieze}
</div>
{DIVIDER}
<section class="sheet wrap" id="sheet">
<h2 class="sheet-title">The Flash Sheet</h2>
<p class="sheet-note">Ten traditions, {total} plates from the archive — pick a design off the wall, every one opens into its own story.</p>
<div class="grid">
{''.join(cards)}
</div>
</section>
"""
    page += footer("")
    return page


def build_style(i: int, s: dict) -> str:
    prev_s = STYLES[(i - 1) % len(STYLES)]
    next_s = STYLES[(i + 1) % len(STYLES)]
    facts = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in s["facts"])
    motifs = "".join(f"<li>{m}</li>" for m in s["motifs"])
    body = "".join(f"<p>{p}</p>" for p in s["paragraphs"])
    lead = fig(s["images"][0], 1100)
    rest = s["images"][1:] if len(s["images"]) > 1 else s["images"]
    plates = "".join(fig(img) for img in rest)
    n_plates = len(s["images"])
    page = HEAD.format(title=f"{s['name']} — {s['region']} · {SITE}", root="../", v=VERSION,
                       desc=html.escape(s["card"]))
    page += masthead("../")
    page += f"""<section class="poster">
<p class="region">{s['region']}</p>
<h1>{s['name']}</h1>
<p class="native">{s['native']}</p>
<p class="lede">{s['lede']}</p>
</section>
<div class="lead-plate wrap">{lead}</div>
<div class="wrap">
<div class="article">
<div class="body">{body}</div>
<aside class="notes">
<h2>Field notes</h2>
<dl>{facts}</dl>
<div class="motifs"><h2>Classic motifs</h2><ul>{motifs}</ul></div>
</aside>
</div>
</div>
{DIVIDER}
<section class="gallery wrap">
<h2>Plates</h2>
<p class="count">{n_plates} plates in this folder — each links to its source and licence.</p>
<div class="plates">{plates}</div>
</section>
<div class="wrap">
<nav class="voyage" aria-label="Previous and next tradition">
<a href="{prev_s['slug']}.html">Previous stop<span class="dest">{prev_s['name']} · {prev_s['region']}</span></a>
<a href="{next_s['slug']}.html" style="text-align:right">Next stop<span class="dest">{next_s['name']} · {next_s['region']}</span></a>
</nav>
</div>
"""
    page += footer("../")
    return page


def build_about() -> str:
    img_items = []
    for s in STYLES:
        for img in s["images"]:
            img_items.append(
                f"<li><a href=\"{commons_page(img['file'])}\">{img['file']}</a> — {img['credit']} "
                f"(used on <a href=\"styles/{s['slug']}.html\">{s['name']}</a>)</li>")
    page = HEAD.format(title=f"About & credits · {SITE}", root="", v=VERSION,
                       desc="About the project, image credits and licences.")
    page += masthead("")
    page += f"""<section class="poster">
<p class="region">The project</p>
<h1>About &amp; Credits</h1>
<p class="lede">Tattoo of the World is an open, illustrated atlas of tattoo traditions —
a reading room for the oldest art form people carry on themselves.</p>
</section>
<div class="credits wrap">
<h2>The project</h2>
<p>Humans have tattooed each other for more than five thousand years: the oldest
preserved tattoos belong to Ötzi the Iceman (c. 3250 BC) and to the Gebelein
mummies of predynastic Egypt. This site collects ten traditions — their tools,
meanings and keepers — as short illustrated essays. It is a static site,
hand-built and hosted on GitHub Pages.</p>
<h2>Images</h2>
<p>All photographs and artworks are served from
<a href="https://commons.wikimedia.org/">Wikimedia Commons</a> and are in the
public domain or under Creative Commons licences. Every plate links to its
Commons file page, where the full licence and author information live.
If you reuse an image from these pages, follow the licence stated there.</p>
<ul>
{''.join(img_items)}
</ul>
<h2>A note on respect</h2>
<p>Several traditions here — tā moko above all — are living cultural property,
not a style menu. Where a tradition distinguishes between its own marks and
art made for outsiders, that distinction is noted in the essay. Read first,
ink later.</p>
<h2>Colophon</h2>
<p>Type set in <em>Rye</em> and <em>IM Fell English</em> (Google Fonts, the
Fell Types digitally reproduced by Igino Marini). No frameworks, no tracking —
plain HTML and CSS. Source on
<a href="https://github.com/DmitryLeLeE/tattooftheworld">GitHub</a>.</p>
</div>
"""
    page += footer("")
    return page


def main() -> None:
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "styles").mkdir(exist_ok=True)
    (ROOT / "assets" / "style.css").write_text(CSS, encoding="utf-8")
    (ROOT / "index.html").write_text(build_index(), encoding="utf-8")
    (ROOT / "about.html").write_text(build_about(), encoding="utf-8")
    for i, s in enumerate(STYLES):
        (ROOT / "styles" / f"{s['slug']}.html").write_text(build_style(i, s), encoding="utf-8")
    print(f"Built index.html, about.html and {len(STYLES)} style pages.")


if __name__ == "__main__":
    main()
