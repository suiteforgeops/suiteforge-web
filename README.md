# SuiteForge — site web (landings + legal + écosystème)

Site statique unique pour `suiteforge.app`. Zéro dépendance externe, zéro CDN, fonts auto-hébergées (privacy-first : aucune requête vers Google quand un visiteur ouvre une page). Prêt pour GitHub Pages.

## Contenu

```
/index.html                  page parent SuiteForge (écosystème, 2 piliers, manifesto privacy, FAQ)
/fastclear/                  landing FastClear      + /privacy/ + /terms/
/routineflow/                landing RoutineFlow    + /privacy/ + /terms/
/walkquest/                  landing WalkQuest      + /privacy/ + /terms/
/keepcontact/                landing KeepContact    + /privacy/ + /terms/
/sitemap.xml  /robots.txt    SEO
/CNAME                       domaine custom (suiteforge.app)
/assets/styles.css           design system partagé
/assets/reveal.js            animation au scroll (progressive enhancement)
/assets/fonts/               Fraunces + Hanken Grotesk (woff2 auto-hébergés)
/assets/og-suiteforge.png    image de partage social (Reddit/Twitter/iMessage)
/build.py                    générateur — source unique de vérité pour le contenu
```

## ⚠️ Avant de déployer : 1 seule chose à compléter

Les liens App Store contiennent des placeholders. Récupère l'**Apple ID numérique** de chaque app dans App Store Connect (App → General → App Information → "Apple ID", un nombre à ~10 chiffres) puis remplace les 4 tokens. Le plus simple, find/replace global dans l'éditeur ou en ligne de commande :

```bash
cd suiteforge-web
sed -i '' 's/APPSTORE_ID_FASTCLEAR/1234567890/g'    fastclear/index.html
sed -i '' 's/APPSTORE_ID_ROUTINEFLOW/1234567891/g'   routineflow/index.html
sed -i '' 's/APPSTORE_ID_WALKQUEST/1234567892/g'     walkquest/index.html
sed -i '' 's/APPSTORE_ID_KEEPCONTACT/1234567893/g'   keepcontact/index.html
```

> Mieux encore : mets les vrais IDs directement dans `build.py` (champ `appstore_id` de chaque app) et relance `python3 build.py`. Comme ça toute régénération future garde les bons liens.

## Déploiement GitHub Pages

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

1. **Les permissions listées par app** correspondent exactement à ce que l'app demande réellement (chaînes d'usage dans `Info.plist`). J'ai supposé : FastClear = HealthKit *write-only* + notifications ; WalkQuest = HealthKit *read steps* + notifications ; RoutineFlow = notifications ; KeepContact = Contacts (optionnel) + notifications. Corrige si une app diverge.
2. Si tu veux une sécurité juridique renforcée (tu opères depuis une SARL FR), une relecture par un professionnel reste recommandée.
