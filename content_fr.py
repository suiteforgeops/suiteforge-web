# -*- coding: utf-8 -*-
"""
French content of the site (pages under /fr/). build.py merges each entry over the
English one in APPS: only the texts live here; colours, icons, App Store IDs, the
order of features/screenshots and the good/bad state of each comparison cell come
from APPS. Lists must keep the same length and order as their English version.

Comparison prices come from the French App Store (euros), not from the US one.
"""

FR_APPS = {
    "fastclear": {
        "category_label": "Santé et bien-être",
        "tagline": "Un minuteur serein pour le jeûne intermittent.",
        "hero_sub": "Choisissez un protocole, lancez le minuteur et regardez votre série grandir. Pas de graphiques illisibles, pas de bruit : juste une vue claire de là où vous en êtes dans votre jeûne.",
        "seo_title": "FastClear : minuteur de jeûne intermittent privé pour iPhone",
        "seo_desc": "FastClear, le minuteur de jeûne intermittent pour iPhone qui respecte votre vie privée : 16:8, 18:6, OMAD ou sur mesure. Sans compte, sans pistage.",
        "home_blurb": "Un minuteur de jeûne intermittent clair et concentré. Choisissez un protocole, lancez votre jeûne, regardez votre série grandir.",
        "price_note": "Téléchargement gratuit · abonnement facultatif",
        "highlights": [
            ("16:8 → OMAD", "Tous les protocoles, ou votre propre fenêtre"),
            ("Widgets", "Votre jeûne sur l'écran d'accueil"),
            ("Apple Santé", "Vos jeûnes terminés, seulement si vous le voulez"),
            ("0", "Compte, publicité ou pisteur"),
        ],
        "features": [
            ("Tous les protocoles, d'un geste", "16:8, 18:6, 20:4, OMAD ou une fenêtre sur mesure. Changez quand vous voulez, sans perdre votre historique."),
            ("Des séries honnêtes", "Vos jeûnes terminés forment une série qui motive sans culpabiliser. Un jour manqué ? Vous reprenez simplement."),
            ("Apple Santé, à votre façon", "Vos jeûnes terminés peuvent être enregistrés dans Apple Santé pour garder vos données de bien-être au même endroit, seulement si vous l'autorisez."),
            ("Des widgets d'un coup d'œil", "Gardez votre jeûne en cours sur l'écran d'accueil. Un regard suffit pour savoir combien de temps il reste."),
        ],
        "steps": [
            ("Choisissez votre fenêtre", "Touchez un protocole ou réglez vos propres heures de jeûne et de repas."),
            ("Lancez le minuteur", "Votre jeûne s'affiche dans l'app, dans un widget et sur l'écran verrouillé."),
            ("Installez l'habitude", "Chaque jeûne terminé s'ajoute à votre série et, si vous le souhaitez, à Apple Santé."),
        ],
        "faq": [
            ("FastClear est-elle gratuite ?", "Oui. FastClear est gratuite à télécharger et le minuteur de base est gratuit. Un abonnement facultatif débloque les protocoles avancés et l'historique complet."),
            ("Quelle app de jeûne intermittent respecte la vie privée ?", "FastClear est conçue pour ceux qui veulent un minuteur de jeûne privé : pas de compte, pas d'outil d'analyse, pas de pisteur, et chaque jeûne est enregistré sur votre appareil, pas sur le serveur d'une entreprise."),
            ("FastClear a-t-elle besoin d'une connexion Internet ?", "Non. FastClear fonctionne entièrement hors ligne. Une connexion sert seulement à Apple pour gérer un abonnement facultatif."),
            ("FastClear partage-t-elle mes données de jeûne ?", "Non. Votre historique de jeûne ne quitte jamais votre appareil, sauf si vous choisissez d'enregistrer vos jeûnes terminés dans Apple Santé, qui reste sous votre contrôle dans l'app Santé."),
            ("FastClear gère-t-elle le 16:8 et l'OMAD ?", "Oui. FastClear gère les protocoles 16:8, 18:6, 20:4, OMAD et les fenêtres de jeûne entièrement sur mesure."),
            ("Quelle différence entre FastClear et Zero, Fastic ou BodyFast ?", "FastClear est uniquement un minuteur de jeûne, pensé pour la vie privée : son étiquette de confidentialité sur l'App Store indique « Données non collectées », elle n'a ni publicité ni compte, et ses achats intégrés vont de 3,99 € à 29,99 €. Zero, Fastic et BodyFast vont plus loin avec le suivi des repas et des calories (et une app Apple Watch pour Zero), mais d'après leurs fiches App Store, elles collectent des données liées à votre identité ; Fastic et BodyFast contiennent aussi de la publicité et utilisent des données pour vous suivre."),
        ],
        "permissions": [
            ("Apple Santé (écriture seule)", "Si vous l'autorisez, FastClear enregistre vos périodes de jeûne terminées dans Apple Santé. FastClear ne lit jamais d'autres données de santé. C'est facultatif et vous pouvez le désactiver à tout moment dans les Réglages d'iOS."),
            ("Notifications", "Utilisées seulement pour vous prévenir quand une fenêtre de jeûne ou de repas commence ou se termine. Facultatives."),
        ],
        "hero_shot_alt": "Écran d'accueil de FastClear avec un jeûne 16:8 en cours",
        "shots": [
            "Sélecteur de protocole FastClear : 16:8, 18:6, 20:4, OMAD, 5:2 et sur mesure",
            "Historique FastClear avec les derniers jeûnes terminés",
            "Statistiques FastClear avec les tendances de jeûne sur la durée",
            "Réglages FastClear : notifications et protocole",
        ],
        "compare": {
            "rows": [
                ("Données utilisées pour vous suivre sur les apps et sites d'autres entreprises", ["Aucune", "Aucune", "Localisation, coordonnées, identifiants, utilisation, achats", "Identifiants, données d'utilisation"]),
                ("Données liées à votre identité", ["Aucune : données non collectées", "Santé, localisation, coordonnées, utilisation", "Santé, localisation, coordonnées, utilisation", "E-mail, identifiants, infos sensibles, utilisation"]),
                ("Données de santé et de forme collectées par le développeur", ["Non", "Oui", "Oui", "Non déclaré"]),
                ("Contient de la publicité", ["Non", "Non", "Oui", "Oui"]),
                ("Achats intégrés affichés", ["3,99 € à 29,99 €", "10,99 € à 99,99 €", "12,99 € à 79,99 €", "11,99 € à 59,99 €"]),
                ("Suivi des repas et des calories", ["Non, jeûne uniquement", "Oui", "Oui", "Oui"]),
                ("App Apple Watch", ["Non", "Oui", "Non", "Non"]),
            ],
            "summary": "D'après leurs étiquettes de confidentialité sur l'App Store, FastClear ne collecte aucune donnée, tandis que Zero, Fastic et BodyFast collectent toutes des données liées à votre identité, dont des données de santé et de forme pour Zero et Fastic. Fastic et BodyFast utilisent aussi des données pour vous suivre sur les apps et sites d'autres entreprises, et contiennent de la publicité. Les achats intégrés de FastClear vont de 3,99 € à 29,99 €, contre jusqu'à 59,99 € à 99,99 € pour les autres. En contrepartie, Zero, Fastic et BodyFast proposent le suivi des repas et des calories, et Zero a une app Apple Watch ; FastClear n'est qu'un minuteur de jeûne.",
            "note": "FastClear fait une seule chose, le jeûne, et la garde sur votre iPhone. Si vous voulez noter vos repas ou une app Watch, les autres en font plus ; si vous voulez un minuteur de jeûne qui ne sait rien de vous, c'est FastClear.",
        },
    },

    "routineflow": {
        "category_label": "Santé et bien-être",
        "tagline": "Une routine du matin qui tient vraiment.",
        "hero_sub": "Composez une suite calme de petites étapes et avancez une étape à la fois. Pas de culpabilisation, pas de surcharge : juste un enchaînement doux pour commencer la journée à votre rythme.",
        "seo_title": "RoutineFlow : routine du matin sereine pour iPhone",
        "seo_desc": "RoutineFlow vous aide à créer et tenir une routine du matin sur iPhone : étapes guidées, rappels doux, sans compte ni pistage. Vos données restent chez vous.",
        "home_blurb": "Une routine du matin qui tient vraiment. Une étape à la fois, dans le calme, chaque jour.",
        "price_note": "Téléchargement gratuit · abonnement facultatif",
        "highlights": [
            ("1 étape", "À l'écran à la fois, jamais une liste interminable"),
            ("Rappels", "Un signal discret à l'heure choisie"),
            ("Sans culpabilité", "Un matin manqué ? Vous recommencez, tout simplement"),
            ("0", "Compte, publicité ou pisteur"),
        ],
        "features": [
            ("Composez votre enchaînement", "Ajoutez les étapes qui comptent pour vous (eau, étirements, journal, méditation) dans l'ordre qui vous convient."),
            ("Une étape à la fois", "RoutineFlow vous montre une seule étape, pas une liste intimidante. Terminez-la, passez à la suivante."),
            ("Des rappels doux", "Un signal discret à l'heure que vous choisissez. Pas de pastilles rouges qui vous crient dessus depuis l'écran d'accueil."),
            ("Progresser sans pression", "Voyez les matins où vous avez été au rendez-vous. Un matin manqué ne casse rien : vous recommencez, simplement."),
        ],
        "steps": [
            ("Dessinez votre matin", "Ajoutez et réordonnez les étapes que vous voulez faire chaque jour."),
            ("Laissez-vous porter", "Chaque matin, avancez dans votre routine une étape calme à la fois."),
            ("Revenez chaque jour", "La régularité s'installe en douceur, sans culpabilité quand la vie s'en mêle."),
        ],
        "faq": [
            ("RoutineFlow est-elle gratuite ?", "Oui. RoutineFlow est gratuite à télécharger, avec une routine de base gratuite. Un abonnement facultatif débloque plusieurs routines et des options avancées."),
            ("Quelle app de routine du matin respecte la vie privée ?", "RoutineFlow est pensée pour un début de journée calme et privé : pas de compte, pas d'outil d'analyse, pas de pisteur, et vos routines restent sur votre appareil."),
            ("Puis-je avoir plusieurs routines ?", "Vous pouvez créer une routine du matin gratuitement ; les routines supplémentaires (soir, week-end, concentration) font partie de l'abonnement facultatif."),
            ("Quelle différence entre RoutineFlow et Routinery, Fabulous ou Me+ ?", "RoutineFlow est pensée pour la vie privée : son étiquette de confidentialité sur l'App Store indique « Données non collectées », elle n'a pas de publicité, et ses achats intégrés vont de 2,99 € à 17,99 €. D'après leurs fiches App Store, Routinery, Fabulous et Me+ collectent des données et en utilisent une partie pour vous suivre, et Routinery et Me+ contiennent de la publicité ; Routinery et Fabulous proposent aussi une app Apple Watch."),
            ("RoutineFlow me piste-t-elle ?", "Non. Il n'y a ni outil d'analyse ni pisteur publicitaire. Vos données de routine ne quittent jamais votre appareil, sauf si vous utilisez la synchronisation iCloud privée."),
        ],
        "permissions": [
            ("Notifications", "Utilisées seulement pour vous rappeler de lancer votre routine à l'heure choisie. Facultatives et réglables dans les Réglages d'iOS."),
        ],
        "hero_shot_alt": "Écran d'accueil de RoutineFlow avec la liste des routines",
        "shots": [
            "RoutineFlow guide une routine une étape calme à la fois",
            "Éditeur de routine RoutineFlow : ajouter, réordonner et minuter chaque étape",
            "Réglages RoutineFlow : heure du rappel et notifications",
            "Historique RoutineFlow des routines terminées",
        ],
        "compare": {
            "rows": [
                ("Données utilisées pour vous suivre sur les apps et sites d'autres entreprises", ["Aucune", "Autres données", "Coordonnées", "Identifiants"]),
                ("Données collectées par le développeur (liées à vous ou non)", ["Aucune : données non collectées", "Coordonnées, identifiants, utilisation, diagnostic", "Localisation, coordonnées, utilisation", "Identifiants, santé et forme, contenu, utilisation"]),
                ("Contient de la publicité", ["Non", "Oui", "Non", "Oui"]),
                ("Achats intégrés affichés", ["2,99 € à 17,99 €", "0,99 € à 38,49 €", "7,99 € à 52,99 €", "9,99 € à 63,99 €"]),
                ("App Apple Watch", ["Non", "Oui", "Oui", "Non"]),
                ("Langues de l'app", ["Anglais, français", "12 langues", "7 langues", "5 langues"]),
            ],
            "summary": "D'après leurs étiquettes de confidentialité sur l'App Store, RoutineFlow ne collecte aucune donnée, tandis que Routinery, Fabulous et Me+ collectent toutes des données et en utilisent une partie pour vous suivre sur les apps et sites d'autres entreprises. Routinery et Me+ contiennent aussi de la publicité. Les achats intégrés de RoutineFlow vont de 2,99 € à 17,99 €, contre jusqu'à 38,49 € à 63,99 € pour les autres. En contrepartie, Routinery et Fabulous ont une app Apple Watch, et toutes trois sont disponibles en plus de langues.",
            "note": "RoutineFlow est une routine du matin calme, étape par étape, qui reste sur votre iPhone. Les autres ajoutent du coaching, des apps Watch et plus de langues ; RoutineFlow n'ajoute rien qui vous observe.",
        },
    },

    "walkquest": {
        "category_label": "Santé et bien-être",
        "tagline": "Faites de vos pas quotidiens une quête tranquille.",
        "hero_sub": "Fixez un objectif de pas adapté à votre vie et regardez votre progression se remplir, jour après jour. Pas de classement, pas de pression sociale : juste vous, qui bougez un peu plus.",
        "seo_title": "WalkQuest : podomètre privé pour iPhone",
        "seo_desc": "WalkQuest, le podomètre pour iPhone qui respecte votre vie privée : objectifs de marche et progrès honnêtes à partir de vos pas Apple Santé. Sans compte.",
        "home_blurb": "Faites de vos pas quotidiens une quête tranquille. Des objectifs simples, des progrès honnêtes, sans bruit.",
        "price_note": "Téléchargement gratuit · abonnement facultatif",
        "highlights": [
            ("Apple Santé", "Les pas que votre iPhone compte déjà"),
            ("Sans Watch", "Votre iPhone suffit"),
            ("Étapes clés", "Défis et récompenses"),
            ("0", "Classement, publicité ou pisteur"),
        ],
        "features": [
            ("Des objectifs à votre mesure", "Partez d'où vous en êtes. Fixez un objectif de pas réaliste et ajustez-le à mesure que l'élan vient."),
            ("Des progrès honnêtes", "Un anneau clair montre la journée d'un coup d'œil et l'historique montre la tendance, sans chiffres de vanité."),
            ("Lit Apple Santé", "WalkQuest utilise les pas déjà enregistrés sur votre iPhone. Rien de plus à porter, rien à configurer."),
            ("Une motivation discrète", "Des étapes clés douces célèbrent la régularité, pas la compétition. Votre marche ne regarde que vous."),
        ],
        "steps": [
            ("Fixez votre objectif", "Choisissez un objectif de pas quotidien qui vous semble atteignable aujourd'hui."),
            ("Marchez votre journée", "WalkQuest lit vos pas dans Apple Santé et remplit votre anneau."),
            ("Regardez-les s'additionner", "De petites journées régulières deviennent une série dont vous pouvez être fier."),
        ],
        "faq": [
            ("WalkQuest est-elle gratuite ?", "Oui. WalkQuest est gratuite à télécharger, avec le suivi quotidien des pas gratuit. Un abonnement facultatif débloque les tendances sur la durée et des objectifs supplémentaires."),
            ("Quel podomètre pour iPhone respecte la vie privée ?", "WalkQuest est un podomètre pensé pour la vie privée : il lit vos pas dans Apple Santé sur votre appareil, n'a ni compte, ni outil d'analyse, ni pisteur, et garde vos données en local."),
            ("Ai-je besoin d'une Apple Watch ?", "Non. WalkQuest utilise les pas que votre iPhone enregistre déjà dans Apple Santé. Une Apple Watch rend simplement le comptage plus précis."),
            ("Quelle différence entre WalkQuest et Pedometer++, StepsApp ou Pacer ?", "D'après leurs fiches App Store, WalkQuest n'a pas de publicité et n'utilise jamais votre localisation, tandis que Pedometer++, StepsApp et Pacer contiennent de la publicité et peuvent utiliser votre localisation quand l'app n'est pas ouverte ; StepsApp et Pacer utilisent aussi des données pour vous suivre. Les achats intégrés de WalkQuest vont de 2,99 € à 17,99 €. Pedometer++, StepsApp et Pacer proposent une app Apple Watch ; WalkQuest utilise les pas que votre iPhone et votre Apple Watch enregistrent déjà dans Apple Santé."),
            ("WalkQuest vend-elle mes données d'activité ?", "Non. WalkQuest ne vend ni ne partage jamais vos données d'activité. Vos pas restent sur votre appareil."),
        ],
        "permissions": [
            ("Apple Santé (lecture des pas)", "Avec votre accord, WalkQuest lit votre nombre de pas dans Apple Santé pour afficher votre progression du jour. Elle n'écrit rien dans Santé et n'y lit rien d'autre, et vous pouvez retirer cet accès à tout moment dans les Réglages d'iOS."),
            ("Notifications", "Utilisées seulement pour les rappels d'objectif et les étapes clés que vous activez. Facultatives."),
        ],
        "hero_shot_alt": "Écran Aujourd'hui de WalkQuest avec les pas du jour et la série en cours",
        "shots": [
            "Écran Défis de WalkQuest avec des défis de pas facultatifs",
            "Écran Succès de WalkQuest avec les badges d'étapes clés",
            "Historique WalkQuest avec le total de pas des derniers jours",
            "Réglages WalkQuest : objectif et notifications",
        ],
        "compare": {
            "rows": [
                ("Données utilisées pour vous suivre sur les apps et sites d'autres entreprises", ["Aucune", "Aucune", "Identifiants, données d'utilisation", "Localisation"]),
                ("Données liées à votre identité", ["Aucune", "Aucune", "Aucune", "Santé, localisation, contacts, coordonnées, achats, utilisation"]),
                ("Données collectées mais non liées à vous", ["Santé et forme", "Localisation, identifiants, utilisation, diagnostic", "Identifiants, utilisation, diagnostic", "Diagnostic"]),
                ("Contient de la publicité", ["Non", "Oui", "Oui", "Oui"]),
                ("Peut utiliser votre localisation quand l'app n'est pas ouverte", ["Non", "Oui", "Oui", "Oui"]),
                ("Achats intégrés affichés", ["2,99 € à 17,99 €", "1,99 € à 44,99 €", "0,99 € à 49,99 €", "4,49 € à 32,99 €"]),
                ("App Apple Watch", ["Non", "Oui", "Oui", "Oui"]),
            ],
            "summary": "D'après leurs fiches App Store, WalkQuest n'a pas de publicité, ne lie aucune donnée à votre identité, ne vous suit nulle part et n'utilise jamais votre localisation, tandis que Pedometer++, StepsApp et Pacer contiennent toutes de la publicité et peuvent utiliser votre localisation quand l'app n'est pas ouverte. StepsApp et Pacer utilisent aussi des données pour vous suivre sur les apps et sites d'autres entreprises, et Pacer lie des données de santé, de localisation et de contact à votre identité. En contrepartie, toutes trois ont une app Apple Watch.",
            "note": "WalkQuest lit les pas que votre iPhone compte déjà et sait se faire oublier : pas de publicité, pas de localisation, pas de classement. Les autres ajoutent une app Watch et des fonctions sociales.",
        },
    },

    "keepcontact": {
        "category_label": "Productivité",
        "tagline": "Restez proche des gens qui comptent.",
        "hero_sub": "Un ami que vous vouliez appeler. Un ancien collègue jamais relancé. KeepContact transforme « je devrais lui écrire » en une habitude simple, et vous aide à savoir quoi dire quand vous le faites. Sans cloud, sans compte, sans serveur.",
        "seo_title": "KeepContact : CRM personnel privé avec IA sur l'iPhone",
        "seo_desc": "CRM personnel privé pour iPhone : qui recontacter chaque matin, ce qui compte pour chacun, des idées de message par l'IA de l'iPhone. 100 % hors ligne.",
        "home_blurb": "Un CRM personnel privé. Chaque matin, qui recontacter et quoi lui dire, rédigé par l'IA embarquée de votre iPhone.",
        "price_note": "Gratuit jusqu'à 15 contacts · Pro avec 7 jours d'essai",
        "highlights": [
            ("IA embarquée", "Résumés et idées de message, sur votre iPhone"),
            ("Score /100", "La santé de vos relations d'un coup d'œil"),
            ("15 gratuits", "Contacts suivis, sans limite de durée"),
            ("100 % hors ligne", "Sans serveur, sans compte, sans synchro"),
        ],
        "privacy_extra": [
            ("IA sur l'appareil", "Sur les iPhone compatibles avec Apple Intelligence, {name} utilise le modèle de langage d'Apple qui fonctionne sur l'appareil pour résumer un contact, proposer des idées de message et repérer des informations dans vos notes. Les notes vocales sont aussi transcrites sur votre appareil. Ce traitement a lieu entièrement sur votre iPhone : vos notes et enregistrements ne sont envoyés ni à SuiteForge, ni à Apple, ni à aucun tiers."),
        ],
        "features": [
            ("Une prochaine étape claire, chaque matin", "Voyez qui attend de vos nouvelles, au rythme choisi pour chaque personne. KeepContact met une personne en avant, avec un résumé en trois lignes, une façon d'ouvrir la conversation, et des idées de message si les premiers mots ne viennent pas."),
            ("Retenez ce qui compte pour eux", "Loisirs, idées de cadeaux, allergies, prénoms de leurs enfants, le sujet sur lequel vous aviez promis de revenir. Et aussi les anniversaires, les dates importantes, le jour de votre rencontre et qui vous a présentés."),
            ("Gardez le fil", "Notez appels, cafés, messages et rendez-vous dans un même journal. Dictez une note vocale, transcrite sur votre iPhone. Scannez une carte de visite et le contact se remplit tout seul. KeepContact repère même qui vous avez vu dans votre calendrier et propose de le noter."),
            ("Votre réseau d'un coup d'œil", "Un score de santé relationnelle sur 100, des cercles du plus proche au plus lointain, et des statistiques sur ceux avec qui vous gardez vraiment le contact."),
            ("Votre année en relations", "En décembre, KeepContact compose le bilan de votre année en relations, au format story, prêt à partager, sans aucun nom affiché par défaut. Avec Pro, ajoutez une carte de vœux à envoyer avec vos messages."),
            ("Sans culpabilité, sans fouillis", "Mettez quelqu'un en veille une semaine, un mois ou sans limite. Les mises à jour de vos Contacts vous sont proposées champ par champ, et les doublons sont repérés et fusionnés d'un geste."),
        ],
        "steps": [
            ("Choisissez les personnes qui comptent", "Travail, amis, famille : choisissez qui compte et à quel rythme vous aimeriez rester en contact. Importez depuis Contacts ou ajoutez des personnes à la main."),
            ("Recontactez, avec quelque chose à dire", "Chaque matin, KeepContact vous montre qui attend de vos nouvelles, ce que vous savez de cette personne et une idée pour lancer la conversation."),
            ("Notez-le d'un geste", "Après l'appel ou le café, notez-le d'un geste ou dictez une note vocale. La prochaine fois, vous reprenez là où vous vous étiez arrêtés."),
        ],
        "faq": [
            ("KeepContact est-elle gratuite ?", "Oui. KeepContact est gratuite à télécharger, et vous pouvez suivre jusqu'à 15 contacts et 3 rappels gratuitement. KeepContact Pro lève les limites et débloque l'IA embarquée, les notes vocales, le brief du matin, le score de santé, les cercles, les statistiques, les messages à plusieurs personnes et les sauvegardes chiffrées. Votre bilan de l'année, chaque mois de décembre, est gratuit. Les abonnements incluent 7 jours d'essai gratuit, ou vous pouvez obtenir Pro à vie en un seul paiement."),
            ("Quel CRM personnel respecte la vie privée ?", "KeepContact est un CRM personnel pour iPhone pensé pour la vie privée : pas de compte, pas de serveur, pas d'outil d'analyse ni de pisteur. Chaque nom, note et rappel est enregistré sur votre appareil, et son étiquette de confidentialité sur l'App Store indique « Données non collectées »."),
            ("KeepContact envoie-t-elle mes contacts quelque part ?", "Non. KeepContact n'envoie jamais vos contacts ni vos notes. Elle fonctionne 100 % hors ligne et tout reste sur votre iPhone. Les sauvegardes sont des fichiers que vous enregistrez vous-même, et vous pouvez les chiffrer avec un mot de passe connu de vous seul."),
            ("Comment fonctionne l'IA sans envoyer mes données ?", "KeepContact utilise le modèle d'IA d'Apple qui fonctionne sur l'appareil. Les résumés, les idées de message et les informations repérées dans vos notes sont générés sur votre iPhone ; vos notes ne le quittent jamais. Il faut un iPhone compatible avec Apple Intelligence ; le reste de l'app fonctionne sur tout iPhone équipé d'une version d'iOS prise en charge."),
            ("Quelle différence entre KeepContact et Dex, Mesh (Clay) ou Contacts Journal ?", "L'étiquette de confidentialité de KeepContact sur l'App Store indique « Données non collectées » : vos contacts et vos notes ne quittent jamais votre iPhone. D'après leurs fiches App Store, Dex et Mesh (Clay) collectent vos contacts et les lient à votre identité, et Contacts Journal collecte des identifiants et des données de diagnostic. Les achats intégrés de KeepContact vont de 5,99 € à 79,99 €, option à vie comprise. Contacts Journal propose une app Apple Watch et des formules d'équipe ; les CRM dans le cloud se synchronisent entre appareils, ce que KeepContact ne fait volontairement pas."),
            ("KeepContact se synchronise-t-elle avec iCloud ?", "Pas pour le moment. KeepContact garde tout sur votre iPhone. Pour transférer vos données sur un autre iPhone, KeepContact Pro propose une sauvegarde dans les Réglages, que vous pouvez chiffrer avec votre propre mot de passe."),
        ],
        "permissions": [
            ("Contacts (facultatif)", "Si vous choisissez d'importer des personnes depuis votre carnet d'adresses, KeepContact lit vos contacts sur votre appareil pour les importer et vous proposer des mises à jour. Elle ne les envoie nulle part et n'écrit jamais dans votre carnet d'adresses. Vous pouvez utiliser KeepContact sans cette autorisation en ajoutant les personnes à la main."),
            ("Calendrier (facultatif)", "Si vous activez les suggestions du calendrier, KeepContact lit vos événements passés sur votre appareil pour vous proposer de noter le temps passé avec vos contacts. Rien n'est enregistré sans votre accord, et rien ne quitte votre iPhone."),
            ("Appareil photo (facultatif)", "Utilisé seulement quand vous scannez une carte de visite, pour la lire et préremplir un contact. L'image n'est ni enregistrée ni envoyée."),
            ("Micro (facultatif)", "Utilisé seulement si vous choisissez d'enregistrer une note vocale sur une interaction. Le micro n'est actif que pendant l'enregistrement. Les notes vocales et leurs transcriptions sont créées et enregistrées sur votre appareil."),
            ("Notifications (facultatives)", "Utilisées seulement pour les rappels de prise de contact, les anniversaires et le brief du matin que vous choisissez de recevoir. Elles sont programmées localement sur votre iPhone."),
        ],
        "hero_shot_alt": "Écran Aujourd'hui de KeepContact : la personne à qui écrire aujourd'hui, avec un résumé par l'IA embarquée, puis les autres en attente",
        "shots": [
            "Carte Préparer de KeepContact : résumé par l'IA embarquée, boutons Écrire et Appeler, idées de message",
            "Section Ce que je sais de KeepContact : loisirs, idées de cadeaux, allergies, proches et sujets à aborder",
            "Vue Mon réseau de KeepContact : vos proches en cercles, du plus proche au plus lointain",
            "Statistiques KeepContact : score de santé du réseau sur 100 et interactions sur quatre semaines",
            "Bilan de l'année KeepContact : votre année en relations en image story, noms masqués par défaut",
        ],
        "compare": {
            "rows": [
                ("Données liées à votre identité", ["Aucune : données non collectées", "Contacts, coordonnées, utilisation", "Contacts, coordonnées, contenu, historique de recherche, identifiants, utilisation", "Aucune"]),
                ("Vos contacts collectés par le développeur", ["Non", "Oui", "Oui", "Non"]),
                ("Données collectées mais non liées à vous", ["Aucune", "Diagnostic", "Diagnostic", "Identifiants, diagnostic"]),
                ("Achats intégrés affichés", ["5,99 € à 79,99 €, option à vie", "22,99 € à 249,99 €", "22,99 € à 129,99 €", "9,99 € à 399,99 €, formules d'équipe"]),
                ("App Apple Watch", ["Non", "Non", "Non", "Oui"]),
                ("Langues de l'app", ["Anglais, français", "Anglais", "Anglais", "Anglais"]),
            ],
            "summary": "D'après leurs étiquettes de confidentialité sur l'App Store, KeepContact ne collecte aucune donnée, tandis que Dex et Mesh (Clay) collectent vos contacts et les lient, avec d'autres données, à votre identité. Contacts Journal ne lie aucune donnée à vous mais collecte des identifiants et des données de diagnostic ; il propose aussi une app Apple Watch et des formules d'équipe. Les achats intégrés de KeepContact vont de 5,99 € à 79,99 €, option à vie comprise, contre jusqu'à 129,99 € à 399,99 € pour les autres.",
            "note": "Votre carnet d'adresses est la donnée la plus personnelle de votre iPhone. KeepContact ne l'envoie jamais nulle part ; les CRM dans le cloud le synchronisent sur leurs serveurs pour fonctionner entre appareils.",
        },
    },

    "jezko": {
        "category_label": "Éducation",
        "tagline": "Le serbe en famille, 10 minutes par jour.",
        "hero_sub": "Votre enfant comprend baka et deka mais n'ose pas répondre ? Ježko fait du serbe un rituel quotidien : une histoire, un hérisson, dix minutes. Les enfants suivent l'été de Milena en Serbie, parlent dès la première leçon et apprennent à lire les deux alphabets.",
        "seo_title": "Ježko : apprendre le serbe aux enfants, en famille",
        "seo_desc": "Ježko apprend le serbe aux enfants et à leur famille avec une histoire en 100 leçons : parler à voix haute, lire latin et cyrillique, 10 min par jour. Sans pub.",
        "home_blurb": "Le serbe pour les enfants et leur famille, 10 minutes par jour. Suivez l'été de Milena chez ses grands-parents en Serbie en 100 leçons, parlez dès le premier jour et apprenez à lire les deux alphabets.",
        "home_pills": ["100 leçons · A1 → B1", "Latin et cyrillique", "Jusqu'à 5 profils", "Sans publicité"],
        "price_note": "7 premières leçons offertes · français et anglais",
        "highlights": [
            ("100 leçons", "Une histoire, du A1 au B1"),
            ("10 min", "Par jour : une séance courte et complète"),
            ("2 alphabets", "Le latin d'abord, puis le cyrillique"),
            ("5 profils", "Enfants de 6 à 14 ans et adultes"),
        ],
        "features": [
            ("Une vraie histoire, 100 leçons", "Milena a 10 ans, moitié française, moitié serbe. Cet été, elle part chez ses grands-parents en Serbie avec Ježko, un hérisson du jardin réveillé dans son sac à dos. Du A1 au B1, les enfants apprennent les mots dont ils ont vraiment besoin : le marché, la slava, le village."),
            ("Parler dès le premier jour", "Écouter, répéter chaque réplique, s'enregistrer et se comparer au modèle, sans jugement. En mode Défi, des étoiles pour chaque mot reconnu, directement sur l'iPhone. Et un journal de voix à envoyer à baka."),
            ("Jouer Milena", "Jouez la scène : la famille vous donne la réplique, vous répondez avec les phrases de Milena. Dès la leçon 50, « Sad ti! » (à toi) vous fait redire de mémoire, en serbe, des phrases des leçons précédentes."),
            ("Lire les deux alphabets", "Le latin d'abord, puis le cyrillique, un groupe de lettres à la fois. Les leçons passent au cyrillique au rythme des lettres apprises : la lecture grandit avec l'histoire."),
            ("La grammaire sans règles à apprendre par cœur", "Les mots d'abord. Ensuite, 25 fiches « Coulisses » expliquent pourquoi on dit « volim čokoladu », chacune avec un mini-quiz, et des jeux font travailler les mots : paires, mot manquant, phrases dans l'ordre."),
            ("Pensé pour toute la famille", "Jusqu'à 5 profils sur un même iPhone, pour les enfants de 6 à 14 ans et pour les adultes. La répétition espacée fait revenir chaque mot au bon moment, et l'espace parent montre les progrès, les phrases dites à voix haute et l'activité de la semaine."),
        ],
        "steps": [
            ("Créez les profils de la famille", "Jusqu'à cinq apprenants, enfants et adultes, chacun avec son parcours et son rythme."),
            ("Dix minutes par jour", "Un échauffement avec les mots à revoir, une nouvelle scène de l'histoire, vos répliques à voix haute, puis un jeu."),
            ("Entendez les progrès", "Les mots reviennent au bon moment. L'espace parent montre ce qui a été appris et dit à voix haute cette semaine."),
        ],
        "faq": [
            ("Ježko est-il gratuit ?", "Les 7 premières leçons sont offertes, avec l'alphabet latin et le premier groupe de lettres cyrilliques, pour un profil. Ježko Famille débloque les 100 leçons et jusqu'à 5 profils : abonnement mensuel ou annuel avec 7 jours d'essai gratuit, ou achat unique à vie. Les trois formules peuvent être partagées avec le Partage familial."),
            ("Quelle app pour apprendre le serbe à mon enfant ?", "Ježko est une app iPhone conçue pour les enfants de 6 à 14 ans et leurs parents, notamment les familles de la diaspora serbe. Au lieu de mots isolés, elle raconte une seule histoire en 100 leçons (du A1 au B1), fait parler les enfants à voix haute dès la première leçon et enseigne les alphabets latin et cyrillique. Sans publicité, sans compte, sans pistage."),
            ("Ježko enseigne-t-il l'alphabet cyrillique ?", "Oui. Ježko commence par l'alphabet latin, puis introduit le cyrillique un groupe de lettres à la fois. Les leçons passent progressivement au cyrillique à mesure que les lettres sont apprises, et vous pouvez choisir l'affichage latin, mixte ou cyrillique."),
            ("Les adultes peuvent-ils aussi apprendre le serbe avec Ježko ?", "Oui. Ježko est conçu pour les enfants, mais chaque membre de la famille peut avoir son propre profil, adultes compris, et avancer à son rythme. Des parents qui apprennent en même temps que leurs enfants, c'est exactement l'idée."),
            ("Ježko est-il adapté aux enfants ?", "Ježko n'a ni publicité, ni compte, ni messagerie, ni pistage. Les prénoms des profils, les enregistrements et les progrès restent sur votre appareil. Sur un profil enfant, les achats, les liens externes et le partage sont protégés par un contrôle parental."),
            ("Ježko fonctionne-t-il hors ligne ?", "Oui. Les leçons et leur audio sont intégrés à l'app : Ježko fonctionne sans connexion. Une connexion sert seulement à acheter ou restaurer Ježko Famille."),
            ("Peut-on apprendre le serbe sur Duolingo ?", "Non. En octobre 2026, le catalogue de cours de Duolingo ne propose pas le serbe. Parmi les apps qui l'enseignent : Drops et Ling, qui couvrent de nombreuses langues et contiennent de la publicité, et Ježko, qui enseigne uniquement le serbe, aux enfants et à leur famille, à travers une histoire en 100 leçons, sans publicité et sans collecte de données."),
            ("Dans quelles langues Ježko est-il disponible ?", "Ježko enseigne le serbe ; l'app et toutes les traductions sont disponibles en français et en anglais."),
        ],
        "permissions": [
            ("Micro (facultatif)", "Utilisé seulement quand l'apprenant touche le bouton micro, pour enregistrer une réplique et la comparer au modèle, ou pour dire une phrase en mode Défi. Les enregistrements restent sur votre appareil et ne sont jamais envoyés. Vous pouvez refuser et continuer à utiliser l'app : chaque étape orale peut être passée."),
            ("Reconnaissance vocale (facultative)", "En mode Défi, Ježko reconnaît les mots prononcés pour attribuer des étoiles. La reconnaissance utilise le moteur vocal d'Apple sur l'appareil : votre voix n'est pas envoyée à SuiteForge."),
            ("Notifications (facultatives)", "Un rappel quotidien pour la leçon, si vous l'activez. Il est programmé localement sur votre iPhone."),
        ],
        "privacy_extra": [
            ("Profils et enregistrements", "Les prénoms des profils, les progrès, les cartes de révision et les enregistrements vocaux sont stockés uniquement sur votre appareil. Ils ne sont jamais envoyés à SuiteForge. Un enregistrement ne quitte votre appareil que si vous choisissez de le partager vous-même, via la feuille de partage d'iOS (sur un profil enfant, derrière un contrôle parental)."),
        ],
        "hero_shot_alt": "Écran Aujourd'hui de Ježko : un « Zdravo! » du hérisson, la leçon 24 prête à commencer et une série de 12 jours",
        "shots": [
            "Leçon 23 de Ježko, Hajde napolje! : le dialogue illustré entre Vuk et Tomi, en serbe avec traduction",
            "Écran Répète de Ježko : dire la réplique comme Milena, puis comparer sa voix au modèle",
            "Joue Milena dans Ježko : à toi de dire la réplique de Milena à voix haute",
            "Écran des alphabets de Ježko : les lettres cyrilliques apprises groupe par groupe",
            "Parcours de Ježko : les leçons terminées et la prochaine étape, la leçon 24",
            "Jeu des paires de Ježko : associer chaque mot serbe à son sens",
            "Fiche Coulisses de Ježko sur le masculin, le féminin et le neutre",
            "Profils de Ježko : « Qui apprend aujourd'hui ? » avec quatre profils de la famille",
        ],
        "compare": {
            "rows": [
                ("Cours de serbe", ["Oui : 100 leçons, du A1 au B1", "Non", "Oui", "Oui"]),
                ("Données utilisées pour vous suivre sur les apps et sites d'autres entreprises", ["Aucune", "Localisation, coordonnées, contenu, identifiants, utilisation, achats", "Coordonnées, identifiants, utilisation", "Coordonnées, identifiants, utilisation, achats"]),
                ("Données liées à votre identité", ["Aucune", "Localisation, contacts, coordonnées, infos financières, contenu, utilisation", "Coordonnées, identifiants, utilisation, diagnostic", "Identifiants, utilisation, achats, diagnostic"]),
                ("Contient de la publicité", ["Non", "Oui", "Oui", "Oui"]),
                ("Autres langues à apprendre", ["Non, serbe uniquement", "Oui, plus de 40", "Oui", "Oui"]),
            ],
            "summary": "Duolingo ne propose pas de cours de serbe. Drops et Ling en proposent un, parmi de nombreuses langues, mais d'après leurs fiches App Store, toutes deux contiennent de la publicité, utilisent des données pour vous suivre sur les apps et sites d'autres entreprises et lient des données à votre identité, tout comme Duolingo. Ježko enseigne uniquement le serbe, à travers une histoire en 100 leçons pour les enfants et leur famille, sans publicité, sans compte et sans collecte de données.",
            "source": "Ježko n'est pas encore sur l'App Store : sa colonne reflète la conception de l'app et sa politique de confidentialité. Cours de Duolingo : catalogue public de Duolingo.",
            "note": "Les grandes apps enseignent des dizaines de langues à tout le monde. Ježko en enseigne une, le serbe, aux enfants et à leur famille, à travers une histoire.",
        },
    },
}

