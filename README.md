# SuiteForge — site web (landings + legal + écosystème)

Site statique unique pour `suiteforge.app`. Zéro dépendance externe, zéro CDN, fonts auto-hébergées (privacy-first : aucune requête vers Google quand un visiteur ouvre une page). Prêt pour GitHub Pages.

## Contenu

```
/index.html                  page parent SuiteForge (écosystème, 2 piliers, manifesto privacy, FAQ) — écrite à la main
/<app>/                      landing de l'app      + /privacy/ + /terms/   (générées par build.py)
/<app>/icon.webp             icône App Store (256 px)
/<app>/og.png                image de partage de l'app (1200 × 630)
/<app>/screenshots/          hero-home.webp + shot-N.webp, et source/ (PNG App Store d'origine, en/ et fr/)
/sitemap.xml  /robots.txt    SEO
/CNAME                       domaine custom (suiteforge.app)
/assets/styles.css           design system partagé
/assets/reveal.js            animation au scroll (progressive enhancement)
/assets/fonts/               Fraunces + Hanken Grotesk (woff2 auto-hébergés)
/assets/og-suiteforge.png    image de partage de la page d'accueil (les 4 icônes)

/build.py                    générateur des pages — source unique de vérité pour le contenu
/make_og.py                  génère les images de partage (<app>/og.png + assets/og-suiteforge.png)
/optimize_shots.py           PNG App Store → WebP du site (hero + carrousel)
/optimize_icons.py           icône 1024 de chaque projet Xcode → <app>/icon.webp
```

Apps : `fastclear`, `routineflow`, `walkquest`, `keepcontact` (App Store IDs réels dans `build.py`, champ `appstore_id`).

## Déploiement GitHub Pages

Le site est servi par GitHub Pages depuis `suiteforgeops/suiteforge-web`, branche `main`. Un `git push` suffit : la mise en ligne prend 1 à 2 minutes. Le push doit se faire avec le compte **`suiteforgeops`** (`gh auth status` pour vérifier, `gh auth login` + `gh auth setup-git` sinon).

Mise en place initiale (déjà faite, pour mémoire) :

1. Crée un repo (ex. `suiteforge-web`) et pousse tout le contenu de ce dossier à la racine.
2. Settings → Pages → Source : `Deploy from a branch`, branche `main`, dossier `/ (root)`.
3. Settings → Pages → Custom domain : `suiteforge.app` (le fichier `CNAME` est déjà présent).
4. Chez ton registrar (où tu achètes `suiteforge.app`), configure le DNS :
   - 4 enregistrements **A** sur l'apex `@` vers les IP GitHub Pages
   - 1 **AAAA** (IPv6) optionnel
   - 1 **CNAME** `www` vers `suiteforgeops.github.io`
   - Les IP exactes sont dans la doc GitHub (« Managing a custom domain ») — recopie-les de là, c'est la source qui fait foi.
