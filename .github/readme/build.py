#!/usr/bin/env python3
"""Regenerate the README Islamic-themed art: the Islamic Star Banner and Academic Lab Dossier Card.

Generates banner-dark.svg, banner-light.svg, card-dark.svg, and card-light.svg.
Embraces an Islamic aesthetic: Emerald & Gold palettes, 8-fold geometric star motifs (Rub el Hizb),
Bismillah calligraphy, Quranic invocation on knowledge (Rabbi Zidni 'Ilma),
and personalized candidate credentials for Muhammad Khaidhir bin Mohd Razin (Student ID: 22007399).
Standard library only.
"""
import math
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).parent

# ------------------------------------------------------------------ Configuration
NAME = "ML-LAB · مُخْتَبَرُ تَعَلُّمِ الآلَة"
STUDENT_NAME = "Muhammad Khaidhir bin Mohd Razin"
STUDENT_ID = "22007399"
INSTITUTION = "Universiti Teknologi PETRONAS (UTP)"
COURSE = "TEB3123 Machine Learning"
EVALUATOR = "Reeyan Afzal"

THEMES = {
    "dark": {
        "bg_start": "#03150f",
        "bg_mid": "#072b1f",
        "bg_end": "#02110c",
        "card_bg": "#041912",
        "card_inner": "#06241a",
        "border": "#b45309",
        "gold_start": "#fde68a",
        "gold_mid": "#f59e0b",
        "gold_end": "#b45309",
        "emerald_start": "#a7f3d0",
        "emerald_mid": "#10b981",
        "emerald_end": "#047857",
        "fg": "#e2e8f0",
        "muted": "#94a3b8",
        "gold": "#fbbf24",
        "emerald": "#34d399",
        "cell_done": "#10b981",
        "cell_next": "#f59e0b",
        "cell_pending": "#1e3a2f",
    },
    "light": {
        "bg_start": "#faf8f2",
        "bg_mid": "#f0f7f3",
        "bg_end": "#f8f5ee",
        "card_bg": "#ffffff",
        "card_inner": "#f4f9f6",
        "border": "#d97706",
        "gold_start": "#b45309",
        "gold_mid": "#d97706",
        "gold_end": "#78350f",
        "emerald_start": "#065f46",
        "emerald_mid": "#047857",
        "emerald_end": "#064e3b",
        "fg": "#1e293b",
        "muted": "#64748b",
        "gold": "#b45309",
        "emerald": "#065f46",
        "cell_done": "#059669",
        "cell_next": "#d97706",
        "cell_pending": "#e2e8f0",
    },
}

FONT_FAMILY = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
MONO_FAMILY = "ui-monospace, 'SFMono-Regular', Menlo, Monaco, Consolas, monospace"
ARABIC_FAMILY = "'Amiri', 'Scheherazade New', 'Traditional Arabic', 'Noto Naskh Arabic', serif"


def get_common_defs(t, theme_name):
    return f"""
    <linearGradient id="bgGrad_{theme_name}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['bg_start']}"/>
      <stop offset="50%" stop-color="{t['bg_mid']}"/>
      <stop offset="100%" stop-color="{t['bg_end']}"/>
    </linearGradient>
    <linearGradient id="goldRamp_{theme_name}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['gold_start']}"/>
      <stop offset="50%" stop-color="{t['gold_mid']}"/>
      <stop offset="100%" stop-color="{t['gold_end']}"/>
    </linearGradient>
    <linearGradient id="emeraldRamp_{theme_name}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{t['emerald_start']}"/>
      <stop offset="50%" stop-color="{t['emerald_mid']}"/>
      <stop offset="100%" stop-color="{t['emerald_end']}"/>
    </linearGradient>
    <filter id="softGlow_{theme_name}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    """


