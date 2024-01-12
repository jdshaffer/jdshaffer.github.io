# The Grammatical Complexity Analysis Tool (GCAT)
# by Jeffrey D. Shaffer
# v1.0 (2021)
#
# Takes in a txt file and saves an analysis to the file. Input and output files can
# be specified, or a default used
#       Default input : input.txt
#       Default output: results.txt
# Results include: average word length, average sentence length, part-of-speech
# counts, and a grammatical complexity score
##########################################################################################

import spacy

sentence_count = 0
noun_count = 0
pnoun_count = 0
verb_count = 0
adj_count = 0
adv_count = 0
prep_count = 0
token_count = 0
punct_count = 0
sym_count = 0
word_count = 0
space_count = 0
apostrophe_count = 0
character_count = 0

nlp = spacy.load('en_core_web_sm')

print("\nDo you wish to use a custom input filename? (Y/N)")
print("(ENTER defaults to input.txt)")
keyboard_answer = input()
if keyboard_answer == "Y" or keyboard_answer == "y":
    print("\nFilename to analyze?")
    print("(Double-check the path!): ")
    filename_to_analyze = input()
else:
    print("---> Using the default input file: input.txt")
    filename_to_analyze = "input.txt"


with open(filename_to_analyze, 'r') as text_input:
    # Count sentences by looking for all possible endings
    for line in text_input:
        if ". " in line:
            sentence_count += 1
        if ".\n" in line:
            sentence_count += 1
        if "? " in line:
            sentence_count += 1
        if "?\n" in line:
            sentence_count += 1
        if "! " in line:
            sentence_count += 1
        if "!\n" in line:
            sentence_count += 1
        if '" ' in line:  # Sentences that end with a " quote
            sentence_count += 1
        if '"\n' in line:
            sentence_count += 1
        if '“ ' in line:  # Sentences that end with a “ quote
            sentence_count += 1
        if '“\n' in line:
            sentence_count += 1
        if '” ' in line:  # Sentences that end with a ” quote
            sentence_count += 1
        if '”\n' in line:
            sentence_count += 1
        if ".)" in line:  # Comments are sentences, too!
            sentence_count += 1
        if "!)" in line:
            sentence_count += 1
        if "?)" in line:
            sentence_count += 1
        if '")' in line:
            sentence_count += 1

        # Count the parts-of-speech (POS)
        for token in nlp(line):
            token_count += 1
            for char in token.text:  # Count only ABCS and apostrophes that occur in words
                if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz’‘'":
                    character_count += 1
                if char in "’‘'":  # Apparently it's hard to catch the proper apostrophe...
                    apostrophe_count += 1
            if token.pos_ == "VERB":
                verb_count += 1
            if token.pos_ == "NOUN":
                noun_count += 1
            if token.pos_ == "PROPN":
                pnoun_count += 1
            if token.pos_ == "ADJ":
                adj_count += 1
            if token.pos_ == "ADV":
                adv_count += 1
            if token.pos_ == "ADP":
                prep_count += 1
            if token.pos_ == "PUNCT":
                punct_count += 1
            if token.pos_ == "SYM":
                sym_count += 1
            if token.pos_ == "SPACE":
                space_count += 1

            # Correct POS over-counting due to contractions and possessives being split in two
            if token.text == "’s" and token.pos_ == "PROPN":      # Don't count possessive "s" as pronoun
                pnoun_count -= 1
            if token.text == "'s" and token.pos_ == "PROPN":
                pnoun_count -= 1
            if token.text == "n’t":      # Don't count "n't" contraction as adverb
                adv_count -= 1
            if token.text == "n't":
                adv_count -= 1

            # print(token.text, token.pos_)     # <--- use for testing POS output


# Correcting our word count to remove the non-word tokens that the NLP parsed the text into
#  We also correct for the contractions & possessives that are split in two by "-apostrophe_count")
word_count = (token_count - punct_count - sym_count - space_count - apostrophe_count)


