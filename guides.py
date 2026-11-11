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
]