FR_HOME_FAQ = [
    ("SuiteForge collecte-t-il mes données personnelles ?", "Non. Les apps SuiteForge enregistrent tout sur votre appareil (certaines peuvent aussi se synchroniser via votre propre iCloud privé). Il n'y a ni compte SuiteForge, ni outil d'analyse, ni pisteur tiers. Les seules données qui quittent votre appareil sont les informations d'achat anonymes dont Apple et notre prestataire d'abonnement ont besoin pour gérer un abonnement."),
    ("Faut-il créer un compte ?", "Non. Les apps SuiteForge fonctionnent dès le premier lancement : pas d'inscription, pas d'e-mail, pas de mot de passe."),
    ("Quel genre d'apps fait SuiteForge ?", "Des apps iPhone concentrées sur un seul usage : santé et bien-être (jeûne intermittent, routine du matin, podomètre), productivité (KeepContact, un CRM personnel privé) et éducation (Ježko, le serbe pour les enfants et leur famille). Chaque app fait une chose, bien, et fonctionne sur l'appareil."),
    ("Les apps sont-elles gratuites ?", "Chaque app est gratuite à télécharger, avec un abonnement facultatif qui débloque des fonctions avancées ; certaines proposent aussi un achat unique à vie. Vous pouvez utiliser l'essentiel de chaque app sans payer."),
    ("Faites-vous des apps pour les enfants ?", "Oui : Ježko apprend le serbe aux enfants de 6 à 14 ans et à leur famille. Comme toutes les apps SuiteForge, elle n'a ni publicité, ni compte, ni pistage, et les achats et liens externes sont protégés par un contrôle parental sur un profil enfant."),
    ("Comment obtenir de l'aide ou proposer une idée ?", "Chaque app a une option de retour dans ses réglages, ou vous pouvez écrire directement à suiteforgeops@gmail.com. Nous lisons tout."),
]
