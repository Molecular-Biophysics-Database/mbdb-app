import polib
import sys

pofile = polib.pofile(sys.argv[1])
entry: polib.POEntry
processed_helps = set()

def process_translation(entry, translation):
    if '.enum.' in translation:
        translation = translation.split('.enum.')[-1]
    translation = translation.replace('_', ' ')
    if translation == '@v':
        translation = 'Version'
    elif translation == 'inchikey':
        translation = 'INCHI key'
    elif translation.lower() == 'mst':
        translation = 'MST'
    elif len(translation)>3:
        translation = translation.title()
    entry.msgstr = translation

for entry in pofile:
    translation = entry.msgid.rsplit('/', maxsplit=1)[-1]
    suffix = translation.split('.')[-1]
    if suffix in ('help', 'hint'):
        if suffix == 'help':
            processed_helps.add(translation.rsplit('.', maxsplit=1)[0] + ".label")
        continue
    if suffix == 'label':
        translation = translation[:-6]
    process_translation(entry, translation)

for entry in pofile:
    if entry.msgid in processed_helps:
        processed_helps.remove(entry.msgid)

for e in processed_helps:
    entry = polib.POEntry(
        msgid=e,
        msgstr='',
    )
    process_translation(entry, e[:-6])
    pofile.append(entry)

pofile.save(sys.argv[1])
pofile.save_as_mofile(sys.argv[1][:-2] + 'mo')
