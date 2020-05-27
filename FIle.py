import re as op
import sys
import os

url = 'https://www.time4education.com/MoodlePages/catmttt/cat20materialvideos/'
ext = '.pdf'
with open("Sequence.txt", 'rt') as file_in:
    with open("Sequence_temp1.txt", 'wt') as wf:
        for new_line in file_in:
            line = op.sub(' ', '^', new_line)
            wf.write(line)
with open("Sequence_temp1.txt",'rt') as file_in:
    with open("Sequence_temp2.txt", 'wt') as wf:
        for new_line in file_in:
            line = op.sub('^', url, new_line)
            fine = op.sub('$', ext, line)
            wf.write(fine)
with open("Sequence_temp2.txt", 'rt') as file_in:
    with open("Sequence2.txt", 'wt') as wf:
        for new_line in file_in:
            fine = op.sub('.pdfhttps','https', new_line)
            wf.write(fine)
os.remove('Sequence_temp1.txt')
os.remove('Sequence_temp2.txt')


