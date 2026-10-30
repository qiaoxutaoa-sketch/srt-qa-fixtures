# Exercise: a passing-looking file can hide a missing cue boundary

Audience: a developer reviewing parser behavior, or a subtitle team checking an
export before it goes back into a course or video project. Use fictional samples
first; do not upload confidential subtitles to an unfamiliar service.

## Predict before running

Restore the bundle using the README instructions, then open these two files
inside srt-qa-kit-v1 without editing them:

- `samples/srt-example-missing-blank-line.srt`
- `samples/srt-example-structure-checked.srt`

Look just before the second cue number. Is there an empty separator line?
Write down the number of intended cues and the number of blocks your parser
actually returns. These need not be the same.

## Observe the diagnostic

Run your parser or the validator linked in the README. The DoneCove manifest
expects one parsed block and a MISSING_SEPARATOR error at line 5 for the broken
file. It expects two cues and no reported issues for the reference. Other
parsers may reject the file or recover differently; document that difference
rather than treating our diagnostic names as mandatory behavior.

## Make one change

Copy the broken file. Insert one blank line before cue number 2. Run the check
again and inspect every text line and both time ranges. Do not accept a reduced
error count as proof that both dialogue lines survived. Keep the broken original
as a regression fixture.

## Add a second reviewer decision

Open `samples/srt-example-overlapping-cues.srt`.
Its first cue ends at 4 seconds and the second starts at 3 seconds. That is a
one-second overlap. The manifest expects zero errors and one warning, so a
structure pass can coexist with a timing issue requiring human review.

Both intentional simultaneous speech and accidental collisions can create an
overlap. This pack has no audio or video, so it cannot tell you which occurred.
Moving both cues by +1 second preserves their overlap. Retiming individual cues
requires the actual media and the receiving platform's caption requirements.

## Handoff note to keep

Record the video filename/version, SRT filename, checker's version/date,
diagnostics before and after the edit, and who reviewed meaning and playback.
For real work, inspect the beginning, middle, end and each edited section in the
target player. Passing this exercise does not certify a real subtitle file.
