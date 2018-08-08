from __future__ import division


def np_list(file):
    with open(file, 'r') as i_file:
        read_data = i_file.read()
        i_file.seek(0)
        line = i_file.readline()
        key = read_data.split()
        offset = len(line.split())
    index = real_np = 0
    inter = 1
    start = 4
    left_bracket = right_bracket = 0

    new_left_bracket = 0
    new_right_bracket = 0
    left_bracket_seen = 0
    right_bracket_seen = 0
    precision = recall = f1_score = 0.0

    o_file = open("noun_phrase.txt", 'w')
    correct_o_file = open("correct_noun_phrase.txt", 'w')
    noun_phrase = []
    correct_noun_phrase = []
    for i in range(int(len(key)/offset)):
        left_bracket_seen = 0
        right_bracket_seen = 0
        new_left_bracket = 0
        new_right_bracket = 0
        for j in range(len(key[(index+1)*offset-1])):
            if key[(index+1)*offset-1][j] == '(':
                left_bracket_seen = 1
                left_bracket += 1
                new_left_bracket += 1
            elif key[(index+1)*offset-1][j] == ')':
                right_bracket_seen = 1
                right_bracket += 1
                new_right_bracket += 1

        if key[(index+1)*offset-1][j] == '-':
            if left_bracket - right_bracket != 0:
                for k in range(len(correct_noun_phrase)):
                    correct_noun_phrase[k] += key[index * offset + start - 1] + ' '
        elif (left_bracket_seen == 1) and (right_bracket_seen == 0):
            for k in range(new_left_bracket):
                correct_noun_phrase.append('')
            for k in range(len(correct_noun_phrase)):
                correct_noun_phrase[k] += key[index * offset + start - 1] + ' '
        elif (left_bracket_seen == 0) and (right_bracket_seen == 1) and \
                left_bracket - right_bracket != 0:
            for k in range(len(correct_noun_phrase)):
                correct_noun_phrase[k] += key[index * offset + start - 1] + ' '
            for k in range(len(correct_noun_phrase) - 1, len(correct_noun_phrase) -1 - new_right_bracket, -1):
                correct_o_file.write(correct_noun_phrase[k])
                correct_o_file.write("\n")
                correct_noun_phrase.pop()
        elif (left_bracket_seen == 0) and (right_bracket_seen == 1) and \
                (left_bracket - right_bracket == 0):
            for k in range(len(correct_noun_phrase)):
                correct_noun_phrase[k] += key[index * offset + start - 1] + ' '
                correct_o_file.write(correct_noun_phrase[k])
                correct_o_file.write("\n")
            for k in range(len(correct_noun_phrase)):
                correct_noun_phrase.pop()
        elif (right_bracket_seen == 1) and (left_bracket_seen == 1) and \
                (left_bracket - right_bracket == 0):
            correct_noun_phrase.append('')
            for k in range(len(correct_noun_phrase)):
                correct_noun_phrase[k] += key[index * offset + start - 1] + ' '
                correct_o_file.write(correct_noun_phrase[k])
                correct_o_file.write("\n")
            for k in range(len(correct_noun_phrase)):
                correct_noun_phrase.pop()
        elif (right_bracket_seen == 1) and (left_bracket_seen == 1) and \
                (left_bracket - right_bracket != 0):
            for k in range(new_left_bracket):
                correct_noun_phrase.append('')
            for k in range(len(correct_noun_phrase)):
                correct_noun_phrase[k] += key[index * offset + start - 1] + ' '
            for k in range(len(correct_noun_phrase) - 1, len(correct_noun_phrase) - 1 - new_right_bracket, -1):
                correct_o_file.write(correct_noun_phrase[k])
                correct_o_file.write("\n")
                del correct_noun_phrase[k]

        value = start + index * offset
        noun_phrase.append('')
        if (key[value] == 'DT') or (key[value] == 'WDT') or (key[value] == 'PDT') or (key[value] == 'PRP$') or (key[value] == 'PRP') or (key[value] == 'NNP') or (key[value] == 'NNPS') or (key[value] == 'JJ') or (key[value] == 'NNS') or (key[value] == 'CD') or (key[value] == 'NN') or (key[value] == 'CC'):
            for j in range(inter):
                noun_phrase[j] += key[start+index*offset - 1] + ' '
            index += 1
        elif (key[value] == 'IN') or (key[value] == 'HYPH') or \
                (key[value] == 'JJS') or (key[value] == 'WRB'):
            inter += 1
            noun_phrase.append('')
            for j in range(inter):
                if noun_phrase[j] != '':
                    o_file.write(noun_phrase[j])
                    o_file.write("\n")
                    noun_phrase[j] += key[start+index*offset - 1] + ' '
            index += 1
        elif (key[value] == 'VBP') or (key[value] == 'JJR') or \
                (key[value] == ',') or (key[value] == '``') or \
                (key[value] == 'RP') or (key[value] == 'VBG') or (key[value] == 'WP') or (key[value] == 'MD') or (key[value] == 'TO') or (key[value] == 'VB') or (key[value] == 'VBD') or (key[value] == 'VBN') or (key[value] == 'VBZ') or (key[value] == "''") or (key[value] == ':') or (key[value] == 'RB') or (key[value] == '.'):
            for j in range(inter):
                if noun_phrase[j] != '':
                    o_file.write(noun_phrase[j])
                    o_file.write("\n")
                    noun_phrase[j] = ''
            index += 1
    o_file.close()
    correct_o_file.close()

#   remove redundant lines from file

    lines_seen = set()
    outfile = open("np_list.txt", 'w')
    for line in open("noun_phrase.txt", 'r'):
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

#   check how many of the noun phrases (inferred) are actual noun phrases
#   (as indicated by the annotation in the file)

    for line in open("np_list.txt", 'r'):
        for c_line in open("correct_noun_phrase.txt", 'r'):
            if line == c_line:
                real_np += 1

#   count the number of correct noun phrases in the text file

    correct_np_count = len(open("correct_noun_phrase.txt", 'r').readlines())

    inferred_np_count = len(open("np_list.txt", 'r').readlines())

#   print "Actual noun phrases: " + str(real_np) + " Total # of actual noun
    # phrases: " + str(correct_np_count) + " Noun phrases computed: " + str(inferred_np_count)

    precision = round((real_np)/inferred_np_count, 2)
    recall = round(real_np/correct_np_count, 2)

#    print str(float(precision)*100) + "%"
#    print str(float(recall)*100) + "%"

    f1_score = 2*float(precision)*float(recall)/(float(precision) + float(recall))

    print "Precision: " + str(float(precision)*100) + "%." + " Recall: " + \
          str(float(precision)*100) + "%." + " F1 Score: " + \
          str(float(f1_score)*100) + "%."