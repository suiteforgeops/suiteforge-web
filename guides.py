# -*- coding: utf-8 -*-
"""Guides: long-form pages that answer a real question, with the app as one possible answer.

Rules (SEO and GEO): facts only, each one sourced in `sources`; first person only for what
Nicolas has made public himself; the app is presented as one option among others, never as the
only answer. One guide = one entry; `en` and `fr` hold the same sections in the same order.
Section bodies are HTML (paragraphs, lists, links); FAQ answers are plain text.
"""

GUIDES = [
    {
        "id": "serbian-for-kids",
        "app": "jezko",
        "published": "11 November 2026",
        "slug": {"en": "teach-your-child-serbian", "fr": "apprendre-le-serbe-a-son-enfant"},
        "sources": [
            ("Annick De Houwer, « Parental language input patterns and children's bilingual use », Applied Psycholinguistics 28 (3), 2007",
             "https://www.cambridge.org/core/journals/applied-psycholinguistics/article/abs/parental-language-input-patterns-and-childrens-bilingual-use/821A5852222197491F4E7ABC8AA4B099"),
            ("Constitution of the Republic of Serbia, article 10 (Language and script)",
             "https://www.refworld.org/sites/default/files/2025-07/constitution_of_the_republic_of_serbia.pdf"),
            ("Emerging Europe, « Cyrillic in Serbia is on life support, but it's not dead yet » (Latin in daily use)",
             "https://emerging-europe.com/cyrillic-in-serbia-is-on-life-support-but-its-not-dead-yet/"),
            ("Večernje novosti, « Otvorena Srpska dopunska škola u Kanu » (Serbian supplementary school in Cannes)",
             "https://www.novosti.rs/reportaze/vesti/1316202/moja-otadzbina-kroz-casove-otvorena-srpska-dopunska-skola-kanu"),
        ],
        "en": {
            "title": "How to teach your child Serbian when you live abroad",
            "seo_title": "How to teach your child Serbian abroad: a parent's guide",
            "desc": "Your child understands Serbian but won't speak it? What research says, how to create the need to speak, Latin or Cyrillic first, and 10 minutes a day that work.",
            "faq_title": "Questions parents ask",
            "lede": "Your child understands when grandma speaks Serbian, but answers in French or English. It's the most common situation in diaspora families, and it can change. Here is what research says, and what works at home.",
            "sections": [
                ("“He understands, but he won't answer”: that's normal",
                 "<p>My daughter is 10. She understands Serbian when her grandparents speak to her, but she doesn't dare answer. If that sounds like your child, you are in good company: linguists call it receptive (or passive) bilingualism. The child hears the language often enough to understand it, but almost never <em>needs</em> it to be understood, because everyone around them also speaks the language of the country.</p>"
                 "<p>The good news: understanding is the hardest part, and it is already there. What's missing is practice, and a reason to speak.</p>"),
                ("What research says",
                 "<p>In 2007, linguist Annick De Houwer studied 1,899 families in Belgium where at least one parent spoke a language other than the majority one, with children aged 6 to 10. Every child spoke the country's language. Far from all of them spoke the family language.</p>"
                 "<p>What made the difference was what the children heard at home. Homes where both parents used the family language, and at most one parent also spoke the majority language, had a high chance of success. The famous “one parent, one language” rule was neither necessary nor enough on its own.</p>"
                 "<p>In practice: the more Serbian your child hears at home, and the more often Serbian is the only way to get something done, the more likely they are to speak it. The rule you choose matters less than the amount.</p>"),
                ("Create the need to speak",
                 "<ul>"
                 "<li><strong>Video calls with the grandparents, in Serbian only.</strong> If baka doesn't speak your country's language, Serbian becomes useful, not a school subject.</li>"
                 "<li><strong>A daily Serbian moment.</strong> The bedtime story, breakfast, the drive to school: a short ritual every day beats a long session once a week.</li>"
                 "<li><strong>Questions that call for an answer in Serbian.</strong> “Hoćeš li jabuku ili krušku?” (an apple or a pear?) is easier to answer than an open question.</li>"
                 "<li><strong>Don't translate everything.</strong> If you repeat each sentence in the other language, the child learns that Serbian is optional.</li>"
                 "<li><strong>Praise the attempt, not the grammar.</strong> A child who is corrected at every word stops trying. Repeat the right form naturally in your answer instead.</li>"
                 "<li><strong>Summers in Serbia.</strong> A few weeks where Serbian is everywhere do more than months of lessons: the need to speak is real.</li>"
                 "</ul>"),
                ("Latin or Cyrillic: where to start?",
                 "<p>Serbian is written in two alphabets, Cyrillic and Latin, and both have 30 letters with one letter for each sound: you read a word the way you say it. The Constitution makes Cyrillic the script in official use, while Latin is everywhere in daily life, from shop signs to messages.</p>"
                 "<p>For a child who already reads French or English, starting with Latin is easier: most letters are familiar, and only a few are new (č, ć, š, ž, đ, dž, lj, nj). Cyrillic then comes one group of letters at a time. Watch out for the false friends: in Cyrillic, В is V, Р is R, Н is N and С is S.</p>"
                 "<p>Learning both is worth it: grandparents' books, street names and road signs in Serbia often use Cyrillic.</p>"),
                ("Ten minutes a day, and a class if you can",
                 "<p>Regularity matters more than length. Ten minutes every day keep the language alive; one hour on Saturday is quickly forgotten during the week.</p>"
                 "<p>Serbia's Ministry of Education also runs free supplementary classes in Serbian for children abroad, as in Cannes, where a school opened with the support of the Serbian Embassy in Paris and a local association. Ask your embassy or consulate whether one exists near you.</p>"),
                ("Tools that help",
                 "<p>Children's books in Serbian, cartoons and songs give the ear new words. Choose the ones your child already likes in their other language: a story they know is easier to follow.</p>"
                 "<p>I made <a href=\"/jezko/\">Ježko</a> for my daughter, because I didn't find an app made for her: one story told over 100 lessons, in which children speak out loud from the first lesson and learn to read Latin, then Cyrillic, ten minutes a day. It's one tool among others; the most important one remains the Serbian you speak at home.</p>"),
            ],
            "faq": [
                ("At what age should my child start learning Serbian?",
                 "As early as possible for listening, but it's never too late to start speaking. Children aged 6 to 14 who already understand Serbian can catch up quickly once they have regular practice and a reason to speak."),
                ("Only one of us speaks Serbian. Is it still worth it?",
                 "Yes. Research by Annick De Houwer shows that the amount of family language a child hears at home matters most. If only one parent speaks Serbian, add other sources: grandparents, friends, books, a supplementary class, summers in Serbia."),
                ("Should my child learn Latin or Cyrillic first?",
                 "For a child who already reads French or English, Latin first is easier, since most letters are familiar. Then add Cyrillic one group of letters at a time. Both alphabets have 30 letters and are read the way they are written."),
                ("My child mixes Serbian and English in the same sentence. Is that a problem?",
                 "Mixing languages is common among bilingual children and is not a sign of confusion. Answer in Serbian, repeating the word they were missing, without stopping the conversation."),
            ],
        },
        "fr": {
            "title": "Apprendre le serbe à son enfant quand on vit en France",
            "seo_title": "Apprendre le serbe à son enfant en France : le guide des parents",
            "desc": "Votre enfant comprend le serbe mais ne le parle pas ? Ce que dit la recherche, créer le besoin de parler, latin ou cyrillique d'abord, et 10 minutes par jour.",
            "faq_title": "Les questions des parents",
            "lede": "Votre enfant comprend quand sa grand-mère parle serbe, mais répond en français. C'est la situation la plus courante dans les familles de la diaspora, et elle peut changer. Voici ce que dit la recherche, et ce qui marche à la maison.",
            "sections": [
                ("« Il comprend, mais il ne répond pas » : c'est normal",
                 "<p>Ma fille a 10 ans. Elle comprend le serbe quand ses grands-parents lui parlent, mais elle n'ose pas répondre. Si c'est le cas de votre enfant, vous êtes en bonne compagnie : les linguistes parlent de bilinguisme réceptif (ou passif). L'enfant entend la langue assez souvent pour la comprendre, mais n'en a presque jamais <em>besoin</em> pour se faire comprendre, puisque tout le monde autour de lui parle aussi français.</p>"
                 "<p>La bonne nouvelle : comprendre, c'est le plus difficile, et c'est déjà acquis. Ce qui manque, c'est la pratique, et une raison de parler.</p>"),
                ("Ce que dit la recherche",
                 "<p>En 2007, la linguiste Annick De Houwer a étudié 1 899 familles en Belgique dont au moins un parent parlait une autre langue que celle du pays, avec des enfants de 6 à 10 ans. Tous les enfants parlaient la langue du pays. Loin de tous parlaient la langue de la famille.</p>"
                 "<p>La différence venait de ce que les enfants entendaient à la maison. Les foyers où les deux parents utilisaient la langue familiale, et où au plus un parent parlait aussi la langue du pays, avaient de fortes chances de réussite. La fameuse règle « un parent, une langue » n'était ni nécessaire, ni suffisante à elle seule.</p>"
                 "<p>En pratique : plus votre enfant entend de serbe à la maison, et plus le serbe est le seul moyen d'obtenir quelque chose, plus il a de chances de le parler. La règle choisie compte moins que la quantité.</p>"),
                ("Créer le besoin de parler",
                 "<ul>"
                 "<li><strong>Les appels vidéo avec les grands-parents, en serbe uniquement.</strong> Si baka ne parle pas français, le serbe devient utile, pas une matière scolaire.</li>"
                 "<li><strong>Un moment serbe chaque jour.</strong> L'histoire du soir, le petit-déjeuner, le trajet de l'école : un court rituel quotidien vaut mieux qu'une longue séance par semaine.</li>"
                 "<li><strong>Des questions qui appellent une réponse en serbe.</strong> « Hoćeš li jabuku ili krušku ? » (une pomme ou une poire ?) est plus facile à répondre qu'une question ouverte.</li>"
                 "<li><strong>Ne pas tout traduire.</strong> Si vous répétez chaque phrase en français, l'enfant apprend que le serbe est facultatif.</li>"
                 "<li><strong>Féliciter l'essai, pas la grammaire.</strong> Un enfant corrigé à chaque mot arrête d'essayer. Reprenez plutôt la bonne forme, naturellement, dans votre réponse.</li>"
                 "<li><strong>Les étés en Serbie.</strong> Quelques semaines où le serbe est partout font plus que des mois de leçons : le besoin de parler est réel.</li>"
                 "</ul>"),
                ("Latin ou cyrillique : par où commencer ?",
                 "<p>Le serbe s'écrit avec deux alphabets, le cyrillique et le latin, qui ont chacun 30 lettres, une lettre par son : on lit un mot comme on le prononce. La Constitution fait du cyrillique l'écriture d'usage officiel, tandis que le latin est partout dans la vie courante, des enseignes aux messages.</p>"
                 "<p>Pour un enfant qui lit déjà le français, commencer par le latin est plus simple : la plupart des lettres sont connues, et seules quelques-unes sont nouvelles (č, ć, š, ž, đ, dž, lj, nj). Le cyrillique vient ensuite, un groupe de lettres à la fois. Attention aux faux amis : en cyrillique, В se lit V, Р se lit R, Н se lit N et С se lit S.</p>"
                 "<p>Apprendre les deux en vaut la peine : les livres des grands-parents, les noms de rues et les panneaux en Serbie sont souvent en cyrillique.</p>"),
                ("Dix minutes par jour, et un cours si possible",
                 "<p>La régularité compte plus que la durée. Dix minutes chaque jour entretiennent la langue ; une heure le samedi s'oublie vite pendant la semaine.</p>"
                 "<p>Le ministère serbe de l'Éducation organise aussi des cours complémentaires de serbe, gratuits, pour les enfants à l'étranger, comme à Cannes, où une école a ouvert avec le soutien de l'ambassade de Serbie à Paris et d'une association locale. Renseignez-vous auprès de l'ambassade ou du consulat pour savoir s'il en existe un près de chez vous.</p>"),
                ("Les outils qui aident",
                 "<p>Les livres pour enfants en serbe, les dessins animés et les chansons apportent de nouveaux mots à l'oreille. Choisissez ceux que votre enfant aime déjà en français : une histoire qu'il connaît est plus facile à suivre.</p>"
                 "<p>J'ai fait <a href=\"/fr/jezko/\">Ježko</a> pour ma fille, parce que je n'ai pas trouvé d'app faite pour elle : une histoire racontée en 100 leçons, où les enfants parlent à voix haute dès la première leçon et apprennent à lire le latin, puis le cyrillique, dix minutes par jour. C'est un outil parmi d'autres ; le plus important reste le serbe que vous parlez à la maison.</p>"),
            ],
            "faq": [
                ("À quel âge commencer à apprendre le serbe à son enfant ?",
                 "Le plus tôt possible pour l'écoute, mais il n'est jamais trop tard pour se mettre à parler. Les enfants de 6 à 14 ans qui comprennent déjà le serbe peuvent rattraper vite, dès qu'ils ont une pratique régulière et une raison de parler."),
                ("Un seul de nous deux parle serbe. Est-ce que ça vaut quand même le coup ?",
                 "Oui. Les travaux d'Annick De Houwer montrent que c'est la quantité de langue familiale entendue à la maison qui compte le plus. Si un seul parent parle serbe, ajoutez d'autres sources : grands-parents, amis, livres, cours complémentaire, étés en Serbie."),
                ("Faut-il apprendre le latin ou le cyrillique en premier ?",
                 "Pour un enfant qui lit déjà le français, le latin d'abord est plus simple, puisque la plupart des lettres sont connues. Ajoutez ensuite le cyrillique, un groupe de lettres à la fois. Les deux alphabets ont 30 lettres et se lisent comme ils s'écrivent."),
                ("Mon enfant mélange le serbe et le français dans la même phrase. Est-ce grave ?",
                 "Mélanger les langues est courant chez les enfants bilingues et n'est pas un signe de confusion. Répondez en serbe en reprenant le mot qui lui manquait, sans arrêter la conversation."),
            ],
        },
    },

    {
        "id": "double-progression",
        "app": "crescendo",
        "published": "11 November 2026",
        "slug": {"en": "double-progression", "fr": "double-progression"},
        "sources": [
            ("American College of Sports Medicine, « Progression Models in Resistance Training for Healthy Adults », Medicine & Science in Sports & Exercise 41 (3), 2009",
             "https://pubmed.ncbi.nlm.nih.gov/19204579/"),
            ("Schoenfeld, Grgic, Ogborn, Krieger, « Strength and Hypertrophy Adaptations Between Low- vs. High-Load Resistance Training », Journal of Strength and Conditioning Research 31 (12), 2017",
             "https://pubmed.ncbi.nlm.nih.gov/28834797/"),
            ("Zourdos et al., « Novel Resistance Training-Specific Rating of Perceived Exertion Scale Measuring Repetitions in Reserve », Journal of Strength and Conditioning Research 30 (1), 2016",
             "https://openrepository.aut.ac.nz/items/efef3b25-6701-4fb5-bb82-55fcd2a26027/full"),
        ],
        "en": {
            "title": "Double progression: how much weight to add, and when",
            "seo_title": "Double progression explained: how much weight to add, and when",
            "desc": "Double progression in plain words: add reps first, then weight. How much to add, which rep range to pick, what to do when you stall, with a worked example.",
            "lede": "At the gym, the real question isn't “what do I do today?” but “how much do I lift?”. Double progression answers it with one simple rule, and no maths. Here is how it works, how much to add, and what to do when you stall.",
            "faq_title": "Questions lifters ask",
            "sections": [
                ("The question at every set",
                 "<p>I go to the gym at least three times a week, in short 30-minute sessions. At every exercise, the same question came back: same weight as last time, or more? Without a rule, you either stay at the same load for months, or you add too much and miss your reps. Double progression is the simplest rule I know to settle it.</p>"),
                ("Double progression in two sentences",
                 "<p>Pick a rep range, for example 3 sets of 8 to 12. Keep the same weight and add reps until <strong>every</strong> set reaches the top of the range; then add the smallest weight step you can, and start again from the bottom of the range.</p>"
                 "<p>You progress twice: first in reps, then in weight. Hence the name.</p>"
                 "<p><strong>Example on the bench press, 3 × 8–12:</strong></p>"
                 "<ul>"
                 "<li>Session 1, 40 kg: 12, 10, 9 reps. Not every set is at 12: same weight next time.</li>"
                 "<li>Session 2, 40 kg: 12, 11, 10. Still not there.</li>"
                 "<li>Session 3, 40 kg: 12, 12, 12. Every set at the top: next time, 42.5 kg.</li>"
                 "<li>Session 4, 42.5 kg: 10, 9, 8. Back in the range, and you start climbing again.</li>"
                 "</ul>"),
                ("How much weight to add",
                 "<p>The American College of Sports Medicine recommends a load increase of 2 to 10% when you can do one or two reps more than planned on two sessions in a row: the lower end for exercises using small muscles (curls, lateral raises), the higher end for large ones (squat, deadlift, leg press).</p>"
                 "<p>In practice, add the smallest jump your equipment allows: 2.5 kg on a barbell (1.25 kg per side), the next dumbbell, the next plate on a machine. Beware of dumbbells: going from 10 to 12 kg is a 20% jump. On light dumbbells, stay longer at the top of the range, or use a wider range (10 to 15 reps) before moving up.</p>"),
                ("Which rep range to choose",
                 "<p>A 2017 meta-analysis by Brad Schoenfeld and colleagues (21 studies) found that muscle growth was similar with light and heavy loads when sets were taken to failure, while maximal strength improved more with heavy loads.</p>"
                 "<p>So the range matters less than regular progress. Common choices: 6 to 10 reps on big compound lifts, 8 to 12 on most exercises, 10 to 15 on isolation work. If your main goal is the heaviest single lift, lower ranges (3 to 6) fit better.</p>"),
                ("When you stall",
                 "<p>Note how hard each set felt. Researchers use “reps in reserve” (RIR): how many more reps you could have done. A set where you had 2 left is RIR 2. The scale, proposed and tested by Zourdos and colleagues in 2016, helps tell a bad day from a real plateau.</p>"
                 "<p>If your reps haven't moved for several sessions at the same weight, change something rather than forcing it: a variant of the exercise, or a lighter week to recover. After a break of more than a week or two, restart a little lighter rather than where you left off. And if something hurts, stop and ask a health professional.</p>"),
                ("How Crescendo applies it",
                 "<p>I built <a href=\"/crescendo/\">Crescendo</a> to apply this rule for me, and to say why:</p>"
                 "<ul>"
                 "<li>It suggests a heavier weight only when <strong>every</strong> working set reached the top of the range, rounded to the loads your equipment actually allows, and it shows the reason in one line: “3 × 12 reached: +2.5 kg”.</li>"
                 "<li>Too many reps or too few on a set: the next set's weight adjusts within ±10%, and you can keep yours in one tap.</li>"
                 "<li>After 3 sessions without progress, it suggests a variant or a deload; after 6 sessions of the same workout, it offers a lighter session (−15%).</li>"
                 "<li>After 10 days without training, it restarts lighter (−15%, then −7.5%) and climbs back over two sessions.</li>"
                 "</ul>"
                 "<p>All of this is free. You can of course apply double progression with a notebook and a pencil: the rule is what matters.</p>"),
            ],
            "faq": [
                ("Should I add weight as soon as I hit the top of the range once?",
                 "The American College of Sports Medicine suggests waiting until you can do one or two extra reps on two sessions in a row. Requiring every set to reach the top of the range, as double progression does, is already a cautious version of the same idea."),
                ("Double progression or percentages of my 1RM?",
                 "Double progression doesn't require testing your one-rep max: your reps tell you when to move up. Percentage-based programs suit lifters who test their max regularly, often for strength sports."),
                ("What if my dumbbells go up 2 kg at a time?",
                 "On light dumbbells, a 2 kg jump can be 15 to 20% of the load. Use a wider rep range (for example 10 to 15), stay longer at the top before moving up, or add a set before adding weight."),
                ("How do I know I've stalled, and not just had a bad day?",
                 "One bad session means little: sleep, stress and food all play a part. If your reps haven't improved for about three sessions at the same weight, it's a plateau: change the exercise variant or take a lighter week."),
            ],
        },
        "fr": {
            "title": "Double progression : combien ajouter sur la barre, et quand ?",
            "seo_title": "Double progression en musculation : combien ajouter, et quand",
            "desc": "La double progression expliquée simplement : d'abord des répétitions, puis de la charge. Combien ajouter, quelle fourchette choisir, que faire quand ça bloque.",
            "lede": "En salle, la vraie question n'est pas « qu'est-ce que je fais aujourd'hui ? » mais « combien je mets ? ». La double progression y répond avec une règle simple, sans calcul. Voici comment elle marche, combien ajouter, et que faire quand ça bloque.",
            "faq_title": "Les questions qu'on se pose en salle",
            "sections": [
                ("La question à chaque série",
                 "<p>Je vais à la salle au moins trois fois par semaine, pour des séances courtes de 30 minutes. À chaque exercice, la même question revenait : la même charge que la dernière fois, ou plus ? Sans règle, soit on reste des mois à la même charge, soit on ajoute trop et on rate ses répétitions. La double progression est la règle la plus simple que je connaisse pour trancher.</p>"),
                ("La double progression en deux phrases",
                 "<p>Choisissez une fourchette de répétitions, par exemple 3 séries de 8 à 12. Gardez la même charge et ajoutez des répétitions jusqu'à ce que <strong>toutes</strong> les séries atteignent le haut de la fourchette ; ajoutez alors le plus petit saut de charge possible, et repartez du bas de la fourchette.</p>"
                 "<p>On progresse deux fois : d'abord en répétitions, puis en charge. D'où le nom.</p>"
                 "<p><strong>Exemple au développé couché, 3 × 8–12 :</strong></p>"
                 "<ul>"
                 "<li>Séance 1, 40 kg : 12, 10, 9 répétitions. Toutes les séries ne sont pas à 12 : même charge la prochaine fois.</li>"
                 "<li>Séance 2, 40 kg : 12, 11, 10. Pas encore.</li>"
                 "<li>Séance 3, 40 kg : 12, 12, 12. Toutes les séries au haut : la prochaine fois, 42,5 kg.</li>"
                 "<li>Séance 4, 42,5 kg : 10, 9, 8. De retour dans la fourchette, et on remonte.</li>"
                 "</ul>"),
                ("Combien ajouter",
                 "<p>L'American College of Sports Medicine recommande d'augmenter la charge de 2 à 10 % quand on fait une ou deux répétitions de plus que prévu sur deux séances de suite : le bas de la fourchette pour les exercices qui sollicitent de petits muscles (curls, élévations latérales), le haut pour les gros (squat, soulevé de terre, presse).</p>"
                 "<p>En pratique, ajoutez le plus petit saut que permet votre matériel : 2,5 kg sur une barre (1,25 kg de chaque côté), l'haltère suivant, la plaque suivante sur une machine. Attention aux haltères : passer de 10 à 12 kg, c'est 20 % de plus. Avec des haltères légers, restez plus longtemps au haut de la fourchette, ou prenez une fourchette plus large (10 à 15 répétitions) avant de monter.</p>"),
                ("Quelle fourchette de répétitions choisir",
                 "<p>Une méta-analyse de Brad Schoenfeld et de ses collègues (2017, 21 études) a montré que la prise de muscle était comparable avec des charges légères ou lourdes quand les séries étaient menées jusqu'à l'échec, alors que la force maximale progressait davantage avec des charges lourdes.</p>"
                 "<p>La fourchette compte donc moins que la progression régulière. Choix courants : 6 à 10 répétitions sur les gros exercices polyarticulaires, 8 à 12 sur la plupart des exercices, 10 à 15 en isolation. Si votre objectif est la charge maximale sur une répétition, des fourchettes basses (3 à 6) conviennent mieux.</p>"),
                ("Quand ça bloque",
                 "<p>Notez la difficulté de chaque série. Les chercheurs utilisent les « répétitions en réserve » (RIR, pour <em>reps in reserve</em>) : combien de répétitions vous auriez encore pu faire. Une série où il vous en restait 2, c'est RIR 2. Cette échelle, proposée et testée par Zourdos et ses collègues en 2016, aide à distinguer un mauvais jour d'un vrai plateau.</p>"
                 "<p>Si vos répétitions ne bougent plus depuis plusieurs séances à la même charge, changez quelque chose plutôt que de forcer : une variante de l'exercice, ou une semaine plus légère pour récupérer. Après une pause de plus d'une ou deux semaines, reprenez un peu plus léger plutôt qu'à la charge où vous vous étiez arrêté. Et en cas de douleur, arrêtez et demandez l'avis d'un professionnel de santé.</p>"),
                ("Comment Crescendo l'applique",
                 "<p>J'ai fait <a href=\"/fr/crescendo/\">Crescendo</a> pour qu'il applique cette règle à ma place, et qu'il dise pourquoi :</p>"
                 "<ul>"
                 "<li>Il ne propose de monter que quand <strong>toutes</strong> les séries de travail ont atteint le haut de la fourchette, en arrondissant aux charges que votre matériel permet vraiment, et il donne la raison en une ligne : « 3 × 12 atteints : +2,5 kg ».</li>"
                 "<li>Trop de répétitions ou pas assez sur une série : la charge de la série suivante s'ajuste dans la limite de ±10 %, et vous gardez la vôtre d'un geste.</li>"
                 "<li>Après 3 séances sans progrès, il propose une variante ou un deload ; après 6 séances d'une même séance, il propose une séance plus légère (−15 %).</li>"
                 "<li>Après 10 jours sans entraînement, il reprend plus léger (−15 %, puis −7,5 %) et remonte en deux séances.</li>"
                 "</ul>"
                 "<p>Tout cela est gratuit. Et vous pouvez bien sûr appliquer la double progression avec un carnet et un crayon : c'est la règle qui compte.</p>"),
            ],
            "faq": [
                ("Faut-il monter dès qu'on atteint le haut de la fourchette une fois ?",
                 "L'American College of Sports Medicine suggère d'attendre de pouvoir faire une ou deux répétitions de plus sur deux séances de suite. Exiger que toutes les séries atteignent le haut de la fourchette, comme le fait la double progression, est déjà une version prudente de la même idée."),
                ("Double progression ou pourcentages du 1RM ?",
                 "La double progression ne demande pas de tester sa charge maximale : ce sont vos répétitions qui disent quand monter. Les programmes en pourcentages conviennent à ceux qui testent régulièrement leur maximum, souvent en force athlétique."),
                ("Mes haltères montent de 2 kg en 2 kg. Comment faire ?",
                 "Avec des haltères légers, un saut de 2 kg peut représenter 15 à 20 % de la charge. Prenez une fourchette plus large (par exemple 10 à 15), restez plus longtemps au haut avant de monter, ou ajoutez une série avant d'ajouter du poids."),
                ("Comment savoir si je stagne, ou si j'ai juste eu un mauvais jour ?",
                 "Une mauvaise séance ne veut pas dire grand-chose : le sommeil, le stress et l'alimentation jouent. Si vos répétitions n'ont pas progressé depuis environ trois séances à la même charge, c'est un plateau : changez de variante ou faites une semaine plus légère."),
            ],
        },
    },

    {
        "id": "camino-steps",
        "app": "walkquest",
        "published": "12 November 2026",
        "slug": {"en": "camino-de-santiago-steps", "fr": "compostelle-combien-de-pas"},
        "sources": [
            ("Ayuntamiento de Pamplona, « Saint-Jean-Pied-de-Port / Donibane Garazi » (Camino Francés, 773 km to Santiago)",
             "https://www.pamplona.es/en/caminodesantiago/caminofrances/sanjuanpiedepuerto"),
            ("Oficina del Peregrino de Santiago, « The Compostela »",
             "https://oficinadelperegrino.com/en/?p=292"),
            ("Apple Developer, « walkingStepLength » (HealthKit)",
             "https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/walkingsteplength"),
        ],
        "en": {
            "title": "How many steps is the Camino de Santiago?",
            "seo_title": "How many steps is the Camino de Santiago? The real numbers",
            "desc": "From Saint-Jean-Pied-de-Port to Santiago: 773 km, about a million steps. How to work it out with your own step length, how long it takes, and how to walk it from home.",
            "lede": "From Saint-Jean-Pied-de-Port to Santiago de Compostela, the Camino Francés covers about 773 km. In steps, that's roughly a million. Here is how to work it out with your own stride, how long it takes on the way or at home, and what the Compostela requires.",
            "faq_title": "Questions walkers ask",
            "sections": [
                ("The short answer: about a million steps",
                 "<p>The Camino Francés, the most walked route to Santiago, starts in Saint-Jean-Pied-de-Port in the French Basque Country and covers about 773 km across northern Spain, according to the city of Pamplona's official Camino site. Guidebooks give figures between about 770 and 790 km, depending on detours and where you sleep.</p>"
                 "<p>With a typical walking step of 70 to 80 cm, that's between about 970,000 and 1.1 million steps. Call it a million.</p>"),
                ("Work it out with your own step",
                 "<p>The number of steps in a kilometre is simply 1,000 divided by your step length in metres:</p>"
                 "<ul>"
                 "<li>70 cm step: about 1,430 steps per km, so about 1.1 million steps for the Camino.</li>"
                 "<li>75 cm step: about 1,330 steps per km, about 1.03 million steps.</li>"
                 "<li>80 cm step: 1,250 steps per km, about 970,000 steps.</li>"
                 "</ul>"
                 "<p>You don't need to guess yours: on iPhone 8 and later, the Health app records your walking step length automatically when you walk steadily on flat ground. You'll find it in Health, under Mobility. With a backpack and on hills, your step gets shorter, so count a little more.</p>"),
                ("How long it takes",
                 "<p><strong>On the way:</strong> many pilgrims walk 20 to 25 km a day. At 25 km a day, 773 km take about 31 days of walking; at 20 km a day, about 39. Add rest days, and the full Camino Francés is often a five-week trip.</p>"
                 "<p><strong>At home, with your daily steps</strong> (75 cm step):</p>"
                 "<ul>"
                 "<li>5,000 steps a day (3.75 km): about 206 days, nearly 7 months.</li>"
                 "<li>8,000 steps a day (6 km): about 129 days, a little over 4 months.</li>"
                 "<li>10,000 steps a day (7.5 km): about 103 days, under 3 and a half months.</li>"
                 "</ul>"
                 "<p>My own floor is 5,000 steps a day: walking the Camino from home would take me about seven months, one ordinary day at a time.</p>"),
                ("The main stages of the Camino Francés",
                 "<p>From the Pyrenees to Galicia, the route goes through Roncesvalles, just after the climb over the mountains, then Pamplona, Logroño, Burgos, the plateau of the meseta to León, Astorga, the mountain village of O Cebreiro on the way into Galicia, Sarria, and finally Santiago de Compostela.</p>"),
                ("The Compostela: the last 100 km",
                 "<p>To receive the Compostela, the certificate given by the Pilgrim's Office in Santiago, you must walk at least the last 100 km of a recognised route (200 km by bike), and get your pilgrim's passport, the credencial, stamped along the way: twice a day on that last stretch, according to the Pilgrim's Office. That's why so many pilgrims start in Sarria, a little over 100 km from Santiago.</p>"
                 "<p>A virtual walk, however long, doesn't earn the Compostela: it's a way to prepare, to dream, or to walk the Camino when you can't leave.</p>"),
                ("Walk it from home",
                 "<p>I made <a href=\"/walkquest/\">WalkQuest</a> to give my daily steps somewhere to go. Its Camino de Santiago journey follows the same towns, from Saint-Jean-Pied-de-Port to Santiago, and moves you along the map with the walking distance your iPhone or Apple Watch already records in Apple Health. Each stop is celebrated as you reach it.</p>"
                 "<p>To be clear about the numbers: the journey in WalkQuest is 655 km, because it joins the ten towns on a simplified route, while the real path winds for about 773 km. It's one of WalkQuest's Premium journeys; two journeys are free. Nothing leaves your iPhone, and there's no account.</p>"),
            ],
            "faq": [
                ("How many steps are there in a kilometre?",
                 "1,000 divided by your step length in metres: about 1,330 steps with a 75 cm step, 1,430 with a 70 cm step, 1,250 with an 80 cm step. The Health app on iPhone measures your own walking step length under Mobility."),
                ("How many steps is the Camino Francés from Saint-Jean-Pied-de-Port?",
                 "About 773 km, so roughly a million steps: between about 970,000 and 1.1 million depending on your step length."),
                ("Can I get the Compostela by walking the Camino virtually?",
                 "No. The Compostela requires walking at least the last 100 km of a recognised route in person, with a stamped credencial. A virtual walk is a way to prepare or to enjoy the route from home."),
                ("Why is the Camino 655 km in WalkQuest and 773 km on the ground?",
                 "WalkQuest joins the main towns of the Camino Francés on a simplified route, which is shorter than the real path with all its bends. The towns and their order are the same."),
            ],
        },
        "fr": {
            "title": "Compostelle : combien de pas pour aller jusqu'à Saint-Jacques ?",
            "seo_title": "Chemin de Compostelle : combien de pas ? Les vrais chiffres",
            "desc": "De Saint-Jean-Pied-de-Port à Saint-Jacques : 773 km, environ un million de pas. Le calcul avec votre propre pas, le temps qu'il faut, et le marcher depuis chez soi.",
            "lede": "De Saint-Jean-Pied-de-Port à Saint-Jacques-de-Compostelle, le chemin français fait environ 773 km. En pas, cela fait à peu près un million. Voici comment le calculer avec votre propre foulée, combien de temps il faut sur le chemin ou chez soi, et ce que demande la Compostela.",
            "faq_title": "Les questions des marcheurs",
            "sections": [
                ("La réponse courte : environ un million de pas",
                 "<p>Le chemin français (Camino Francés), le plus parcouru vers Saint-Jacques, part de Saint-Jean-Pied-de-Port, au Pays basque, et traverse le nord de l'Espagne sur environ 773 km, d'après le site officiel du Chemin de la ville de Pampelune. Les guides donnent des chiffres entre 770 et 790 km environ, selon les détours et les lieux d'étape.</p>"
                 "<p>Avec un pas de marche courant de 70 à 80 cm, cela fait entre 970 000 et 1,1 million de pas environ. Disons un million.</p>"),
                ("Le calcul avec votre propre pas",
                 "<p>Le nombre de pas dans un kilomètre, c'est 1 000 divisé par la longueur de votre pas en mètres :</p>"
                 "<ul>"
                 "<li>Pas de 70 cm : environ 1 430 pas par km, soit environ 1,1 million de pas pour le Chemin.</li>"
                 "<li>Pas de 75 cm : environ 1 330 pas par km, environ 1,03 million de pas.</li>"
                 "<li>Pas de 80 cm : 1 250 pas par km, environ 970 000 pas.</li>"
                 "</ul>"
                 "<p>Inutile de deviner le vôtre : sur iPhone 8 et ultérieur, l'app Santé enregistre automatiquement la longueur de votre pas quand vous marchez régulièrement sur terrain plat. Vous la trouvez dans Santé, rubrique Mobilité. Avec un sac à dos et en montée, le pas raccourcit : comptez un peu plus.</p>"),
                ("Combien de temps il faut",
                 "<p><strong>Sur le chemin :</strong> beaucoup de pèlerins marchent 20 à 25 km par jour. À 25 km par jour, 773 km demandent environ 31 jours de marche ; à 20 km par jour, environ 39. Avec les jours de repos, le chemin français complet est souvent un voyage de cinq semaines.</p>"
                 "<p><strong>Chez soi, avec ses pas du quotidien</strong> (pas de 75 cm) :</p>"
                 "<ul>"
                 "<li>5 000 pas par jour (3,75 km) : environ 206 jours, près de 7 mois.</li>"
                 "<li>8 000 pas par jour (6 km) : environ 129 jours, un peu plus de 4 mois.</li>"
                 "<li>10 000 pas par jour (7,5 km) : environ 103 jours, moins de 3 mois et demi.</li>"
                 "</ul>"
                 "<p>Mon plancher, c'est 5 000 pas par jour : marcher le Chemin depuis chez moi me prendrait donc environ sept mois, une journée ordinaire après l'autre.</p>"),
                ("Les grandes étapes du chemin français",
                 "<p>Des Pyrénées à la Galice, le chemin passe par Roncevaux, juste après la traversée de la montagne, puis Pampelune, Logroño, Burgos, le plateau de la meseta jusqu'à León, Astorga, le village de montagne d'O Cebreiro à l'entrée de la Galice, Sarria, et enfin Saint-Jacques-de-Compostelle.</p>"),
                ("La Compostela : les 100 derniers kilomètres",
                 "<p>Pour recevoir la Compostela, le certificat remis par le bureau des pèlerins de Saint-Jacques, il faut avoir marché au moins les 100 derniers kilomètres d'un chemin reconnu (200 km à vélo), et faire tamponner sa credencial, le passeport du pèlerin, en chemin : deux fois par jour sur ce dernier tronçon, d'après le bureau des pèlerins. C'est pourquoi tant de pèlerins partent de Sarria, à un peu plus de 100 km de Saint-Jacques.</p>"
                 "<p>Une marche virtuelle, aussi longue soit-elle, ne donne pas droit à la Compostela : c'est une façon de se préparer, de rêver, ou de marcher le Chemin quand on ne peut pas partir.</p>"),
                ("Le marcher depuis chez soi",
                 "<p>J'ai fait <a href=\"/fr/walkquest/\">WalkQuest</a> pour donner une destination à mes pas du quotidien. Son voyage du Chemin de Compostelle suit les mêmes villes, de Saint-Jean-Pied-de-Port à Saint-Jacques, et vous fait avancer sur la carte avec la distance de marche que votre iPhone ou votre Apple Watch enregistre déjà dans Apple Santé. Chaque étape atteinte est célébrée.</p>"
                 "<p>Pour être clair sur les chiffres : le voyage fait 655 km dans WalkQuest, parce qu'il relie les dix villes par un tracé simplifié, alors que le vrai chemin serpente sur environ 773 km. C'est l'un des voyages Premium de WalkQuest ; deux voyages sont gratuits. Rien ne quitte votre iPhone, et il n'y a pas de compte.</p>"),
            ],
            "faq": [
                ("Combien de pas dans un kilomètre ?",
                 "1 000 divisé par la longueur de votre pas en mètres : environ 1 330 pas avec un pas de 75 cm, 1 430 avec un pas de 70 cm, 1 250 avec un pas de 80 cm. L'app Santé de l'iPhone mesure la longueur de votre pas dans la rubrique Mobilité."),
                ("Combien de pas pour le chemin français depuis Saint-Jean-Pied-de-Port ?",
                 "Environ 773 km, soit à peu près un million de pas : entre 970 000 et 1,1 million environ selon la longueur de votre pas."),
                ("Peut-on obtenir la Compostela en marchant le Chemin virtuellement ?",
                 "Non. La Compostela demande d'avoir marché soi-même au moins les 100 derniers kilomètres d'un chemin reconnu, avec une credencial tamponnée. Une marche virtuelle sert à se préparer ou à profiter du parcours depuis chez soi."),
                ("Pourquoi le Chemin fait-il 655 km dans WalkQuest et 773 km sur le terrain ?",
                 "WalkQuest relie les principales villes du chemin français par un tracé simplifié, plus court que le vrai chemin avec tous ses détours. Les villes et leur ordre sont les mêmes."),
            ],
        },
    },

    {
        "id": "keep-in-touch",
        "app": "keepcontact",
        "published": "12 November 2026",
        "slug": {"en": "keep-in-touch-with-friends", "fr": "garder-le-contact-avec-ses-amis"},
        "sources": [
            ("Liu, Rim, Min, Min, « The Surprise of Reaching Out: Appreciated More Than We Think », Journal of Personality and Social Psychology 124 (4), 2023 (APA press release)",
             "https://www.apa.org/news/press/releases/2022/07/friends-enjoy-being-reached"),
            ("Jeffrey A. Hall, « How many hours does it take to make a friend? », Journal of Social and Personal Relationships, 2018 (University of Kansas release)",
             "https://news.ku.edu/news/article/2018/03/06/study-reveals-number-hours-it-takes-make-friend"),
            ("Holt-Lunstad, Smith, Layton, « Social Relationships and Mortality Risk: A Meta-analytic Review », PLoS Medicine, 2010",
             "https://doaj.org/article/c9833ba608474b048444b92ae7ee48ad"),
        ],
        "en": {
            "title": "How to keep in touch with friends when you're busy",
            "seo_title": "How to keep in touch with friends when you're busy",
            "desc": "You think of them but never write? What research says about reaching out, how often to do it, what to say in 30 seconds, and simple rituals that keep friendships alive.",
            "lede": "A friend you meant to call. A former colleague you never followed up with. Most of us think about the people who matter far more often than we tell them. Here is what research says, and a few simple habits that change it.",
            "faq_title": "Questions people ask",
            "sections": [
                ("We think of them, but we don't write",
                 "<p>The hardest part is rarely knowing what to say: it's the feeling that it's been too long, that the message will be awkward, or that the other person won't care.</p>"
                 "<p>Research says otherwise. In a series of experiments published in 2022 in the Journal of Personality and Social Psychology, Peggy Liu and her colleagues found that people consistently underestimate how much others appreciate being reached out to, with a short message, a note or a small gift. And the more unexpected the message, the more it's appreciated: an old friend you haven't spoken to in a while is exactly the person who will be glad to hear from you.</p>"),
                ("Why it's worth the effort",
                 "<p>Friendships take time to build. Jeffrey Hall, at the University of Kansas, estimated that it takes about 50 hours together to go from acquaintance to casual friend, about 90 hours to become friends, and more than 200 hours to become close friends. That time is an investment you don't want to lose to silence.</p>"
                 "<p>And it matters beyond the pleasure of it. A 2010 meta-analysis by Julianne Holt-Lunstad and colleagues, covering 148 studies and more than 300,000 people, found that people with stronger social relationships were more likely to survive over the period studied, an effect the authors describe as comparable to well-known risk factors.</p>"),
                ("Choose who, and how often",
                 "<p>You can't keep up with everyone, and you don't need to. Start with a short list: the five to fifteen people you would genuinely miss. A few years ago, I sorted out my own circle and moved away from people who constantly criticise; it left more room for the others.</p>"
                 "<p>Then give each person a rhythm that fits the relationship: every week or two for the closest, every month for good friends, every few months for the people you don't want to lose touch with. There is no right number; what counts is that it's realistic for you.</p>"),
                ("A 30-second message is enough",
                 "<p>You don't need a long catch-up. A short, specific message does the job:</p>"
                 "<ul>"
                 "<li>“Saw this and thought of you. How did the move go?”</li>"
                 "<li>“It's been too long! Coffee next week?”</li>"
                 "<li>“Happy birthday! How's the new job treating you?”</li>"
                 "</ul>"
                 "<p>The secret is the detail: the move, the new job, the child who started school. Write down what people tell you after each conversation, and you'll always have something to say next time.</p>"),
                ("Rituals rather than willpower",
                 "<p>Good intentions fade; habits stay. Attach reaching out to something you already do: a message during your Sunday morning coffee, a call on the walk home on Thursdays, birthdays in your calendar with a reminder the day before. Two or three people a week is enough to keep a whole circle alive over a year.</p>"),
                ("A tool to remember for you",
                 "<p>A notebook and your phone's reminders can do the job. <a href=\"/keepcontact/\">KeepContact</a> is the app I make for it: you choose a rhythm for each person, and it shows you who is overdue. It keeps birthdays, the things that matter to each person and the thread of your conversations. With Pro, a morning brief puts one person first with a short summary, and its on-device AI suggests a first sentence when you're stuck.</p>"
                 "<p>It's free for up to 15 contacts, which is enough for the short list above. Everything stays on your iPhone: no account, no server, and your address book is never uploaded.</p>"),
            ],
            "faq": [
                ("Is it weird to reach out to someone after years of silence?",
                 "Less than you think. Research by Peggy Liu and colleagues shows that people appreciate being contacted more than senders expect, and even more so when the message is a surprise. A short, warm message is usually welcome."),
                ("How often should I contact a friend?",
                 "There is no universal rule. Choose a rhythm per person: every week or two for the closest, every month for good friends, every few months for others. A realistic rhythm you keep beats an ambitious one you abandon."),
                ("What can I say when I don't know what to write?",
                 "Mention something they told you last time, a shared memory, or something you saw that made you think of them, then ask a simple question. Keeping short notes after each conversation makes this easy."),
                ("Do I need an app to keep in touch?",
                 "No. A notebook and calendar reminders work. An app helps when your list grows, by remembering rhythms, birthdays and what each person told you."),
            ],
        },
        "fr": {
            "title": "Garder le contact avec ses amis quand on n'a pas le temps",
            "seo_title": "Garder le contact avec ses amis quand on manque de temps",
            "desc": "Vous pensez à eux mais n'écrivez jamais ? Ce que dit la recherche, à quel rythme reprendre contact, quoi écrire en 30 secondes, et des rituels qui entretiennent l'amitié.",
            "lede": "Un ami qu'on voulait appeler. Un ancien collègue qu'on n'a jamais relancé. On pense aux gens qui comptent bien plus souvent qu'on ne le leur dit. Voici ce que dit la recherche, et quelques habitudes simples qui changent ça.",
            "faq_title": "Les questions qu'on se pose",
            "sections": [
                ("On pense à eux, mais on n'écrit pas",
                 "<p>Le plus difficile est rarement de savoir quoi dire : c'est l'impression que cela fait trop longtemps, que le message sera gênant, ou que l'autre s'en moquera.</p>"
                 "<p>La recherche dit le contraire. Dans une série d'expériences publiées en 2022 dans le Journal of Personality and Social Psychology, Peggy Liu et ses collègues ont montré qu'on sous-estime systématiquement à quel point les autres apprécient qu'on prenne de leurs nouvelles, par un court message, un mot ou un petit cadeau. Et plus le message est inattendu, plus il est apprécié : un vieil ami à qui l'on n'a pas parlé depuis longtemps est justement celui qui sera content d'avoir de vos nouvelles.</p>"),
                ("Pourquoi ça vaut l'effort",
                 "<p>Une amitié prend du temps à construire. Jeffrey Hall, de l'université du Kansas, a estimé qu'il faut environ 50 heures passées ensemble pour passer de connaissance à copain, environ 90 heures pour devenir amis, et plus de 200 heures pour devenir amis proches. Ce temps est un investissement qu'on n'a pas envie de perdre dans le silence.</p>"
                 "<p>Et cela compte au-delà du plaisir. Une méta-analyse de Julianne Holt-Lunstad et ses collègues, publiée en 2010 et portant sur 148 études et plus de 300 000 personnes, a montré que les personnes aux liens sociaux plus forts avaient davantage de chances de survie sur la période étudiée, un effet que les auteurs jugent comparable à celui de facteurs de risque bien connus.</p>"),
                ("Choisir qui, et à quel rythme",
                 "<p>On ne peut pas suivre tout le monde, et ce n'est pas nécessaire. Commencez par une courte liste : les cinq à quinze personnes qui vous manqueraient vraiment. Il y a quelques années, j'ai fait le tri dans mon entourage et je me suis éloigné des gens qui critiquent sans cesse ; cela a laissé plus de place aux autres.</p>"
                 "<p>Donnez ensuite à chacun un rythme adapté à la relation : toutes les une ou deux semaines pour les plus proches, chaque mois pour les bons amis, tous les quelques mois pour ceux avec qui vous ne voulez pas perdre le lien. Il n'y a pas de bon chiffre ; ce qui compte, c'est qu'il soit réaliste pour vous.</p>"),
                ("Un message de 30 secondes suffit",
                 "<p>Pas besoin d'un long rattrapage. Un message court et précis fait l'affaire :</p>"
                 "<ul>"
                 "<li>« J'ai vu ça et j'ai pensé à toi. Ça s'est bien passé, le déménagement ? »</li>"
                 "<li>« Ça fait trop longtemps ! Un café la semaine prochaine ? »</li>"
                 "<li>« Joyeux anniversaire ! Et ce nouveau boulot, ça se passe comment ? »</li>"
                 "</ul>"
                 "<p>Le secret, c'est le détail : le déménagement, le nouveau travail, l'enfant qui vient d'entrer à l'école. Notez ce que les gens vous racontent après chaque conversation, et vous aurez toujours quelque chose à dire la fois suivante.</p>"),
                ("Des rituels plutôt que de la volonté",
                 "<p>Les bonnes intentions s'effacent ; les habitudes restent. Accrochez la prise de nouvelles à quelque chose que vous faites déjà : un message pendant le café du dimanche matin, un appel sur le trajet du retour le jeudi, les anniversaires dans votre agenda avec un rappel la veille. Deux ou trois personnes par semaine suffisent à entretenir tout un cercle sur une année.</p>"),
                ("Un outil qui se souvient pour vous",
                 "<p>Un carnet et les rappels de votre téléphone peuvent suffire. <a href=\"/fr/keepcontact/\">KeepContact</a> est l'app que je fais pour ça : vous choisissez un rythme pour chaque personne, et elle vous montre qui attend de vos nouvelles. Elle garde les anniversaires, ce qui compte pour chacun et le fil de vos échanges. Avec Pro, un point du matin met une personne en avant avec un court résumé, et son IA intégrée à l'iPhone propose une première phrase quand vous séchez.</p>"
                 "<p>Elle est gratuite jusqu'à 15 contacts, ce qui suffit pour la courte liste ci-dessus. Tout reste sur votre iPhone : pas de compte, pas de serveur, et votre carnet d'adresses n'est jamais envoyé nulle part.</p>"),
            ],
            "faq": [
                ("Est-ce bizarre de reprendre contact après des années de silence ?",
                 "Moins qu'on ne le croit. Les travaux de Peggy Liu et ses collègues montrent que les gens apprécient d'être contactés davantage que ne l'imagine celui qui écrit, et encore plus quand le message est une surprise. Un message court et chaleureux est en général bien reçu."),
                ("À quelle fréquence prendre des nouvelles d'un ami ?",
                 "Il n'y a pas de règle universelle. Choisissez un rythme par personne : toutes les une ou deux semaines pour les plus proches, chaque mois pour les bons amis, tous les quelques mois pour les autres. Un rythme réaliste et tenu vaut mieux qu'un rythme ambitieux abandonné."),
                ("Que dire quand on ne sait pas quoi écrire ?",
                 "Rappelez quelque chose qu'il vous a raconté la dernière fois, un souvenir commun, ou une chose vue qui vous a fait penser à lui, puis posez une question simple. Prendre quelques notes après chaque conversation rend cela facile."),
                ("Faut-il une app pour garder le contact ?",
                 "Non. Un carnet et des rappels dans l'agenda fonctionnent. Une app aide quand la liste s'allonge, en retenant les rythmes, les anniversaires et ce que chacun vous a dit."),
            ],
        },
    },

    {
        "id": "morning-routine",
        "app": "routineflow",
        "published": "12 November 2026",
        "slug": {"en": "morning-routine-that-sticks", "fr": "routine-du-matin-qui-tient"},
        "sources": [
            ("Lally, van Jaarsveld, Potts, Wardle, « How are habits formed: Modelling habit formation in the real world », European Journal of Social Psychology 40 (6), 2010 (British Psychological Society summary)",
             "https://bps.org.uk/research-digest/how-form-habit"),
            ("Gollwitzer, Sheeran, « Implementation Intentions and Goal Achievement: A Meta-analysis of Effects and Processes », Advances in Experimental Social Psychology 38, 2006",
             "https://kops.uni-konstanz.de/server/api/core/bitstreams/eb48c8cf-7855-478e-90ec-1ea6d44f8252/content"),
        ],
        "en": {
            "title": "How to build a morning routine that sticks",
            "seo_title": "How to build a morning routine that sticks (before your phone wins)",
            "desc": "Why morning routines fail, how long a habit really takes to form, how to start with 10 minutes, and how to keep your phone out of the way until you're done.",
            "lede": "You set the alarm early, you have a plan, and twenty minutes later you're still scrolling in bed. Morning routines rarely fail for lack of motivation: they fail because they're too big, too vague, and because the phone gets there first. Here is what research says, and how to build one that holds.",
            "faq_title": "Questions people ask",
            "sections": [
                ("Why morning routines fall apart",
                 "<p>Most routines start too ambitious: an hour of sport, meditation, journaling and reading, from day one. After a short night, the whole thing feels impossible, so you skip it, and the next day it's harder to start again. And in between, the phone on the nightstand offers something easier: messages, news, a feed that never ends.</p>"
                 "<p>A routine that holds is short, precise and protected from the phone.</p>"),
                ("How long a habit really takes",
                 "<p>The “21 days to form a habit” you often read has no solid basis. In 2010, Phillippa Lally and her colleagues at University College London followed participants who chose a new daily habit, such as drinking a glass of water at breakfast or going for a run before dinner. It took them 66 days on average for the behaviour to become automatic, with very wide differences: from 18 to 254 days depending on the person and the habit.</p>"
                 "<p>Two findings help: missing one day didn't significantly harm the process, and more complex behaviours took longer to become automatic. In other words: start simple, and don't give up after a missed morning.</p>"),
                ("Start small: three steps, ten minutes",
                 "<p>Choose three steps you can do even on a bad day, and give each one a duration. For example:</p>"
                 "<ul>"
                 "<li>A glass of water: 1 minute.</li>"
                 "<li>Three stretches: 3 minutes.</li>"
                 "<li>Plan the day: 2 minutes.</li>"
                 "</ul>"
                 "<p>That's the <a href=\"/routineflow/routines/morning-express/\">5-minute morning</a>. When it's automatic, add a step: deep breathing, a cool shower, reading. The <a href=\"/routineflow/routines/morning-energy/\">Energizing morning</a> is a good next level. Times matter: a step with a duration ends, a vague intention never does.</p>"),
                ("Decide in advance: “when X, I do Y”",
                 "<p>Psychologists call it an implementation intention: a plan in the form “when this happens, I do that”. In their 2006 meta-analysis of 94 tests, Peter Gollwitzer and Paschal Sheeran found that this kind of plan helped people act on their goals; a 2024 update suggests the effect is more modest than first estimated, but real.</p>"
                 "<p>For the morning: “when my alarm rings, I get up and drink a glass of water”, “when I've had my coffee, I start the routine”. Hook the routine to something that already happens every day.</p>"),
                ("Keep the phone out of the way",
                 "<p>The simplest solution is physical: charge your phone outside the bedroom and use a separate alarm clock. If that's not possible, iPhone's Screen Time lets you limit apps by time slot, and some apps go further by locking the distracting apps until your routine is done. Either way, the rule is the same: the routine first, the phone after.</p>"),
                ("On the days it doesn't happen",
                 "<p>You'll miss mornings: illness, travel, a sleepless night. According to Lally's study, a single missed day doesn't undo the habit; what breaks it is giving up after the miss. Have a minimal version for bad days (just the glass of water and one stretch) and pick up the full routine the next day.</p>"),
                ("With RoutineFlow",
                 "<p>I use <a href=\"/routineflow/\">RoutineFlow</a> every morning. It guides your routine step by step, out loud, with a timer for each step, and keeps the apps you choose (Instagram, TikTok, news) locked until the routine is done. The block always ends, when you finish or after a safety limit you set.</p>"
                 "<p>The free version includes 2 routines of up to 8 steps, voice guidance, the Live Activity, reminders, 3 templates and one free “Earn your phone” morning; Premium unlocks app blocking every day, all templates and the Apple Watch app. No account and no ads.</p>"),
            ],
            "faq": [
                ("How long does it take for a morning routine to become a habit?",
                 "There's no fixed number. In Phillippa Lally's 2010 study, it took 66 days on average for a new daily behaviour to become automatic, from 18 to 254 days depending on the person and the habit. Simple routines become automatic faster."),
                ("What should I do if I miss a morning?",
                 "Pick it up again the next day. Lally's study found that missing one day didn't significantly affect habit formation; giving up after a miss is what breaks it. Keep a minimal version for bad days."),
                ("How many steps should a morning routine have?",
                 "Start with three steps and about ten minutes, simple enough to do on a bad day. Add a step only when the routine feels automatic."),
                ("How do I stop checking my phone first thing in the morning?",
                 "Charge it outside the bedroom and use a separate alarm clock, or use Screen Time or an app that locks distracting apps until your routine is done. Hooking the routine to your alarm (“when it rings, I get up and drink water”) also helps."),
            ],
        },
        "fr": {
            "title": "Une routine du matin qui tient, avant que le téléphone ne gagne",
            "seo_title": "Routine du matin : comment la tenir (avant que le téléphone ne gagne)",
            "desc": "Pourquoi les routines du matin échouent, combien de temps il faut vraiment pour une habitude, commencer par 10 minutes, et tenir le téléphone à l'écart jusqu'à la fin.",
            "lede": "Le réveil sonne tôt, vous avez un plan, et vingt minutes plus tard vous faites encore défiler votre écran au lit. Les routines du matin échouent rarement par manque de motivation : elles échouent parce qu'elles sont trop longues, trop floues, et parce que le téléphone arrive en premier. Voici ce que dit la recherche, et comment en construire une qui tient.",
            "faq_title": "Les questions qu'on se pose",
            "sections": [
                ("Pourquoi les routines du matin s'écroulent",
                 "<p>La plupart des routines démarrent trop ambitieuses : une heure de sport, de méditation, de journal et de lecture, dès le premier jour. Après une nuit courte, tout semble impossible, alors on saute, et le lendemain il est plus dur de recommencer. Et entre-temps, le téléphone sur la table de nuit propose plus facile : les messages, les infos, un fil sans fin.</p>"
                 "<p>Une routine qui tient est courte, précise et protégée du téléphone.</p>"),
                ("Combien de temps il faut vraiment pour une habitude",
                 "<p>Les « 21 jours pour prendre une habitude » qu'on lit souvent ne reposent sur rien de solide. En 2010, Phillippa Lally et ses collègues de l'University College London ont suivi des participants qui avaient choisi une nouvelle habitude quotidienne, comme boire un verre d'eau au petit-déjeuner ou courir avant le dîner. Il leur a fallu en moyenne 66 jours pour que le geste devienne automatique, avec de très grands écarts : de 18 à 254 jours selon les personnes et les habitudes.</p>"
                 "<p>Deux résultats aident : rater un jour n'a pas nui de façon significative, et les gestes plus complexes ont mis plus de temps à devenir automatiques. Autrement dit : commencez simple, et n'abandonnez pas après un matin raté.</p>"),
                ("Commencer petit : trois étapes, dix minutes",
                 "<p>Choisissez trois étapes que vous pouvez faire même un mauvais jour, et donnez une durée à chacune. Par exemple :</p>"
                 "<ul>"
                 "<li>Un verre d'eau : 1 minute.</li>"
                 "<li>Trois étirements : 3 minutes.</li>"
                 "<li>Planifier la journée : 2 minutes.</li>"
                 "</ul>"
                 "<p>C'est le <a href=\"/fr/routineflow/routines/morning-express/\">Matin express</a>. Quand il devient automatique, ajoutez une étape : respiration profonde, douche fraîche, lecture. Le <a href=\"/fr/routineflow/routines/morning-energy/\">Matin énergie</a> est un bon palier suivant. Les durées comptent : une étape chronométrée se termine, une intention floue jamais.</p>"),
                ("Décider d'avance : « quand X, je fais Y »",
                 "<p>Les psychologues parlent d'intention de mise en œuvre : un plan de la forme « quand ceci arrive, je fais cela ». Dans leur méta-analyse de 2006 portant sur 94 tests, Peter Gollwitzer et Paschal Sheeran ont montré que ce type de plan aidait à passer à l'acte ; une mise à jour de 2024 juge l'effet plus modeste qu'estimé au départ, mais réel.</p>"
                 "<p>Pour le matin : « quand mon réveil sonne, je me lève et je bois un verre d'eau », « quand j'ai bu mon café, je lance la routine ». Accrochez la routine à quelque chose qui arrive déjà chaque jour.</p>"),
                ("Tenir le téléphone à l'écart",
                 "<p>La solution la plus simple est physique : chargez votre téléphone hors de la chambre et utilisez un vrai réveil. Si ce n'est pas possible, Temps d'écran sur iPhone permet de limiter des apps par plage horaire, et certaines apps vont plus loin en bloquant les apps qui distraient jusqu'à la fin de la routine. Dans tous les cas, la règle est la même : la routine d'abord, le téléphone ensuite.</p>"),
                ("Les jours où ça ne se fait pas",
                 "<p>Vous raterez des matins : maladie, voyage, nuit blanche. D'après l'étude de Lally, un jour manqué ne défait pas l'habitude ; ce qui la casse, c'est d'abandonner après. Prévoyez une version minimale pour les mauvais jours (juste le verre d'eau et un étirement), et reprenez la routine complète le lendemain.</p>"),
                ("Avec RoutineFlow",
                 "<p>J'utilise <a href=\"/fr/routineflow/\">RoutineFlow</a> tous les matins. Elle vous guide pas à pas, à voix haute, avec un minuteur pour chaque étape, et garde bloquées les apps que vous choisissez (Instagram, TikTok, les infos) jusqu'à la fin de la routine. Le blocage se termine toujours, quand vous finissez ou après une limite de sécurité que vous fixez.</p>"
                 "<p>La version gratuite comprend 2 routines de 8 étapes au plus, le guidage vocal, la Live Activity, les rappels, 3 modèles et une matinée « Gagnez votre téléphone » offerte ; Premium débloque le blocage des apps tous les jours, tous les modèles et l'app Apple Watch. Sans compte et sans publicité.</p>"),
            ],
            "faq": [
                ("Combien de temps faut-il pour qu'une routine du matin devienne une habitude ?",
                 "Il n'y a pas de chiffre fixe. Dans l'étude de Phillippa Lally (2010), il a fallu en moyenne 66 jours pour qu'un nouveau geste quotidien devienne automatique, de 18 à 254 jours selon les personnes et les habitudes. Les routines simples deviennent automatiques plus vite."),
                ("Que faire si je rate un matin ?",
                 "Reprendre le lendemain. L'étude de Lally a montré que rater un jour ne nuisait pas de façon significative à la formation de l'habitude ; c'est l'abandon après le raté qui la casse. Gardez une version minimale pour les mauvais jours."),
                ("Combien d'étapes doit compter une routine du matin ?",
                 "Commencez par trois étapes et une dizaine de minutes, assez simples pour les faire un mauvais jour. N'ajoutez une étape que quand la routine devient automatique."),
                ("Comment ne plus prendre son téléphone dès le réveil ?",
                 "Chargez-le hors de la chambre et utilisez un vrai réveil, ou servez-vous de Temps d'écran ou d'une app qui bloque les apps qui distraient jusqu'à la fin de la routine. Accrocher la routine au réveil (« quand il sonne, je me lève et je bois de l'eau ») aide aussi."),
            ],
        },
    },

    {
        "id": "fasting-16-8",
        "app": "fastclear",
        "published": "12 November 2026",
        "slug": {"en": "16-8-intermittent-fasting", "fr": "jeune-intermittent-16-8"},
        "sources": [
            ("Lowe et al., « Effects of Time-Restricted Eating on Weight Loss and Other Metabolic Parameters (TREAT) », JAMA Internal Medicine 180 (11), 2020",
             "https://pubmed.ncbi.nlm.nih.gov/32986097/"),
            ("de Cabo, Mattson, « Effects of Intermittent Fasting on Health, Aging, and Disease », New England Journal of Medicine 381, 2019",
             "https://doi.org/10.1056/NEJMra1905136"),
            ("Johns Hopkins Medicine, « Intermittent Fasting: What is it, and how does it work? »",
             "https://www.hopkinsmedicine.org/health/wellness-and-prevention/intermittent-fasting-what-is-it-and-how-does-it-work"),
        ],
        "en": {
            "title": "16:8 intermittent fasting: when to start counting, and what it really does",
            "seo_title": "16:8 intermittent fasting: when to start counting, what breaks a fast",
            "desc": "16:8 fasting in plain words: when the 16 hours start, what you can drink, how to choose your eating window, what research really shows, and who shouldn't fast.",
            "lede": "16:8 is the most popular form of intermittent fasting: 16 hours without eating, then an 8-hour eating window. The idea is simple; the details are where people get stuck. When does the fast start? Does coffee break it? And what does it actually do? Here are clear answers, including the less exciting ones.",
            "faq_title": "Questions people ask",
            "sections": [
                ("16:8 in one sentence",
                 "<p>You go 16 hours without eating, then eat within an 8-hour window, every day or on the days you choose. In practice, the night does most of the work: if you finish dinner at 8 pm and eat again at noon, that's 16 hours.</p>"),
                ("When the 16 hours start",
                 "<p>The fast starts with your <strong>last bite</strong>, not when you go to bed or when you remember to start a timer. Sleep counts. If you forgot to start your timer, simply set the start time to when you actually finished eating: what matters is the real time, not the button.</p>"
                 "<p>Nothing magic happens at exactly 16:00:00. If one day you stop at 15 hours, or go on to 17, the fast still counts.</p>"),
                ("What breaks a fast, and what doesn't",
                 "<p>During the fasting hours, Johns Hopkins Medicine lists water and zero-calorie drinks such as black coffee and tea as permitted. Sparkling water and plain herbal tea fall in the same category.</p>"
                 "<p>Anything with calories ends the fast: milk in your coffee, sugar, juice, a snack, a smoothie. Drinks with sweeteners are debated; if you want to keep things simple, stick to water, black coffee and plain tea.</p>"),
                ("Choose a window that fits your life",
                 "<p>The best window is the one you can keep. Common options:</p>"
                 "<ul>"
                 "<li><strong>Noon to 8 pm:</strong> skip breakfast, keep family dinner. The most common choice.</li>"
                 "<li><strong>10 am to 6 pm:</strong> a late breakfast and an early dinner.</li>"
                 "<li><strong>8 am to 4 pm:</strong> for early risers who don't mind a light evening.</li>"
                 "</ul>"
                 "<p>Social life matters: if Friday dinners are late, shift the window that day rather than giving up. Regularity helps more than perfection.</p>"),
                ("What research really shows",
                 "<p>The honest answer is less spectacular than many apps suggest. In the TREAT trial, published in 2020 in JAMA Internal Medicine, 116 adults with overweight or obesity were randomised either to eat only between noon and 8 pm, or to eat three structured meals a day, for 12 weeks. The 16:8 group lost about 0.9 kg and the meals group about 0.7 kg: the difference between the two was not significant. The authors concluded that time-restricted eating alone was not more effective for weight loss than eating throughout the day.</p>"
                 "<p>A 2019 review in the New England Journal of Medicine by Rafael de Cabo and Mark Mattson describes promising effects of intermittent fasting on metabolism, many of them observed in animals, while human trials have mostly been short. Timelines you may see for “milestones” such as ketosis or autophagy come largely from that kind of research: treat them as rough orders of magnitude, not promises.</p>"
                 "<p>In other words, 16:8 is a framework. It helps some people eat more regularly and snack less in the evening; what you eat in the window still matters.</p>"),
                ("Who shouldn't fast",
                 "<p>Johns Hopkins Medicine advises against intermittent fasting for children and teenagers under 18, and for people with a history of eating disorders, and warns that people with type 1 diabetes who take insulin risk dangerously low blood sugar while fasting. Pregnancy and breastfeeding, which increase energy needs, call for advice from your doctor or midwife. If you take regular medication or have a health condition, talk to your doctor before starting.</p>"),
                ("A timer that follows your real rhythm",
                 "<p><a href=\"/fastclear/\">FastClear</a> is the fasting timer I make for exactly these details. You can correct the start time if you started late, go past your goal without the timer “ending”, and see your eating window counted down. A Live Activity keeps the fast on your lock screen, for free.</p>"
                 "<p>All protocols, the Live Activity, 30 days of history and the export are free; Premium adds your full history, statistics and widgets. No account, no ads, and FastClear gives no medical advice.</p>"),
            ],
            "faq": [
                ("When does a 16:8 fast start?",
                 "With your last bite of food, not when you go to bed. If you finish dinner at 8 pm, your fast ends at noon the next day. If you forgot to start your timer, set the start to when you actually stopped eating."),
                ("Does black coffee break a fast?",
                 "No. Johns Hopkins Medicine lists water and zero-calorie drinks such as black coffee and tea as permitted during fasting periods. Milk, sugar or anything with calories ends the fast."),
                ("Does 16:8 fasting help you lose weight?",
                 "Not necessarily more than other ways of eating. In the TREAT trial (JAMA Internal Medicine, 2020), 12 weeks of eating between noon and 8 pm did not lead to significantly more weight loss than three meals a day. It can help some people structure their eating; what you eat still matters."),
                ("Do I have to fast every day?",
                 "No. Many people fast on weekdays and relax at weekends, or shift their window on social evenings. A rhythm you can keep is better than a perfect one you give up."),
            ],
        },
        "fr": {
            "title": "Jeûne intermittent 16:8 : quand commencer à compter, et ce qu'il fait vraiment",
            "seo_title": "Jeûne 16:8 : quand commencer à compter, ce qui rompt le jeûne",
            "desc": "Le jeûne 16:8 expliqué simplement : quand commencent les 16 heures, ce qu'on peut boire, comment choisir sa fenêtre, ce que montre vraiment la recherche, et qui ne doit pas jeûner.",
            "lede": "Le 16:8 est la forme la plus courante de jeûne intermittent : 16 heures sans manger, puis une fenêtre de repas de 8 heures. L'idée est simple ; c'est dans les détails qu'on bloque. Quand commence le jeûne ? Le café le rompt-il ? Et qu'est-ce qu'il fait vraiment ? Voici des réponses claires, y compris les moins enthousiasmantes.",
            "faq_title": "Les questions qu'on se pose",
            "sections": [
                ("Le 16:8 en une phrase",
                 "<p>On passe 16 heures sans manger, puis on mange dans une fenêtre de 8 heures, chaque jour ou les jours qu'on choisit. En pratique, la nuit fait l'essentiel du travail : si vous finissez de dîner à 20 h et remangez à midi, cela fait 16 heures.</p>"),
                ("Quand commencent les 16 heures",
                 "<p>Le jeûne commence à votre <strong>dernière bouchée</strong>, pas au coucher ni au moment où vous pensez à lancer un minuteur. Le sommeil compte. Si vous avez oublié de lancer votre minuteur, réglez simplement le début sur l'heure à laquelle vous avez vraiment fini de manger : c'est l'heure réelle qui compte, pas le bouton.</p>"
                 "<p>Rien de magique ne se produit à 16 h 00 min 00 s. Si un jour vous vous arrêtez à 15 heures, ou continuez jusqu'à 17, le jeûne compte quand même.</p>"),
                ("Ce qui rompt le jeûne, et ce qui ne le rompt pas",
                 "<p>Pendant les heures de jeûne, Johns Hopkins Medicine indique que l'eau et les boissons sans calories comme le café noir et le thé sont permises. L'eau gazeuse et les tisanes nature entrent dans la même catégorie.</p>"
                 "<p>Tout ce qui apporte des calories met fin au jeûne : le lait dans le café, le sucre, un jus, un en-cas, un smoothie. Les boissons aux édulcorants font débat ; pour rester simple, tenez-vous-en à l'eau, au café noir et au thé nature.</p>"),
                ("Choisir une fenêtre qui colle à votre vie",
                 "<p>La meilleure fenêtre est celle que vous pouvez tenir. Les options courantes :</p>"
                 "<ul>"
                 "<li><strong>De midi à 20 h :</strong> on saute le petit-déjeuner, on garde le dîner en famille. Le choix le plus courant.</li>"
                 "<li><strong>De 10 h à 18 h :</strong> un petit-déjeuner tardif et un dîner tôt.</li>"
                 "<li><strong>De 8 h à 16 h :</strong> pour les lève-tôt que des soirées légères ne gênent pas.</li>"
                 "</ul>"
                 "<p>La vie sociale compte : si le dîner du vendredi se termine tard, décalez la fenêtre ce jour-là plutôt que d'abandonner. La régularité aide plus que la perfection.</p>"),
                ("Ce que montre vraiment la recherche",
                 "<p>La réponse honnête est moins spectaculaire que ce que promettent beaucoup d'apps. Dans l'essai TREAT, publié en 2020 dans JAMA Internal Medicine, 116 adultes en surpoids ou en obésité ont été répartis au hasard entre manger seulement de midi à 20 h, ou prendre trois repas structurés par jour, pendant 12 semaines. Le groupe 16:8 a perdu environ 0,9 kg et le groupe repas environ 0,7 kg : la différence entre les deux n'était pas significative. Les auteurs ont conclu que restreindre la fenêtre de repas, seul, n'était pas plus efficace pour perdre du poids que manger tout au long de la journée.</p>"
                 "<p>Une revue publiée en 2019 dans le New England Journal of Medicine par Rafael de Cabo et Mark Mattson décrit des effets prometteurs du jeûne intermittent sur le métabolisme, dont beaucoup observés chez l'animal, alors que les essais chez l'humain ont surtout été de courte durée. Les délais qu'on voit parfois pour des « repères » comme la cétose ou l'autophagie viennent en grande partie de ce type de recherches : prenez-les comme des ordres de grandeur, pas comme des promesses.</p>"
                 "<p>Autrement dit, le 16:8 est un cadre. Il aide certaines personnes à manger plus régulièrement et à grignoter moins le soir ; ce que vous mangez dans la fenêtre compte toujours.</p>"),
                ("Qui ne devrait pas jeûner",
                 "<p>Johns Hopkins Medicine déconseille le jeûne intermittent aux enfants et adolescents de moins de 18 ans et aux personnes ayant un passé de troubles du comportement alimentaire, et avertit que les personnes avec un diabète de type 1 sous insuline risquent une hypoglycémie dangereuse pendant le jeûne. La grossesse et l'allaitement, qui augmentent les besoins en énergie, demandent l'avis de votre médecin ou de votre sage-femme. Si vous prenez un traitement régulier ou avez un problème de santé, parlez-en à votre médecin avant de commencer.</p>"),
                ("Un minuteur qui suit votre vrai rythme",
                 "<p><a href=\"/fr/fastclear/\">FastClear</a> est le minuteur de jeûne que je fais pour exactement ces détails. Vous pouvez corriger l'heure de début si vous avez lancé le minuteur en retard, dépasser votre objectif sans que le minuteur « s'arrête », et voir votre fenêtre de repas décomptée. Une Live Activity garde le jeûne sur l'écran verrouillé, gratuitement.</p>"
                 "<p>Tous les protocoles, la Live Activity, 30 jours d'historique et l'export sont gratuits ; Premium ajoute l'historique complet, les statistiques et les widgets. Sans compte, sans publicité, et FastClear ne donne aucun conseil médical.</p>"),
            ],
            "faq": [
                ("Quand commence un jeûne 16:8 ?",
                 "À votre dernière bouchée, pas au coucher. Si vous finissez de dîner à 20 h, votre jeûne se termine à midi le lendemain. Si vous avez oublié de lancer votre minuteur, réglez le début sur l'heure où vous avez vraiment arrêté de manger."),
                ("Le café noir rompt-il le jeûne ?",
                 "Non. Johns Hopkins Medicine indique que l'eau et les boissons sans calories comme le café noir et le thé sont permises pendant le jeûne. Le lait, le sucre ou tout ce qui apporte des calories met fin au jeûne."),
                ("Le jeûne 16:8 fait-il maigrir ?",
                 "Pas forcément plus qu'une autre façon de manger. Dans l'essai TREAT (JAMA Internal Medicine, 2020), 12 semaines à manger de midi à 20 h n'ont pas fait perdre significativement plus de poids que trois repas par jour. Il peut aider certaines personnes à structurer leur alimentation ; ce qu'on mange compte toujours."),
                ("Faut-il jeûner tous les jours ?",
                 "Non. Beaucoup de gens jeûnent en semaine et se relâchent le week-end, ou décalent leur fenêtre les soirs de sortie. Un rythme qu'on tient vaut mieux qu'un rythme parfait qu'on abandonne."),
            ],
        },
    },
]
