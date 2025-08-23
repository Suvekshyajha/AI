% ---------- DCG for simple English sentences ----------

% A sentence = noun phrase + verb phrase
sentence --> noun_phrase, verb_phrase.

% Noun phrase = article + noun
noun_phrase --> article, noun.

% Verb phrase = verb [+ noun phrase (optional)]
verb_phrase --> verb, noun_phrase.
verb_phrase --> verb.

% Articles
article --> [the].
article --> [a].

% Nouns
noun --> [cat].
noun --> [dog].
noun --> [man].
noun --> [woman].

% Verbs
verb --> [runs].
verb --> [sleeps].
verb --> [loves].
verb --> [sees].
