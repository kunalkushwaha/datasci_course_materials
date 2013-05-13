import sys

def hw(sent_file,tweet_file):
    print '.. Analysing the data ...\n'
    afinnfile = sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
	    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	    scores[term] = int(score)  # Convert the score to an integer.

#    print scores.items() + '\n' # Print every (term, score) pair in the dictionary)
    
    for tweet in tweet_file:
	    tweet_score = 0
	    text_start_offset = tweet.find("text") # extract the start position of text + 6
	    text_end_offset = tweet.find("source") # extract the end position of text - 2
	    print '\n' +tweet[text_start_offset+6:text_end_offset-2]
	    tweet_text = tweet[text_start_offset+6:text_end_offset-2].split()
	    for word in tweet_text :
		    tweet_score = tweet_score + scores.get(word,0) #cacluate the tweet score
	    print "tweet-score " +  str(tweet_score)


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
