# Pracownia Pięknej Przestrzeni

Responsywna, wielostronicowa strona internetowa pracowni projektowania wnętrz Magdaleny Miszczyszyn.

**Wersja produkcyjna:** https://ppp-miszczyszyn.pl

![Podgląd strony Pracowni Pięknej Przestrzeni](https://ppp-miszczyszyn.pl/assets/og-cover.jpg)

## O projekcie

Strona prezentuje ofertę, proces współpracy, portfolio realizacji oraz dane kontaktowe Pracowni Pięknej Przestrzeni. Projekt został przygotowany jako lekka strona statyczna, bez frameworków i bez procesu budowania.

Portfolio zostało podzielone na stronę zbiorczą oraz osobne podstrony projektów. Dzięki temu użytkownik może przejść bezpośrednio do wybranej realizacji bez przewijania jednej bardzo długiej strony.

Najważniejsze założenia:

- szybkie ładowanie i dobra wydajność na telefonach oraz komputerach,
- spokojna, elegancka identyfikacja wizualna,
- czytelna prezentacja usług i realizacji,
- pełna responsywność,
- dostępność i poprawna semantyka HTML,
- przygotowanie pod SEO lokalne dla Szczecina i współpracy online.

## Funkcje

- responsywna nawigacja z mobilnym menu,
- ukrywanie i pokazywanie nagłówka podczas przewijania,
- subtelne animacje wejścia elementów,
- przycisk „Wróć na górę” omijający stopkę,
- osobne podstrony dla każdej realizacji,
- galerie projektów z pełnoekranowym podglądem zdjęć,
- obsługa gestów przesuwania zdjęć na urządzeniach dotykowych,
- nawigacja pomiędzy realizacjami,
- formularz kontaktowy obsługiwany przez Formspree,
- FAQ,
- polityka prywatności,
- Open Graph i Twitter Cards,
- dane strukturalne JSON-LD,
- `sitemap.xml` i `robots.txt`,
- własna domena i HTTPS,
- automatyczne wdrażanie przez GitHub Actions.

## Technologie

- HTML5
- CSS3
- JavaScript
- GitHub Pages
- GitHub Actions
- Formspree

Projekt nie wymaga Node.js, bundlera ani frameworka do działania.

## Podstrony

### Główne strony

| Plik | Zawartość |
|---|---|
| `index.html` | Strona główna |
| `o-mnie.html` | Informacje o projektantce i pracowni |
| `oferta.html` | Usługi i zakresy współpracy |
| `realizacje.html` | Indeks wszystkich realizacji |
| `proces.html` | Etapy współpracy |
| `kontakt.html` | Dane kontaktowe i formularz |
| `faq.html` | Najczęściej zadawane pytania |
| `polityka-prywatnosci.html` | Informacje dotyczące przetwarzania danych |

### Osobne strony realizacji

| Plik | Projekt |
|---|---|
| `realizacja-dla-niego.html` | Dla niego |
| `realizacja-dla-pary.html` | Dla pary |
| `realizacja-pokoj-goscinny.html` | Pokój gościnny |
| `realizacja-mini-kawalerka.html` | Mini kawalerka |
| `realizacja-sypialnia-w-trzech-odslonach.html` | Sypialnia w trzech odsłonach |

## Struktura repozytorium

```text
.
├── .github/
│   └── workflows/
│       └── static.yml
├── assets/
│   ├── realizacje/
│   │   ├── DlaNiego/
│   │   ├── DlaPary/
│   │   ├── MiniKawalerka/
│   │   ├── PokojGoscinny/
│   │   └── SypialniaW3Odslonach/
│   ├── favicon.png
│   └── og-cover.jpg
├── index.html
├── o-mnie.html
├── oferta.html
├── realizacje.html
├── realizacja-dla-niego.html
├── realizacja-dla-pary.html
├── realizacja-pokoj-goscinny.html
├── realizacja-mini-kawalerka.html
├── realizacja-sypialnia-w-trzech-odslonach.html
├── proces.html
├── kontakt.html
├── faq.html
├── polityka-prywatnosci.html
├── styles.css
├── script.js
├── robots.txt
├── sitemap.xml
├── CNAME
└── README.md
```

Pliki HTML pozostają w katalogu głównym celowo. Dzięki temu adresy podstron są krótkie, a konfiguracja GitHub Pages pozostaje prosta.

## Realizacje

Strona `realizacje.html` pełni funkcję katalogu projektów. Każda karta prowadzi do osobnej podstrony, na której znajdują się:

- opis projektu,
- najważniejsze założenia,
- szczegóły funkcjonalne,
- galeria zdjęć i wizualizacji,
- rzut projektu,
- nawigacja do pozostałych realizacji.

Zdjęcia pełnej rozdzielczości oraz miniatury znajdują się w:

```text
assets/realizacje/<NazwaProjektu>/
```

Przy dodawaniu nowego zdjęcia należy przygotować:

```text
nazwa.webp
nazwa-thumb.webp
```

Pełny obraz jest używany w podglądzie galerii, a wersja `-thumb.webp` jako lekka miniatura na stronie.

## Uruchomienie lokalne

W katalogu projektu uruchom prosty serwer:

```bash
python3 -m http.server 8000
```

Następnie otwórz:

```text
http://localhost:8000
```

Zatrzymanie serwera:

```text
Ctrl + C
```

## Formatowanie kodu

Repozytorium zawiera konfigurację Prettier. Aby sformatować pliki:

```bash
npx --yes prettier@3.9.5 --write "*.html" "styles.css" "script.js" ".github/workflows/*.yml" "*.json" "*.md"
```

Kontrola bez zapisywania zmian:

```bash
npx --yes prettier@3.9.5 --check "*.html" "styles.css" "script.js" ".github/workflows/*.yml" "*.json" "*.md"
```

Po formatowaniu zawsze sprawdź stronę lokalnie oraz przejrzyj zmiany:

```bash
git diff
```

## Publikacja

Zmiany wysłane do gałęzi `main` uruchamiają workflow GitHub Actions i publikują stronę w GitHub Pages.

```bash
git add .
git commit -m "Opis zmian"
git push origin main
```

Status wdrożenia można sprawdzić w zakładce **Actions** repozytorium.

## Formularz kontaktowy

Formularz na stronie `kontakt.html` korzysta z Formspree. Przy zmianie formularza należy zachować:

- poprawny adres endpointu,
- wymagane pola,
- zabezpieczenie typu honeypot,
- informację o polityce prywatności.

## SEO i utrzymanie

Przy dodawaniu lub usuwaniu podstron należy zaktualizować:

1. nawigację i stopkę,
2. `sitemap.xml`,
3. adres kanoniczny strony,
4. metadane Open Graph,
5. wewnętrzne odnośniki,
6. dane strukturalne, jeżeli dotyczą nowej treści.

Przy dodawaniu nowej realizacji należy również:

1. utworzyć osobny plik HTML,
2. dodać kartę w `realizacje.html`,
3. zaktualizować nawigację poprzednia/następna realizacja,
4. dodać adres podstrony do `sitemap.xml`,
5. dodać zoptymalizowane pliki `.webp` i `-thumb.webp`,
6. uzupełnić opisy `alt` i podpisy galerii.

Po zmianie `styles.css` lub `script.js` warto zaktualizować parametr wersji w plikach HTML, aby przeglądarki pobrały nową wersję plików.

## Najważniejsze adresy

- Strona: https://ppp-miszczyszyn.pl
- Instagram: https://www.instagram.com/ppp.magda.miszczyszyn/
- E-mail: pracownia.miszczyszyn@gmail.com
- Telefon: +48 509 850 497

## Status

Strona jest wdrożona produkcyjnie i aktywnie utrzymywana.

Aktualna stabilna wersja: **v1.0.0**.

## Prawa do materiałów

Zdjęcia, wizualizacje, teksty oraz identyfikacja wizualna należą do Pracowni Pięknej Przestrzeni. Repozytorium nie zawiera licencji open-source zezwalającej na ich swobodne ponowne wykorzystanie.
