#!/usr/bin/env python3
"""
Pakiet SEO dla ppp-miszczyszyn.pl

Uruchom w głównym folderze repozytorium:
    python3 zastosuj_seo.py

Skrypt:
- aktualizuje title i meta description,
- dodaje canonical, Open Graph i Twitter Cards,
- dodaje dane strukturalne firmy na stronie głównej,
- poprawia usunięcie FAQ z głównego navbara,
- dodaje FAQ do stopki, jeśli go brakuje,
- tworzy sitemap.xml i robots.txt.
"""

from __future__ import annotations

from pathlib import Path
import html as html_lib
import json
import re
import sys

DOMAIN = "https://ppp-miszczyszyn.pl"
OG_IMAGE = f"{DOMAIN}/assets/og-cover.jpg"

PAGE_CONFIG = {
  "index.html": {
    "title": "Projektowanie wnętrz Szczecin | Pracownia Pięknej Przestrzeni",
    "description": "Projektowanie i stylizacja wnętrz w Szczecinie i online. Funkcjonalne projekty, konsultacje i realistyczne wizualizacje 3D.",
    "path": "/",
    "og_title": "Pracownia Pięknej Przestrzeni | Projektowanie wnętrz Szczecin",
    "og_description": "Tworzę funkcjonalne, harmonijne i ponadczasowe wnętrza dopasowane do stylu życia klienta."
  },
  "o-mnie.html": {
    "title": "Magdalena Miszczyszyn – projektantka wnętrz | Szczecin",
    "description": "Poznaj Magdalenę Miszczyszyn i filozofię Pracowni Pięknej Przestrzeni: indywidualne, funkcjonalne i ponadczasowe wnętrza.",
    "path": "/o-mnie.html",
    "og_title": "O mnie | Pracownia Pięknej Przestrzeni",
    "og_description": "Poznaj Magdalenę Miszczyszyn — projektantkę wnętrz, która łączy estetykę z funkcjonalnością i codziennym komfortem."
  },
  "oferta.html": {
    "title": "Projektowanie i stylizacja wnętrz – oferta | Szczecin",
    "description": "Projektowanie wnętrz, stylizacja, konsultacje i wizualizacje 3D. Sprawdź zakres współpracy w Szczecinie i w formie online.",
    "path": "/oferta.html",
    "og_title": "Oferta projektowania wnętrz | Szczecin i online",
    "og_description": "Od konsultacji po kompletną koncepcję z wizualizacjami 3D. Poznaj zakresy współpracy Pracowni Pięknej Przestrzeni."
  },
  "realizacje.html": {
    "title": "Realizacje wnętrz | Pracownia Pięknej Przestrzeni",
    "description": "Zobacz realizacje mieszkań, kawalerek i pojedynczych pomieszczeń. Funkcjonalne układy, spokojna estetyka i wizualizacje 3D.",
    "path": "/realizacje.html",
    "og_title": "Realizacje | Pracownia Pięknej Przestrzeni",
    "og_description": "Portfolio wnętrz tworzonych dla konkretnych potrzeb, metraży i sposobów codziennego użytkowania."
  },
  "proces.html": {
    "title": "Proces współpracy – projektowanie wnętrz | Szczecin",
    "description": "Poznaj proces projektowania wnętrza: konsultacja, analiza, układ funkcjonalny, kierunek stylistyczny i wizualizacje 3D.",
    "path": "/proces.html",
    "og_title": "Proces współpracy | Pracownia Pięknej Przestrzeni",
    "og_description": "Spokojna i czytelna droga od pierwszej rozmowy do spójnej koncepcji wnętrza."
  },
  "kontakt.html": {
    "title": "Kontakt – projektowanie wnętrz Szczecin | PPP",
    "description": "Skontaktuj się z Pracownią Pięknej Przestrzeni. Opisz wnętrze, metraż i oczekiwany zakres projektu lub umów konsultację.",
    "path": "/kontakt.html",
    "og_title": "Kontakt | Pracownia Pięknej Przestrzeni",
    "og_description": "Opowiedz o swojej przestrzeni i sprawdź, jaki zakres współpracy będzie najlepiej dopasowany do Twoich potrzeb."
  },
  "faq.html": {
    "title": "FAQ – projektowanie wnętrz | Pracownia Pięknej Przestrzeni",
    "description": "Odpowiedzi na pytania o projektowanie wnętrz, współpracę online, pomiary, wizualizacje 3D, czas realizacji, wycenę i płatność.",
    "path": "/faq.html",
    "og_title": "FAQ | Pracownia Pięknej Przestrzeni",
    "og_description": "Najczęstsze pytania dotyczące współpracy, pomiarów, projektu, wizualizacji, wyceny i płatności."
  }
}
BUSINESS_SCHEMA = {
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "@id": "https://ppp-miszczyszyn.pl/#business",
  "name": "Pracownia Pięknej Przestrzeni",
  "alternateName": "PPP",
  "description": "Projektowanie i stylizacja wnętrz, konsultacje wnętrzarskie oraz realistyczne wizualizacje 3D w Szczecinie i online.",
  "url": "https://ppp-miszczyszyn.pl/",
  "logo": "https://ppp-miszczyszyn.pl/assets/favicon.svg",
  "image": "https://ppp-miszczyszyn.pl/assets/og-cover.jpg",
  "telephone": "+48509850497",
  "email": "pracownia.miszczyszyn@gmail.com",
  "founder": {
    "@type": "Person",
    "name": "Magdalena Miszczyszyn"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ul. Modrzewiowa 8",
    "addressLocality": "Mierzyn",
    "addressRegion": "zachodniopomorskie",
    "postalCode": "72-006",
    "addressCountry": "PL"
  },
  "areaServed": [
    {
      "@type": "City",
      "name": "Szczecin"
    },
    {
      "@type": "AdministrativeArea",
      "name": "województwo zachodniopomorskie"
    },
    {
      "@type": "Country",
      "name": "Polska"
    }
  ],
  "sameAs": [
    "https://www.instagram.com/ppp.magda.miszczyszyn"
  ],
  "priceRange": "Wycena indywidualna",
  "makesOffer": [
    {
      "@type": "Offer",
      "itemOffered": {
        "@type": "Service",
        "name": "Projektowanie wnętrz"
      }
    },
    {
      "@type": "Offer",
      "itemOffered": {
        "@type": "Service",
        "name": "Stylizacja wnętrz"
      }
    },
    {
      "@type": "Offer",
      "itemOffered": {
        "@type": "Service",
        "name": "Wizualizacje wnętrz 3D"
      }
    },
    {
      "@type": "Offer",
      "itemOffered": {
        "@type": "Service",
        "name": "Konsultacje wnętrzarskie"
      }
    }
  ]
}

