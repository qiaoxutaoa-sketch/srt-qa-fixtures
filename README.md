# SRT QA fixtures

Nine tiny, fictional subtitle files for developers testing an SRT parser and for
video teams practicing a subtitle handoff. Each case has expected diagnostics,
an explanation and a passing control. No customer material or companion video
is included. These are sample materials, not the DoneCove product source code.

Published by the DoneCove team. The original sample pack is version 1.0.0,
released October 24, 2026; this repository provides the original sample contents in a
readable JSON bundle plus an exercise. An extraction helper restores the exact bytes.

## Start with one mistake

1. Open [the exercise](EXERCISE.md), then restore the sample files as described below.
2. Inspect the blank line between cues. Predict how many blocks your parser sees.
3. Check the files in your own parser, or in the
   [DoneCove SRT validator](https://subtitle.donecove.com/en/tools/srt-validator/).
4. Compare the result with the `manifest.json` inside the extracted pack. Its error codes
   and line numbers describe DoneCove's checker, not a universal SRT standard.
5. Change a copy, check again and keep the original for regression testing.

## What is in the pack?

| Case | Intended check | Expected result in the manifest |
| --- | --- | --- |
| Timestamp punctuation | Dot instead of comma | TIMESTAMP error |
| Missing blank line | Two intended cues merge into one parsed block | MISSING_SEPARATOR error |
| Duplicate number | Two cues use the same number | DUPLICATE_NUMBER error |
| Overlap | One cue starts before the previous one ends | OVERLAP warning |
| Structure-checked reference | Small passing control | No reported issues |
| End before start | Reversed time range | TIME_RANGE error |
| Empty dialogue | Cue has no text | EMPTY_TEXT error |
| Touching boundaries | Adjacent cues and two-language text | No reported issues |
| BOM and CRLF | UTF-8 BOM, Windows line endings, nonconsecutive numbers | No reported issues |

## Restore the files without an account

Download [fixture-bundle.json](fixture-bundle.json) and
[extract-fixtures.py](extract-fixtures.py) into the same local folder. Inspect
the helper, then run `python extract-fixtures.py` with Python 3.9 or later.
It restores `srt-qa-kit-v1/`, verifies each file's SHA-256 and refuses to overwrite
an existing output folder. It uses only Python's standard library and makes no
network request. No install or API key is needed.

The JSON stores the nine fictional SRT files plus the original README, manifest,
license and internal checksum list. Escaped CRLF and the UTF-8 BOM are restored
as their original bytes. The internal checksum list belongs to the extracted
folder. All expected diagnostics and repair instructions are in that folder's
README and manifest. You can also inspect those contents directly in the JSON.
The helper was checked against every original package file on October 31, 2026;
all 13 restored file hashes matched. That is a packaging check, not a test of
subtitle translation, player support or timing against media.

## Use it for a real handoff

For a course, game trailer or subtitle-group review, separate three questions:

- Does the file meet the receiving application's structural requirements?
- Does the translated text preserve the intended meaning and terminology?
- Does the caption appear at the right moment in the exact video cut?

This pack only helps practice the first question. A structure pass, a warning
count or a successful conversion cannot answer the other two. Check real output
in the target player and keep language review separate. A whole-file time shift
preserves overlaps; it is not an overlap repair.

## Reuse and provenance

See [LICENSE.txt](LICENSE.txt): the fictional examples and accompanying
explanations may be used, modified and redistributed, including commercially,
without a fee. Attribution is appreciated but not required. That permission
does not license DoneCove software, services, trademarks or third-party media.
There is no implied certification or endorsement of tools using these examples.

The [original resource page](https://subtitle.donecove.com/en/guides/srt-qa-test-kit/)
provides the downloadable release and product context. Repository documentation
was prepared with AI assistance and editorial review. No translation-accuracy,
latency, customer-use or player-compatibility claim is made.
