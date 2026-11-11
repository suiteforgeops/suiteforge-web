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
]