SEO_START = "<!-- SEO START -->"
SEO_END = "<!-- SEO END -->"
SCHEMA_START = "<!-- BUSINESS JSON-LD START -->"
SCHEMA_END = "<!-- BUSINESS JSON-LD END -->"

FAQ_FOOTER_LINK = """
        <a
          class="footer-contact__item"
          href="faq.html"
          aria-label="Najczęściej zadawane pytania"
        >
          <span class="footer-contact__icon" aria-hidden="true">?</span>
          <span>FAQ</span>
        </a>
""".rstrip()


def clean_existing_seo(content: str) -> str:
    content = re.sub(
        rf"\s*{re.escape(SEO_START)}.*?{re.escape(SEO_END)}\s*",
        "\n",
        content,
        flags=re.DOTALL,
    )

    patterns = [
        r'\s*<meta\s+name=["\']description["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']robots["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']author["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']theme-color["\'][^>]*>\s*',
        r'\s*<meta\s+property=["\']og:[^"\']+["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']twitter:[^"\']+["\'][^>]*>\s*',
        r'\s*<link\s+rel=["\']canonical["\'][^>]*>\s*',
        r'\s*<link\s+rel=["\']alternate["\'][^>]*hreflang=["\']pl-PL["\'][^>]*>\s*',
    ]
    for pattern in patterns:
        content = re.sub(pattern, "\n", content, flags=re.IGNORECASE)
    return content


def seo_block(cfg: dict[str, str]) -> str:
    canonical = DOMAIN + cfg["path"]
    values = {
        "description": html_lib.escape(cfg["description"], quote=True),
        "canonical": html_lib.escape(canonical, quote=True),
        "og_title": html_lib.escape(cfg["og_title"], quote=True),
        "og_description": html_lib.escape(cfg["og_description"], quote=True),
    }
    return f"""
    {SEO_START}
    <meta name="description" content="{values['description']}" />
    <meta name="robots" content="index, follow, max-image-preview:large" />
    <meta name="author" content="Magdalena Miszczyszyn" />
    <meta name="theme-color" content="#fbf8f3" />

    <link rel="canonical" href="{values['canonical']}" />
    <link rel="alternate" hreflang="pl-PL" href="{values['canonical']}" />

    <meta property="og:locale" content="pl_PL" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Pracownia Pięknej Przestrzeni" />
    <meta property="og:title" content="{values['og_title']}" />
    <meta property="og:description" content="{values['og_description']}" />
    <meta property="og:url" content="{values['canonical']}" />
    <meta property="og:image" content="{OG_IMAGE}" />
    <meta property="og:image:secure_url" content="{OG_IMAGE}" />
    <meta property="og:image:type" content="image/jpeg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta
      property="og:image:alt"
      content="Jasne wnętrze zaprojektowane przez Pracownię Pięknej Przestrzeni"
    />

    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{values['og_title']}" />
    <meta name="twitter:description" content="{values['og_description']}" />
    <meta name="twitter:image" content="{OG_IMAGE}" />
    {SEO_END}
""".rstrip()


