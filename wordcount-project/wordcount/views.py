from django.http import HttpResponse
from django.shortcuts import render 
import operator

def homepage(request):
	return render(request, 'home.html', {'yolo':'Burmese Cat'})

def count(request):
	fulltext = request.GET['fulltext']
	# print(fulltext) prints to terminal
	wordlist = fulltext.split()

	countdict = {}

	for word in wordlist:
		if word in countdict:
			#increase
			countdict[word] += 1
		else:
			#Add to dict
			countdict[word] = 1

	sortedwords = sorted(countdict.items(), key=operator.itemgetter(1), reverse=True)
	# print(sortedwords)
	return render(request, 'count.html', {'fulltext':fulltext, 'no_words':len(wordlist), 'sortedwords':sortedwords})

def about(request):
	return render(request, 'about.html')