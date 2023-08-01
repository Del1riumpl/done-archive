import mido
from mido import MidiFile, MidiTrack, Message

def pitchconv(pitch):
    return int(round(1193180.0 / (2**((pitch - 69) / 12.0) * 440), 0))

def convert_midi_to_mido(input_file, output_file):
    mid = MidiFile(input_file)
    out = MidiFile()

    track = MidiTrack()
    out.tracks.append(track)

    b = 0
    d = 0

    for event in mid.tracks[0]:  # Assuming you are working with the first track
        if event.type == 'note_on':
            if event.velocity == 0:
                d += int(round(event.time / 48.0, 0))
                p = pitchconv(event.note)
                msg = Message('note_off', note=p, time=d)
                track.append(msg)
                b = 0
            else:
                d = int(round(event.time / 48.0, 0))
                p = pitchconv(event.note)
                msg = Message('note_on', note=p, velocity=event.velocity, time=d)
                track.append(msg)

    out.save(output_file)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script.py input_midi_file output_midi_file")
    else:
        convert_midi_to_mido(sys.argv[1], sys.argv[2])
