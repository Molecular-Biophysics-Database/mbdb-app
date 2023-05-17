import polib
import sys

pofile = polib.pofile(sys.argv[1])
entry: polib.POEntry
for entry in pofile:
    translation = entry.msgid.rsplit('/', maxsplit=1)[-1]
    suffix = translation.split('.')[-1]
    if suffix in ('help', 'hint'):
        continue
    if suffix == 'label':
        translation = translation[:-6]
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

pofile.save(sys.argv[1])
