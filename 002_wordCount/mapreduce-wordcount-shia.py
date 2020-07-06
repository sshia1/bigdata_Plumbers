# John Shia, 07/05/2020, BigData programming assignment #1
#
# Simulate Hadoop MapReduce algorithm in Python, doing word count on Shakespeare.txt
#
# data_source              = file_read(data_file, start_line, end_line)...file=>list of string, terminated by '\n'
# record_stream            = TextInputFormat(data_source).................init stream of kvp=(index, line$)
# intermediate_data        = mapper(record_stream)........................stream of tokens: kvp=(word, 1)
# intermediate_data        = partitioner(intermediate_data)...............return output=input since only 1 mapper function
# sorted_intermediate_data = shuffle_and_sort(intermediate_data)..........sort intermediate data by key
# final_data               = reducer(sorted_intermediate_data)............final output: dictionary of word count
#
# CAVEAT: de-pluralization is implemented on a very limited scale, using dictionary
#


data_file = "Shakespeare.txt"
start_line = 0  # for debugging purpose, process only in the range of start_line to end_line
end_line = 0  # for debugging purpose, if end_line <= start_line, return entire file


def file_read(data_file, start_line, end_line):
    #   return list of string read from file "data_file"
    #   start_line, end_line are for debugging purpose
    #   if start_line < end_line, then contents only from start_line to end_line-1 are read & returned

    f = open(data_file, "r")
    full_raw_data = f.readlines()
    f.close()
    if (end_line > start_line):
        partial_raw_data = full_raw_data[start_line:end_line]
    else:
        partial_raw_data = full_raw_data
    return (partial_raw_data)


def TextInputFormat(data_stream):
    #   convert list of strings terminated by '\n' to
    #   format of list of kvp=(line_no, line_string)

    list_of_records = []
    line_no = 0
    for line in data_stream:
        list_of_records.append((line_no, line))
        line_no += 1
    return (list_of_records)


def mapper(records):
    #   convert list of kvp=(line_no, line_string) to list of (token, [1]) & return it
    #
    #   tokenization():      create tokens, using space as delimiter
    #   caseNormalization(): convert everything to lower case
    #   stripPunctuation():  get rid of comma, exclamation mark, question mark, period
    #   stemming():          get rid of possessives, pluralization (getting rid of pluralization not implemented)
    #   letters():           check to see if the string is all letters or not
    #   depluralization():   converts plural to singular, very limited dictionary size

    def remove_punctuation(s):
        s2 = s
        if ("." in s):
            s2 = s.replace(".", "")
        if ("!" in s):
            s2 = s.replace("!", "")
        if ("?" in s):
            s2 = s.replace("?", "")
        if ("," in s):
            s2 = s.replace(",", "")
        return (s2)

    def remove_possessive(s):
        s2 = s
        if ("'s" in s):
            s2 = s.replace("'s", "")
        return (s2)

    def depluralization(plural):
        #       get rid of extra 's' at end & map it to word version which doesn't have 's'
        plural_list1 = {"etexts": "etext", "cdroms": "cdrom", "works": "work", "editions": "edition",
                        "versions": "version"}
        plural_list2 = {"releases": "release", "implications": "implication", "copies": "copy", "charges": "charge"}
        plural_list3 = {"volunteers": "volunteer", "computers": "computer", "conditions": "condition",
                        "donations": "donation"}
        plural_list4 = {"humans": "human", "hundreds": "hundred", "includes": "include", "letters": "letter",
                        "sizes": "size"}
        plural_list5 = {"users": "user", "titles": "title", "sources": "source", "fails": "fail", "files": "file",
                        "readers": "reader"}
        plural_list6 = {"scrambles": "scramble", "abjects": "abject", "abodements": "abodement",
                        "abortives": "abortive"}
        plural_list7 = {"abatements": "abatement", "abates": "abate", "abbeys": "abbey", "abhors": "abhor",
                        "abides": "abide"}
        plural_list8 = {"abominations": "abomination", "abstains": "abstain", "abuses": "abuse", "academes": "academe"}
        plural_list9 = {"accepts": "accept", "accites": "accite", "accidents": "accident", "accords": "accord"}
        plural_list10 = {"accomplices": "accomplice", "accounts": "account", "accuses": "accuse",
                         "accusations": "accusation"}
        plural_list11 = {"achievements": "achievement", "aches": "ache", "accoutrements": "accoutrement"}
        plural_list12 = {"accommodations": "accommodation", "achieves": "achieve", "accusers": "accuser"}
        singular = plural
        if (plural in plural_list1):
            singular = plural_list1[plural]
        if (plural in plural_list2):
            singular = plural_list2[plural]
        if (plural in plural_list3):
            singular = plural_list3[plural]
        if (plural in plural_list4):
            singular = plural_list4[plural]
        if (plural in plural_list5):
            singular = plural_list5[plural]
        if (plural in plural_list6):
            singular = plural_list6[plural]
        if (plural in plural_list7):
            singular = plural_list7[plural]
        if (plural in plural_list8):
            singular = plural_list8[plural]
        if (plural in plural_list9):
            singular = plural_list9[plural]
        if (plural in plural_list10):
            singular = plural_list10[plural]
        if (plural in plural_list11):
            singular = plural_list11[plural]
        if (plural in plural_list12):
            singular = plural_list12[plural]
        return (singular)

    data = []
    for record in records:
        word_list = record[1].split()
        for word in word_list:
            w = word.lower()  # convert to lower case
            w = remove_punctuation(w)
            w = remove_possessive(w)
            if w.isalpha():
                w = depluralization(w)
                data.append((w, 1))
    return (data)


def partitioner(intermediate_data):
    #   dummy function, just return input since only 1 mapper()
    return (intermediate_data)


def shuffle_and_sort(data):
    #   return sorted input data
    return (sorted(data))


def reducer(data_in):
    #   data_in: list of kvp=(token, [1])
    #   data_out: return dictionary where kvp=(token, total_count_per_token)

    data_out = {}
    for d in data_in:
        key = d[0]
        value = d[1]
        if (key in data_out):
            data_out[key] = data_out[key] + value
        else:
            data_out[key] = value
    return (data_out)


data_source = file_read(data_file, start_line, end_line)
record_stream = TextInputFormat(data_source)
intermediate_data = mapper(record_stream)
intermediate_data = partitioner(intermediate_data)
sorted_intermediate_data = shuffle_and_sort(intermediate_data)
final_data = reducer(sorted_intermediate_data)

print("FINAL_DATA:")
print(final_data)
