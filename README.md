# Midi-tools

This repository contains two tools, `mt-highlight-tracks` and `mt-replace-instruments`

## Installation

    pip install -r requirements.txt
    pip install -e .

## Tools

### mt-highlight-tracks

mt-highlight-tracks takes a midi file and splits it into one file per track.
In each of these files the are quieter, except for one.

Example usage:

    mt-highlight-tracks some_midi.mid [...]

The resulting filenames would be (for example):

    - `some_midi - Soprano.hl.mid`
    - `some_midi - Alto.hl.mid`
    - `some_midi - Tenor.hl.mid`
    - `some_midi - Bass.hl.mid`

The tool will *not* work on files called "*.hl.mid" to avoid accidents.

### mt-replace-instruments

In progress. This tool will change instruments in a midi file.

Example usage:

    mt-replace-instruments some_midi.mid output.mid

