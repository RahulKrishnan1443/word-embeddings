
import numpy as np
import os

def np_list(file):
    with open(file, 'r') as i_file:
        read_data = i_file.read()
        i_file.seek(0)
        line = i_file.readline()
        key = read_data.split()
        offset = len(line.split())
    index = 0
    inter = 1
    start = 4
    o_file = open("noun_phrase.txt", 'w')
    noun_phrase = []
    for i in range(len(key)/offset):
        value = start + index * offset
        noun_phrase.append('')
        if (key[value] == 'DT') or (key[value] == 'WDT') or (key[value] == 'PDT') or (key[value] == 'PRP$') or (key[value] == 'PRP') or (key[value] == 'NNP') or (key[value] == 'NNPS') or (key[value] == 'JJ') or (key[value] == 'NNS') or (key[value] == 'CD') or (key[value] == 'NN') or (key[value] == 'CC'):
            for j in range(inter):
                noun_phrase[j] += key[start+index*offset - 1] + ' '
            index += 1
        elif (key[value] == 'IN'):
            inter += 1
            noun_phrase.append('')
            for j in range(inter):
                if (noun_phrase[j] != ''):
                    o_file.write(noun_phrase[j])
                    o_file.write("\n")
                    noun_phrase[j] += key[start+index*offset - 1] + ' '
            index += 1
        elif (key[value] == 'VBP') or (key[value] == 'JJR') or (key[value] == ',') or (key[value] == '``') or (key[value] == 'RP') or (key[value] == 'VBG') or (key[value] == 'WP') or (key[value] == 'MD') or (key[value] == 'TO') or (key[value] == 'VB') or (key[value] == 'VBD') or (key[value] == 'VBN') or (key[value] == 'VBZ') or (key[value] == "''") or (key[value] == ':') or (key[value] == 'RB') or (key[value] == '.'):
            for j in range(inter):
                if (noun_phrase[j] != ''):
                    o_file.write(noun_phrase[j])
                    o_file.write("\n")
                    noun_phrase[j] = ''
            index += 1
    o_file.close()

#   remove redundant lines from file

    lines_seen = set()
    outfile = open("np_list.txt", 'w')
    for line in open("noun_phrase.txt", 'r'):
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
