import os
import sys
from mido import MidiFile


def highlight_track(in_path, out_path, n, track_name):
  print(f"Converting {in_path} {track_name} -> {out_path}")

  mid = MidiFile(in_path, clip=True)
  # Remove piano tracks
  mid.tracks = [ t for t in mid.tracks if t.name != "Piano" ]

  for i, track in enumerate(mid.tracks):
    for msg in track:
      if n != i and msg.type == "note_on":
        new_velocity = int(msg.velocity * .40)
        msg.velocity = new_velocity

  mid.save(out_path)


def highlight_tracks(input_path):
  mid = MidiFile(input_path, clip=True)
  track_names = [track.name for track in mid.tracks]

  filenames = set()

  for i, track_name in enumerate(track_names):
    # Don't produce piano tracks
    if track_name == "Piano":
      continue
    dirname = os.path.dirname(input_path)
    filename = generate_filename(input_path, i + 1, track_name)

    output_path = os.path.join(dirname, filename)

    highlight_track(input_path, output_path, i, track_name)


def generate_filename(input_path, n, track_name):
    ext = ".mid"
    if input_path.endswith(ext):
      prefix = os.path.basename(input_path)[:-len(ext)]
    else:
      prefix = os.path.basename(input_path)

    suffix = " - %02d.%s.hl.mid"%(n, track_name)

    return prefix + suffix


def main():
  input_paths = sys.argv[1:]

  for input_path in input_paths:
    if not input_path.endswith(".hl.mid"):
      highlight_tracks(input_path)


if __name__ == "__main__":
  main()