5. Reviens dans Settings → Pages, coche **Enforce HTTPS** une fois le domaine vérifié (certificat Let's Encrypt auto, `.app` force le HTTPS de toute façon).

Propagation DNS : quelques minutes à quelques heures.

## Mettre à jour App Store Connect

Une fois en ligne, remplace les URLs Notion par celles-ci dans chaque fiche (App → General + App Privacy) :

| App | Privacy Policy URL | Terms / EULA URL |
|---|---|---|
| FastClear | `https://suiteforge.app/fastclear/privacy/` | `https://suiteforge.app/fastclear/terms/` |
| RoutineFlow | `https://suiteforge.app/routineflow/privacy/` | `https://suiteforge.app/routineflow/terms/` |
| WalkQuest | `https://suiteforge.app/walkquest/privacy/` | `https://suiteforge.app/walkquest/terms/` |
| KeepContact | `https://suiteforge.app/keepcontact/privacy/` | `https://suiteforge.app/keepcontact/terms/` |

Le champ Terms est facultatif côté Apple (un EULA standard s'applique sinon), mais pointer vers ta page est plus propre et cohérent avec le footer des landings.

## Modifier le contenu plus tard

Tout le texte vit dans `build.py` (dict `APPS`). Édite, puis :

```bash
python3 build.py        # régénère les 12 pages HTML + sitemap
```

Options par app dans `APPS` (facultatives) : `updated` (date « Last updated » des pages légales, sinon `UPDATED`), `icloud: False` (l'app ne synchronise pas via iCloud : la page Privacy le dit), `lifetime: True` (achat à vie mentionné dans Privacy et Terms).

`index.html` (page d'accueil) n'est **pas** généré : une modification d'app (couleur, phrase d'accroche) s'y reporte à la main.

## Nouvelle version d'une app : captures, icône, image de partage

1. Copier les nouvelles captures App Store (PNG, EN) dans `<app>/screenshots/source/en/`, archiver les anciennes. Ordre = ordre alphabétique des noms ; l'écran dont le nom contient `home` (ou `today`) devient le hero. Le carrousel prend les N premières sources moins le hero : N = 5 par défaut (soit 4 captures), réglable par app dans `MAX_COUNT` de `optimize_shots.py` (6 pour KeepContact, soit 5 captures).
2. Mettre à jour les textes `alt` des captures (`shots`, `hero_shot_alt`) dans `build.py`.
3. Lancer, dans cet ordre :

```bash
python3 optimize_shots.py   # captures → WebP (toutes les apps)
python3 optimize_icons.py   # icônes Xcode → icon.webp (toutes les apps)
python3 make_og.py          # images de partage (textes et couleurs dans OG / HOUSE)
python3 build.py            # pages HTML
```

Chaque URL d'image porte un `?v=<hash du fichier>` calculé par `build.py` : après un déploiement, navigateurs et réseaux sociaux chargent la nouvelle image sans attendre l'expiration du cache. Un aperçu déjà partagé peut se rafraîchir avec le Post Inspector de LinkedIn ou le Sharing Debugger de Facebook.

`make_og.py` utilise la police système SF Pro Rounded : il tourne sur un Mac.

Prévisualiser en local (les chemins sont absolus, donc il faut un serveur) :

```bash
python3 -m http.server 8000   # puis ouvre http://localhost:8000
```

## Ce que ces pages couvrent côté SEO / GEO

- **SEO** : `<title>`/meta par page, canonical, sitemap, et JSON-LD `SoftwareApplication` + `BreadcrumbList` sur chaque landing → Google comprend que c'est une app (catégorie, prix, éditeur).
- **GEO** : bloc FAQ + `FAQPage` structured data avec des réponses factuelles citables (« What's the best app for private intermittent fasting? ») → c'est la surface que ChatGPT/Claude/Perplexity récupèrent.
- **Privacy = argument marketing** : le « stays on your device / no tracking » est mis en avant partout, pas caché dans le legal.

## Note importante (legal)

Je ne suis pas avocat et ces pages Privacy/Terms sont des modèles solides et standards pour des apps freemium on-device, pas un avis juridique. Les points sensibles sont traités honnêtement (HealthKit, RevenueCat + Apple comme sous-traitants, RGPD/France, disclaimer santé sur les apps Health). Avant la mise en ligne, vérifie surtout deux choses :

1. **Les permissions listées par app** correspondent exactement à ce que l'app demande réellement (chaînes d'usage dans `Info.plist`). État actuel : FastClear = HealthKit *write-only* + notifications ; WalkQuest = HealthKit *read steps* + notifications ; RoutineFlow = notifications ; KeepContact (1.6.0, vérifié dans le code le 11/10/2026) = Contacts, calendrier, appareil photo, micro et notifications, tous optionnels, pas de synchro iCloud. À revérifier à chaque nouvelle permission dans une app.
2. Si tu veux une sécurité juridique renforcée (tu opères depuis une SARL FR), une relecture par un professionnel reste recommandée.
