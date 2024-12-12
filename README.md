# Files
amznotes.ipynb
    kindle vocab highlights 

# Workflow
- raw *list of words*
    - can have nltk process if just raw text
- check words against deck in anki
- process new kanji
- process new words
    - to add (not in deck)
        - auto create with jisho api
    - to learn (in deck)





# JP STANDARD FIELDS
WORD -> needed, can automate
FURIGANA -> needed, automate????
    bad (search):
        加わる
        加[くわ]わる
    good: 
        加わる
        加わる[くわわる]
MEANING -> needed, can automate
unihan -> DROP, can be automated in future ???
    why important: two kanji words, easier to remember the kanji if reminded kanji meaning
    why not: should remember what both mean anyways??
        could always search if not remembered...
frequency -> DROP, new cards don't need this
hint -> drop
example -> drop
pitch accent -> drop, generateable
tags -> drop, too hard not used often enough anyways
    three important tags: homophone, verb, kana



distinciont between common and topic? 
    -> just dump into topic first...
    and move to common if think common


# newer process?
could be semi automated with API
combine jisho.ipynb and anki-tool.ipynb






=========================
# PROCESS EASY
=========================
1. get vocab list (amznotes.ipynb, etc)
2. process list and create cards (anki-tool.ipynb)
    - 