def update_title(content: str, title: str) -> str:
    escaped = html_lib.escape(title)
    replacement = f"<title>{escaped}</title>"
    updated, count = re.subn(
        r"<title>.*?</title>",
        replacement,
        content,
        count=1,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if count:
        return updated

    return content.replace("</head>", f"  {replacement}\n  </head>", 1)


def insert_before_head_end(content: str, block: str) -> str:
    if "</head>" not in content.lower():
        raise ValueError("Brak znacznika </head>.")
    return re.sub(
        r"</head>",
        block + "\n  </head>",
        content,
        count=1,
        flags=re.IGNORECASE,
    )


def update_business_schema(content: str, filename: str) -> str:
    content = re.sub(
        rf"\s*{re.escape(SCHEMA_START)}.*?{re.escape(SCHEMA_END)}\s*",
        "\n",
        content,
        flags=re.DOTALL,
    )
    if filename != "index.html":
        return content

    schema = json.dumps(BUSINESS_SCHEMA, ensure_ascii=False, indent=2)
    block = f"""
    {SCHEMA_START}
    <script type="application/ld+json">
{schema}
    </script>
    {SCHEMA_END}
""".rstrip()
    return insert_before_head_end(content, block)


def remove_faq_from_main_nav(content: str) -> str:
    nav_pattern = re.compile(
        r'(<nav\b[^>]*\bclass=(["\'])main-nav\2[^>]*>)(.*?)(</nav>)',
        flags=re.IGNORECASE | re.DOTALL,
    )
    faq_pattern = re.compile(
        r'\s*<a\b[^>]*\bhref=(["\'])faq\.html(?:#[^"\']*)?\1[^>]*>'
        r'\s*FAQ\s*</a>\s*',
        flags=re.IGNORECASE | re.DOTALL,
    )

    def replace_nav(match: re.Match[str]) -> str:
        opening, _, body, closing = match.groups()
        body = faq_pattern.sub("\n", body)
        return opening + body + closing

    return nav_pattern.sub(replace_nav, content)


def add_faq_to_footer(content: str, filename: str) -> str:
    footer_pattern = re.compile(
        r'(<div\b[^>]*\bclass=(["\'])footer-contact\2[^>]*>)(.*?)(</div>)',
        flags=re.IGNORECASE | re.DOTALL,
    )
    faq_pattern = re.compile(
        r'<a\b[^>]*\bhref=(["\'])faq\.html(?:#[^"\']*)?\1',
        flags=re.IGNORECASE,
    )

    def replace_footer(match: re.Match[str]) -> str:
        opening, _, body, closing = match.groups()
        if faq_pattern.search(body):
            return match.group(0)

        link = FAQ_FOOTER_LINK
        if filename == "faq.html":
            link = link.replace(
                'href="faq.html"',
                'href="faq.html" aria-current="page"',
                1,
            )
        return opening + body.rstrip() + "\n\n" + link + "\n      " + closing

    updated, _ = footer_pattern.subn(replace_footer, content, count=1)
    return updated


def process_page(path: Path, cfg: dict[str, str]) -> None:
    content = path.read_text(encoding="utf-8")
    content = clean_existing_seo(content)
    content = update_title(content, cfg["title"])
    content = insert_before_head_end(content, seo_block(cfg))
    content = update_business_schema(content, path.name)
    content = remove_faq_from_main_nav(content)
    content = add_faq_to_footer(content, path.name)
    path.write_text(content, encoding="utf-8")


def create_sitemap(root: Path) -> None:
    urls = [DOMAIN + PAGE_CONFIG[name]["path"] for name in PAGE_CONFIG]
    entries = "\n".join(
        f"""  <url>
    <loc>{html_lib.escape(url)}</loc>
    <lastmod>2026-07-18</lastmod>
  </url>"""
        for url in urls
    )
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""
    (root / "sitemap.xml").write_text(sitemap, encoding="utf-8")


def create_robots(root: Path) -> None:
    robots = """User-agent: *
Allow: /

Sitemap: https://ppp-miszczyszyn.pl/sitemap.xml
"""
    (root / "robots.txt").write_text(robots, encoding="utf-8")


def main() -> int:
    root = Path.cwd()

    if not (root / "styles.css").exists():
        print(
            "BŁĄD: uruchom skrypt w głównym folderze projektu, "
            "obok styles.css i index.html.",
            file=sys.stderr,
        )
        return 1

    missing = [name for name in PAGE_CONFIG if not (root / name).exists()]
    if missing:
        print("BŁĄD: brakuje plików: " + ", ".join(missing), file=sys.stderr)
        return 1

    for name, cfg in PAGE_CONFIG.items():
        process_page(root / name, cfg)
        print(f"Zaktualizowano: {name}")

    create_sitemap(root)
    create_robots(root)
    print("Utworzono: sitemap.xml")
    print("Utworzono: robots.txt")
    print("Gotowe.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