# ------------------------------------------------------------------ Banner
def build_banner(theme_name):
    t = THEMES[theme_name]
    w, h = 850, 154
    defs = get_common_defs(t, theme_name)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="ML-LAB Islamic Academic Banner">
  <defs>
    {defs}
  </defs>

  <!-- Outer Background Container -->
  <rect x="2" y="2" width="{w - 4}" height="{h - 4}" rx="14" fill="url(#bgGrad_{theme_name})" stroke="{t['border']}" stroke-width="1.6" stroke-opacity="0.85"/>

  <!-- Inner Decorative Border -->
  <rect x="8" y="8" width="{w - 16}" height="{h - 16}" rx="10" fill="none" stroke="url(#goldRamp_{theme_name})" stroke-width="0.8" stroke-dasharray="8,5" opacity="0.6"/>

  <!-- Islamic Corner Stars (Rub el Hizb 8-point motif) -->
  <g fill="url(#goldRamp_{theme_name})" opacity="0.85">
    <!-- Top-Left -->
    <path d="M 22 17 L 24 20 L 27 22 L 24 24 L 22 27 L 20 24 L 17 22 L 20 20 Z"/>
    <!-- Top-Right -->
    <path d="M 828 17 L 830 20 L 833 22 L 830 24 L 828 27 L 826 24 L 823 22 L 826 20 Z"/>
    <!-- Bottom-Left -->
    <path d="M 22 127 L 24 130 L 27 132 L 24 134 L 22 137 L 20 134 L 17 132 L 20 130 Z"/>
    <!-- Bottom-Right -->
    <path d="M 828 127 L 830 130 L 833 132 L 830 134 L 828 137 L 826 134 L 823 132 L 826 130 Z"/>
  </g>

  <!-- Calligraphy: Bismillah Ar-Rahman Ar-Rahim -->
  <text x="{w // 2}" y="36" font-family="{ARABIC_FAMILY}" font-size="22" font-weight="bold" fill="url(#goldRamp_{theme_name})" text-anchor="middle" letter-spacing="1">
    بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
  </text>

  <!-- Title: ML-LAB with Rub el Hizb and Arabic Translation -->
  <text x="{w // 2}" y="76" font-family="{FONT_FAMILY}" font-size="23" font-weight="800" fill="url(#emeraldRamp_{theme_name})" text-anchor="middle" letter-spacing="3.5">
    ML · LAB  <tspan fill="url(#goldRamp_{theme_name})" font-family="{ARABIC_FAMILY}" font-size="20">۞</tspan>  مُخْتَبَرُ تَعَلُّمِ الآلَة
  </text>

  <!-- Subtitle: University and Course Code -->
  <text x="{w // 2}" y="104" font-family="{MONO_FAMILY}" font-size="11.5" font-weight="600" fill="{t['muted']}" text-anchor="middle" letter-spacing="2">
    TEB3123 MACHINE LEARNING · UNIVERSITI TEKNOLOGI PETRONAS
  </text>

  <!-- Student Line with Student ID prominently featured -->
  <g text-anchor="middle" font-family="{MONO_FAMILY}">
    <text x="{w // 2}" y="128" font-size="11.5" font-weight="600" fill="url(#goldRamp_{theme_name})" letter-spacing="1.2">
      CANDIDATE: {STUDENT_NAME.upper()}  ·  STUDENT ID: {STUDENT_ID}
    </text>
  </g>
