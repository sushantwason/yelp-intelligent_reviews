
from collections import defaultdict
from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten,kmeans2
import math


def dataCleaning(doc):
    #Removing Multiple white spaces anywhere in the string, permanently
    doc=' '.join(doc.split())    
    return doc

# Computes the starting location/index of each word and sentence within the string and returns the same in a list
def dataPreProcessing(doc,query):
    wordStartingIndex=getWordStartingLocation(doc)
    wordStartingIndex.append(len(doc)) #Including the last word
    sentenceStartingLocation=getSentenceStartingLocation(doc)
    sentenceStartingLocation.insert(0,0) #Including the first sentence
    return wordStartingIndex,sentenceStartingLocation

# returns an list of indices of the position where the sentence starts, identified by a period mark.
def getSentenceStartingLocation(doc):
    return [sentenceStartIndex for sentenceStartIndex, ltr in enumerate(doc) if ltr in ['.']]

# returns an list of indices of position of starting of each word, tokenizes by an empty char (' ')
def getWordStartingLocation(doc):
    return [wordStartIndex for wordStartIndex, ltr in enumerate(doc) if ltr in [' ']]


# locates each query 'word' with the wordIndex in the original doc string, and associates the findings with a priority number
# e.g: [" deep","dish","pizza"] in " ---deep dish pizza--- tastes very good in the ---pizza deep--- when the ---pizza--- is ---deep---"
# priority of deep dish pizza is 3, pizza deep is 2,  pizza is 1 , deep is 1 
#priority = no. of consecutive words in doc that are present in the query list
# so, here deep dish pizza will have the same priority as pizza deep dish ( order doesnt matter)    

#Input: 1. the doc to be reviewed, query list by the user, and 2. a list of word starting location indices
#Output: 1. a dictionary with key as the priority number, and the value as the starting location of where the query word/set of words is/are found in the string
#        2. a list of starting location of where the query parameters were found in the doc string
#        3. a dictionary containing the the indices as the key and lengths of the keywords/set of keywords at each starting location as the value

def findSubString(doc,query,wordIndex):
    storeIndexPriority = defaultdict(list) 
    storeLength=defaultdict() 
    start=0
    i=0
    priority=0
    keywordIndexArray=[]
    totalLength=0  
    while i < len(wordIndex): # for each word in the doc string
        end=wordIndex[i] 
        wordToSearch=doc[start:end].lower()  #converting the word to be scanned to lower case, to avoid discrepencies while comparing 
        if wordToSearch[-1:] in [',','.','-'] :
            wordToSearch=wordToSearch[:-1] # removing the comma, period and other char from the word ,e.g: deep, ==> deep
        if wordToSearch in query or wordToSearch[:-1] in query or wordToSearch[:-2] in query: #Keyword Found in the doc!!!!, also making room for error, e.g: pizzas is same as pizza,(simgular, plural) 
            if priority==0: # first word
                priorityStart=start
            totalLength+=len(wordToSearch)+1
            priority=priority+1  #increase priority by 1, every time a word is found
        else:
            if priority!=0: # the consecutive chain ends, find out where, and store the essentials
                storeIndexPriority[priority].append(priorityStart) 
                keywordIndexArray.append(priorityStart)
                storeLength[priorityStart]=totalLength
                priority=0
                totalLength=0
        start=end+1
        i=i+1  
    #Corner Case, the last keyword set, or the word to be found is computed here  
    if priority!=0:
        storeIndexPriority[priority].append(priorityStart)
        keywordIndexArray.append(priorityStart)
        storeLength[priorityStart]=totalLength
    return storeIndexPriority,array(keywordIndexArray),storeLength

# Calculates the weight of members of each cluster computed by k-means, in order to prioritize 
def calculateWeight(values,d):
    weight=0
    for item in values:
        for key in d.iterkeys():
            if item in d[key]:
                weight=weight + key #priority=no. of consecutive words
    return weight,values
    
#Prioritize, select the cluster with maximum weight, and returns a list with the stored keywords
def prioritize(clusterMembers,d):
    max_weight=0
    highlighted_text_positioning=[]
    for key in clusterMembers.iterkeys():
        weight,values=calculateWeight(clusterMembers[key],d)
        if weight>max_weight:
            max_weight=weight
            highlighted_text_positioning=values
    return highlighted_text_positioning

