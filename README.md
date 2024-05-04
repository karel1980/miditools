# Miditools

There's only one tool for now, which takes midi files as input, and splits them one file per track.
Each produced file contains all tracks, but one track is louder than the others. 

You'll have to install it yourself since it's not published to pypi.

Installation

    pip install -r requirements.txt
    python setup.py develop --user

Example usage

    mt-highlight-tracks some_midi.mid