</svg>"""


# ------------------------------------------------------------------ Islamic Star Rosette Geometry
def build_rosette(cx, cy, base_r, theme_name):
    t = THEMES[theme_name]
    elements = []

    # 1. Outer celestial orbital ring
    elements.append(
        f'<circle cx="{cx}" cy="{cy}" r="{base_r * 1.18:.1f}" fill="none" stroke="url(#goldRamp_{theme_name})" stroke-width="1" stroke-dasharray="4,6" opacity="0.45"/>'
    )

    # 2. Outer 16 planetary data points (Machine Learning feature space)
    for i in range(16):
        ang = i * math.pi / 8
        px = cx + base_r * 1.18 * math.cos(ang)
        py = cy + base_r * 1.18 * math.sin(ang)
        color = "url(#goldRamp_" + theme_name + ")" if i % 2 == 0 else "url(#emeraldRamp_" + theme_name + ")"
        elements.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2.8" fill="{color}" opacity="0.85"/>')

    # 3. Two rotated interlaced squares forming an octagram (Rub el Hizb)
    for rot in [0, 45]:
        rad = math.radians(rot)
        s = base_r * 0.96
        pts = []
        for j in range(4):
            a = rad + j * math.pi / 2
            pts.append(f"{cx + s * math.cos(a):.1f},{cy + s * math.sin(a):.1f}")
        elements.append(
            f'<polygon points="{" ".join(pts)}" fill="none" stroke="url(#emeraldRamp_{theme_name})" stroke-width="1.8" opacity="0.8"/>'
        )

    # 4. Primary 8-pointed Islamic Star
    pts8 = []
    for k in range(16):
        a = k * math.pi / 8 - math.pi / 2
        r = base_r * 0.84 if k % 2 == 0 else base_r * 0.52
        pts8.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    elements.append(
        f'<polygon points="{" ".join(pts8)}" fill="{t["card_inner"]}" stroke="url(#goldRamp_{theme_name})" stroke-width="2" opacity="0.95"/>'
    )

    # 5. Inner decorative 8-pointed star
    pts_in = []
    for k in range(16):
        a = k * math.pi / 8 - math.pi / 2 + math.pi / 16
        r = base_r * 0.46 if k % 2 == 0 else base_r * 0.28
        pts_in.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    elements.append(
        f'<polygon points="{" ".join(pts_in)}" fill="none" stroke="url(#goldRamp_{theme_name})" stroke-width="1.4" opacity="0.9"/>'
    )

    # 6. Center sanctuary node
    elements.append(
        f'<circle cx="{cx}" cy="{cy}" r="{base_r * 0.17:.1f}" fill="url(#emeraldRamp_{theme_name})" stroke="url(#goldRamp_{theme_name})" stroke-width="1.5"/>'
    )
    elements.append(
        f'<circle cx="{cx}" cy="{cy}" r="{base_r * 0.06:.1f}" fill="{t["gold"]}"/>'
    )

    return "\n    ".join(elements)


# ------------------------------------------------------------------ Academic Lab Card
def build_card(theme_name):
    t = THEMES[theme_name]
    w, h = 850, 360
    defs = get_common_defs(t, theme_name)
    rosette_svg = build_rosette(185, 180, 115, theme_name)

    card_label = (
        f"ML-LAB Academic Research Dossier - {STUDENT_NAME} (ID: {STUDENT_ID}), "
        f"Universiti Teknologi PETRONAS, TEB3123 Machine Learning."
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{escape(card_label)}">
  <defs>
    {defs}
  </defs>

  <!-- Outer Card Frame -->
  <rect x="2" y="2" width="{w - 4}" height="{h - 4}" rx="14" fill="url(#bgGrad_{theme_name})" stroke="{t['border']}" stroke-width="1.6" stroke-opacity="0.85"/>
  <rect x="8" y="8" width="{w - 16}" height="{h - 16}" rx="10" fill="none" stroke="url(#goldRamp_{theme_name})" stroke-width="0.75" stroke-dasharray="6,4" opacity="0.45"/>

  <!-- Left Side: Islamic Sacred Geometry & Pattern -->
  <g id="islamic_geometry">
    {rosette_svg}
    <text x="185" y="325" font-family="{ARABIC_FAMILY}" font-size="16" font-weight="bold" fill="url(#goldRamp_{theme_name})" text-anchor="middle">
      إِحْسَانٌ وَعِلْمٌ نَافِعٌ
    </text>
    <text x="185" y="342" font-family="{MONO_FAMILY}" font-size="9" fill="{t['muted']}" text-anchor="middle" letter-spacing="1.5">
      RIGOR · REPRODUCIBILITY · INTEGRITY
    </text>
  </g>

  <!-- Vertical Divider with Gold Accent -->
  <line x1="370" y1="28" x2="370" y2="332" stroke="url(#goldRamp_{theme_name})" stroke-width="1" stroke-dasharray="6,4" opacity="0.5"/>
  <polygon points="370,175 375,180 370,185 365,180" fill="url(#goldRamp_{theme_name})"/>

  <!-- Right Side: Academic Dossier & Experimental Status -->
  <!-- Header & Quranic Invocation -->
  <text x="400" y="46" font-family="{FONT_FAMILY}" font-size="13" font-weight="800" fill="url(#emeraldRamp_{theme_name})" letter-spacing="2">
    ✦ RESEARCH &amp; LABORATORY DOSSIER
  </text>
  <text x="400" y="70" font-family="{ARABIC_FAMILY}" font-size="17" font-weight="bold" fill="url(#goldRamp_{theme_name})">
    "رَّبِّ زِدْنِي عِلْمًا"
  </text>
  <text x="510" y="69" font-family="{FONT_FAMILY}" font-size="11.5" font-style="italic" fill="{t['muted']}">
    — "My Lord, increase me in knowledge." (20:114)
  </text>

  <line x1="400" y1="84" x2="820" y2="84" stroke="{t['muted']}" stroke-opacity="0.3" stroke-width="1"/>

  <!-- Metadata Table Rows -->
  <g font-family="{MONO_FAMILY}" font-size="12">
    <!-- Candidate -->
    <text x="400" y="110">
      <tspan fill="url(#goldRamp_{theme_name})" font-weight="bold">CANDIDATE</tspan>
      <tspan x="515" fill="{t['fg']}" font-weight="600">{STUDENT_NAME}</tspan>
    </text>

    <!-- Student ID -->
    <text x="400" y="134">
      <tspan fill="url(#goldRamp_{theme_name})" font-weight="bold">STUDENT ID</tspan>
      <tspan x="515" fill="{t['emerald']}" font-weight="bold" letter-spacing="1">{STUDENT_ID}</tspan>
      <tspan x="620" fill="{t['muted']}" font-size="11">(UTP Computer Science)</tspan>
    </text>

    <!-- Course & GA -->
    <text x="400" y="158">
      <tspan fill="url(#goldRamp_{theme_name})" font-weight="bold">COURSE</tspan>
      <tspan x="515" fill="{t['fg']}">{COURSE}</tspan>
    </text>
    <text x="400" y="182">
      <tspan fill="url(#goldRamp_{theme_name})" font-weight="bold">EVALUATOR</tspan>
      <tspan x="515" fill="{t['fg']}">GA {EVALUATOR}</tspan>
      <tspan x="670" fill="{t['muted']}" font-size="10.5">· Lab Feedback Addressed</tspan>
    </text>

    <!-- Milestone Progress -->
    <text x="400" y="210">
      <tspan fill="url(#goldRamp_{theme_name})" font-weight="bold">MILESTONES</tspan>
      <tspan x="515" fill="{t['fg']}">4 of 8 Labs Completed</tspan>
    </text>

    <!-- Milestone Cells: 1, 2, 3, 4 Done (Green), 5 Next (Gold), 6-8 Pending -->
    <g transform="translate(685, 199)">
      <rect x="0" y="0" width="13" height="12" rx="2.5" fill="{t['cell_done']}"/>
      <rect x="16" y="0" width="13" height="12" rx="2.5" fill="{t['cell_done']}"/>
      <rect x="32" y="0" width="13" height="12" rx="2.5" fill="{t['cell_done']}"/>
      <rect x="48" y="0" width="13" height="12" rx="2.5" fill="{t['cell_done']}"/>
      <rect x="64" y="0" width="13" height="12" rx="2.5" fill="{t['cell_next']}"/>
      <rect x="80" y="0" width="13" height="12" rx="2.5" fill="{t['cell_pending']}"/>
      <rect x="96" y="0" width="13" height="12" rx="2.5" fill="{t['cell_pending']}"/>
      <rect x="112" y="0" width="13" height="12" rx="2.5" fill="{t['cell_pending']}"/>
    </g>

    <!-- Current & Next Focus -->
    <text x="400" y="234">
      <tspan fill="url(#goldRamp_{theme_name})" font-weight="bold">NEXT LAB</tspan>
      <tspan x="515" fill="{t['gold']}" font-weight="bold">Lab 05: Anomaly Detection &amp; Limited Labels</tspan>
    </text>

    <!-- Empirical Benchmark Records -->
    <text x="400" y="260">
      <tspan fill="url(#goldRamp_{theme_name})" font-weight="bold">BENCHMARKS</tspan>
      <tspan x="515" fill="{t['fg']}">Titanic: <tspan fill="{t['emerald']}">0.837</tspan> · SVM: <tspan fill="{t['emerald']}">0.997</tspan> · PCA: <tspan fill="{t['emerald']}">0.947</tspan></tspan>
    </text>
    <text x="515" y="278" font-size="11" fill="{t['muted']}">
      Mall Silhouette: 0.528 · Digit Compression: 64 → 29 components
    </text>
  </g>

  <!-- Bottom Verification Seal -->
  <line x1="400" y1="298" x2="820" y2="298" stroke="{t['muted']}" stroke-opacity="0.3" stroke-width="1"/>
  <g font-family="{MONO_FAMILY}" font-size="11">
    <rect x="400" y="309" width="112" height="20" rx="4" fill="{t['card_inner']}" stroke="url(#emeraldRamp_{theme_name})" stroke-width="1"/>
    <text x="456" y="323" fill="{t['emerald']}" font-weight="bold" text-anchor="middle">✓ VERIFIED</text>
    <text x="522" y="323" fill="{t['muted']}">Random Seed 42 Fixed · Zero Leakage Pipelines</text>
  </g>
</svg>"""


def main():
    print(f"Building Islamic-themed SVG banners and dossier cards for {STUDENT_NAME} ({STUDENT_ID})...")
    for theme in THEMES:
        banner_svg = build_banner(theme)
        card_svg = build_card(theme)

        # Write to standard names, v2 names, and semantic names to ensure cache-busting
        for suffix in ["", "-v2", "-islamic"]:
            banner_name = f"banner{suffix}-{theme}.svg" if suffix == "-islamic" else f"banner-{theme}{suffix}.svg"
            card_name = f"card{suffix}-{theme}.svg" if suffix == "-islamic" else f"card-{theme}{suffix}.svg"
            (ROOT / banner_name).write_text(banner_svg, encoding="utf-8", newline="\n")
            (ROOT / card_name).write_text(card_svg, encoding="utf-8", newline="\n")
            print(f"  ✓ Wrote {banner_name} & {card_name}")

    print("SVG Generation completed successfully!")


if __name__ == "__main__":
    main()
