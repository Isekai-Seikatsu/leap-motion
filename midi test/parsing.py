from mido import MidiFile
mid = MidiFile('Hikaru Nara.mid')
print mid.ticks_per_beat
print mid.type, mid.length
print len(mid.tracks)
#for track in mid.tracks:
for i in mid.tracks[1]:
    print i
    #print i.type, i.tempo, i.time
'''
    if i.type=='note_on':
        print i.note, i.velocity, i.time'''
