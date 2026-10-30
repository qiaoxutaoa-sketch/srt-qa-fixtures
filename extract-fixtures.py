"""Restore the fictional SRT teaching pack; no network or third-party packages."""
import hashlib
import json
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    bundle = json.loads((here / 'fixture-bundle.json').read_text(encoding='utf-8'))
    if bundle.get('format') != 'donecove-srt-qa-text-bundle-v1':
        raise ValueError('Unrecognized bundle format')
    dest = here / 'srt-qa-kit-v1'
    if dest.exists():
        raise FileExistsError('Keep existing output safe: use a fresh folder')
    checked = []
    for entry in bundle['files']:
        path = Path(entry['path'])
        target = (dest / path).resolve()
        if path.is_absolute() or not target.is_relative_to(dest.resolve()):
            raise ValueError('Unsafe bundle path')
        data = entry['content'].encode('utf-8')
        if hashlib.sha256(data).hexdigest() != entry['sha256']:
            raise ValueError('Checksum mismatch: ' + entry['path'])
        checked.append((target, data))
    dest.mkdir()
    for target, data in checked:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    print(f'Restored {len(checked)} verified files to {dest.name}/')


if __name__ == '__main__':
    main()
