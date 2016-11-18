#use variable blueDuration for duration from blue
#use variable userConfigDir for user's .blue dir
#use variable blueLibDir for blue's lib directory
#use variable blueProjectDir for this project's directory
#use variable score at end of script to bring score back into blue
from composition.itemstream import Itemstream
from composition.score import Score


#IdMusic1.wav 
# ['h',.769], ['h',1.95], ['w'], 3.175], ['h',5.54], ['h'], 6.67], ['w'], 8.0]

# rhythms = Itemstream(['e.','e.','e','q.','e','q.','e','h'],'sequence', tempo=[120,60,30])
rhythms = Itemstream(['q'],'sequence', tempo=[120,60,30])
rhythms.notetype = 'rhythm'
amps = Itemstream([1])

pitches = Itemstream(sum([
    ['c4','c','c','d','c5','c','c','d'],
    ],[]))
#pitches.streammode = 'heap'
pitches.notetype = 'pitch'
s = Score(rhythms,[amps,pitches], note_limit=(len(pitches.values)*2))
s.gen_lines = [';sine\n','f 1 0 16384 10 1\n',';saw','f 2 0 256 7 0 128 1 0 -1 128 0\n',';pulse\n','f 3 0 256 7 1 128 1 0 -1 128 -1\n']
s.durstream = Itemstream([.1])
s.instr = 3
#s.generate_score("/Users/benmca/Documents/src/sandbox/python/test.sco")
#s.generate_score()
s.generate_notes()

output = ""
for x in range(len(s.gen_lines)):
    output += s.gen_lines[x]
for x in range(len(s.notes)):
    output += s.notes[x]
    
rhythms = Itemstream(['e']*12,'sequence', tempo=[120,60,30])
#rhythms = composition.itemstream.itemstream(['e.','e.','e'],'heap', tempo=240)
rhythms.notetype = 'rhythm'
s.rhythmstream = rhythms
pitches = Itemstream(sum([
    ['fs6'],
    ],[]))
pitches.notetype = 'pitch'
s.streams[1] = pitches
s.note_limit = 32
#reset time
s.starttime = 0.0
s.curtime = s.starttime
#for x in s.notes:
    #print(x)
s.instr = 3
s.generate_notes()
for x in range(len(s.notes)):
    output += s.notes[x]

print(output)
    
s.generate_score("test.sco")
#score  = s.generate_score_string()
