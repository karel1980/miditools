import os
import sys
from mido import MidiFile


def highlight_track(in_path, out_path, track_name):
	print(f"Converting {in_path} {track_name} -> {out_path}")

	mid = MidiFile(in_path, clip=True)

	for i, track in enumerate(mid.tracks):
		for msg in track:

			if track.name != track_name and msg.type == "note_on":
				new_velocity = int(msg.velocity * .30)
				msg.velocity = new_velocity

	mid.save(out_path)


def highlight_tracks(input_path):
	mid = MidiFile(input_path, clip=True)
	track_names = [track.name for track in mid.tracks]

	for track_name in track_names:
		dirname = os.path.dirname(input_path)
		ext = ".mid"
		if input_path.endswith(ext):
			filename = os.path.basename(input_path)[:-len(ext)] + f" - {track_name}.hl.mid"

		output_path = os.path.join(dirname, filename)
		highlight_track(input_path, output_path, track_name)


def main():
	input_paths = sys.argv[1:]

	for input_path in input_paths:
		if not input_path.endswith(".hl.mid"):
			highlight_tracks(input_path)


if __name__ == "__main__":
	main()