#Calculates clusters, and assigns membership based on proximity

def kmeans_calculation(arrayToCluster):
    if len(arrayToCluster)==1:
        return None,[0]
    whitenArray=whiten(array(arrayToCluster))
    #The best K- Selection strategy; an alternative was to pick sqrt(no. of elements/2), PCA cannot be applied here, as the data is one dimensional
    if len(arrayToCluster)<7:
        k=1
    elif len(arrayToCluster <10):
        k=2
    else:
        k=3
    centroid,label=kmeans2(whitenArray,k,10)
    return centroid,label
    
#Function that finds the indices of the starting sentence just before the first keyword finally selected, and the ending indices of the sentence just after the final keyword finally selected
def findStartingEndingSentence(start,end,sentenceStartingIndex,highligted_text):
    firstVal=prevStart=highligted_text[0]
    lastVal=prevEnd=highligted_text[-1]
    for item in sentenceStartingIndex:
        if item > firstVal:
            break
        else:
            prevStart=item
    for item in reversed(sentenceStartingIndex):
        if item < lastVal:
            break
        else:
            prevEnd=item
            
    return prevStart,prevEnd 
    

#Displays the short review, with the keywords being highlighted
#Input: the document, starting indices of the final cluster that was selected and deemed to be the max weight group,length of keywords, list containing indices of starting of each new sentence
#Output the shortened review
def displayShortenedReview(doc,highlighted_text_positioning,storeLength,sentenceStartingindex):
    startHighlight=" [[HIGHLIGHT]] "
    endHighLight=" [[ENDHIGHLIGHT]] "
    #To Look like a complete sentence, find the previous starting sentence from the first keyword, and the next sentence end from the last keyword
    
    startPoint,endPoint=findStartingEndingSentence(highlighted_text_positioning[0],highlighted_text_positioning[-1],sentenceStartingindex,highlighted_text_positioning)
    
    endPointer=highlighted_text_positioning[0]
    shortReview=doc[startPoint:endPointer] # beginning of the sentence till the first keyword
    startFlag=True
    for startPointer in highlighted_text_positioning:
        if startFlag==True:
            startFlag=False
        else:
            shortReview+=doc[endPointer:startPointer]
        shortReview+=startHighlight
        endPointer=startPointer+storeLength[startPointer]
        shortReview=shortReview+doc[startPointer:endPointer]+endHighLight
    shortReview+=doc[endPointer:endPoint]# beginning of the last keyword till the end of last sentence
    return shortReview



#The main program that does all the computation, prints the shortened review, and returns True of the test case succeeded, else false
def highlightDoc(doc,query):
    #converting the query parameters to lower case for string matching
    query= map(lambda x:x.lower(),query) 
    wordStartingIndex,sentenceStartingIndex=dataPreProcessing(doc,query)
    clusterMembers=defaultdict(list)
    d,keywordIndexArray,storeLength=findSubString(doc,query,wordStartingIndex)
    #The Query Parameter was not found in the document, just print this for now, may be skip this review, and move on to the next one!
    if len(keywordIndexArray)==0:
        print "No Match"
        return True
    #Cluster the members( keywords indices that were found in the document) into groups
    centroid,label=kmeans_calculation(keywordIndexArray)
    #Store the cluster members with the corresponding cluster if in a dictionary
    for i in range(0,len(label)):
        clusterId=label[i]
        clusterMembers[clusterId].append(keywordIndexArray[i])
    #Select the final Cluster based on weight, and store its members in a list
    highlighted_text_positioning=prioritize(clusterMembers,d)
    #Display the short review
    print displayShortenedReview(doc,highlighted_text_positioning,storeLength,sentenceStartingIndex)
    return True


def main():
    '''To Yelp Employees:
        If you want to check any test case, please make sure to add \" and \', escape characters for any quotation symbols within the string '''
    
    doc="deep dish pizza is the deep of the deep dish in the pizza"
    doc=dataCleaning(doc)
    query=["deep","dish","pizza"]
    query= map(lambda x:x.lower(),query)    
    print highlightDoc(doc,query)
    
        
if __name__ == "__main__":
    main()