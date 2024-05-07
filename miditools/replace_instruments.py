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
	# input_path = sys.argv[1]
	# output_path = sys.argv[2]

	input_path = os.path.join(os.path.dirname(__file__), "..", "samples", "le dromadaire.mid")
	output_path = os.path.join(os.path.dirname(__file__), "..", "out.mid")

	replace_instruments(input_path, os.path.expanduser(output_path))


if __name__ == "__main__":
	main()
