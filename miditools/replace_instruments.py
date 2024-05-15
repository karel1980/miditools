import os
import sys
from mido import MidiFile


def replace_instruments(in_path, out_path):
  print(f"Replacing instruments in {in_path}")

  mid = MidiFile(in_path, clip=True)

  for i, track in enumerate(mid.tracks):
    for msg in track:
      if msg.type == "program_change":
        msg.program = 0

  mid.save(out_path)


def main():
  if len(sys.argv) != 3:
    print(f"usage: {sys.argv[0]} infile outfile")

  input_path = sys.argv[1]
  output_path = sys.argv[2]

  replace_instruments(input_path, os.path.expanduser(output_path))


if __name__ == "__main__":
  main()
