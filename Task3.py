import spacy
import wikipedia     #for fetching from wikipedia

nlp=spacy.load("en_core_web_sm")#load the NLP model by spacy

def wiki_ans(question):
    doc=nlp(question)    #it intakes the user input which to be specific

    topic=[chunk.text for chunk in doc.noun_chunks
           if chunk.root.pos_ in ["NOUN","PROPN"]]  #it extracts Phrases and nouns like Mumbai
    if not topic:
        return "Please be Specific about your explanation. "#if no Phrase present in wikipedia

    try:
        return wikipedia.summary(topic[0],sentences=4,auto_suggest=False)#using try to fetch topics

    except wikipedia.exceptions.DisambiguationError as e:   #handle multiple answer case
        return "Multiple Matches Found. Query to be more specific. "

    except wikipedia.exception.PageError:      #Handle page not found case
        return "Cannot find information about specified Topic! "

    except Exception as e:                    #handle other not specified cases
        return f'Error:{str(e)}'

while True:
    userInput=input("\n You:  ")        #fetch user query

    if userInput.lower() in ['exit','quit']:  #exit the chatbot
        print("Achoo Bot: Sayonara !!!")
        break
    print("Achoo Bot: ",wiki_ans(userInput))   #here it will return the answer if found or error if occured