# SAVE RESULTS TO A FILE, TAB-SPACED FOR EASY PASTING INTO EXCEL
print("\nDo you wish to use a custom output filename? (Y/N)")
print("(ENTER defaults to results.txt)")
keyboard_answer2 = input()
if keyboard_answer2 == "Y" or keyboard_answer2 == "y":
    print("\nFilename to save?")
    print("(Double-check the path!): ")
    filename_to_save = input()
else:
    print("---> Using the default outputfile: results.txt.")
    filename_to_save = "results.txt"

with open(filename_to_save, 'w') as results_file:
    print("-----------------------------------------", file=results_file)
    print(character_count, "\tLetters", file=results_file)
    print(word_count, "\tWords", file=results_file)
    print(sentence_count, "\tSentences", file=results_file)
    print("\n-----------------------------------------", file=results_file)
    print("%005.2f" % ((character_count / word_count)), "\tLetters per word (avg)", file=results_file)
    if sentence_count != 0:       # Make sure we don't accidentally divide by zero
        print("%005.2f" % ((word_count / sentence_count)), "\tWords per sentence (avg)", file=results_file)
    print("\n-----------------------------------------", file=results_file)
    print((noun_count + pnoun_count), "\tNouns (incl names)", file=results_file)
    print(verb_count, "\tVerbs", file=results_file)
    print(adj_count, "\tAdjectives", file=results_file)
    print(adv_count, "\tAdverbs", file=results_file)
    print(prep_count, "\tPrepositions", file=results_file)
    print(pnoun_count, "\tNames", file=results_file)
    print(punct_count, "\tPunctuation marks", file=results_file)
    print("\n-----------------------------------------", file=results_file)
    print("%005.2f" % (((noun_count + pnoun_count) / word_count) * 100), "\t% of text are nouns", file=results_file)
    print("%005.2f" % ((verb_count / word_count) * 100), "\t% of text are verbs", file=results_file)
    print("%005.2f" % ((adj_count / word_count) * 100), "\t% of text are adjectives", file=results_file)
    print("%005.2f" % ((adv_count / word_count) * 100), "\t% of text are adverbs", file=results_file)
    print("%005.2f" % ((prep_count / word_count) * 100), "\t% of text are prepositions", file=results_file)
    print("%005.2f" % ((pnoun_count / word_count) * 100), "\t% of text are names", file=results_file)
    print("\n-----------------------------------------", file=results_file)
    if sentence_count != 0:       # Make sure we don't accidentally divide by zero
        print("%005.2f" % (((noun_count + pnoun_count) / sentence_count)), "\tAvg nouns per sentence", file=results_file)
        print("%005.2f" % ((verb_count / sentence_count)), "\tAvg verbs per sentence", file=results_file)
        print("%005.2f" % ((adj_count / sentence_count)), "\tAvg adjectives per sentence", file=results_file)
        print("%005.2f" % ((adv_count / sentence_count)), "\tAvg adverbs per sentence", file=results_file)
        print("%005.2f" % ((prep_count / sentence_count)), "\tAvg prep. per sentence", file=results_file)
        print("%005.2f" % ((pnoun_count / sentence_count)), "\tAvg names per sentence", file=results_file)




    ##########################################################################################
    # Calculate the Grammatical Complexity score
    ##########################################################################################
    if sentence_count != 0:       # Make sure we don't accidentally divide by zero
        anps = ((noun_count + pnoun_count) / sentence_count)
        avps = (verb_count / sentence_count)
        aadjps = (adj_count / sentence_count)
        aadvps = (adv_count / sentence_count)
        apps = (prep_count / sentence_count)

        jds_gc_score = ((anps + avps) + ((aadjps + aadvps) *2) + (apps * 3))

        print("\n-----------------------------------------", file=results_file)
        print("-----------------------------------------", file=results_file)
        print("Grammatical Complexity Score: ", jds_gc_score, file=results_file)
        print("", file=results_file)
    else:
        print("Could not calculate grammatical complexity score -- no complete sentences found.", file=results_file)

print("\Output successfully saved to file.")
