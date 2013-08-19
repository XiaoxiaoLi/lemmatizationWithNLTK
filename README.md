lemmatizationWithNLTK
=====================

Do lemmatization for each file in a folder using nltk in python.

<b>Prerequisite: </b>

installed the [NLTK python package] (http://nltk.org/install.html)

Downloaded the WordNet corpora by: `python -m    nltk.downloader all`


<b>To run:</b>

`python lemmatizationWithNLTK.py <input folder path> <output folder path>`

For example:

`python lemmatizationWithNLTK.py .\\inputData .\\outputData`

Why lemmatization and not stemming?
To quote [my Master's thesis](https://www.google.ca/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CDAQFjAA&url=http%3A%2F%2Fera.library.ualberta.ca%2Fpublic%2Fdatastream%2Fget%2Fuuid%3Aeb31a8b0-d7de-4042-8d36-e2bc8612ee60%2FDS1&ei=ktCoUcrDJamViAK0yoAQ&usg=AFQjCNGRDDSj7Cke-yuOhkrfHmW9-f6kBg&sig2=tWZqTJ3xPXDOLqWMy9hgOA&bvm=bv.47244034,d.cGE&cad=rjt):

> We lemmatize all the words to reduce the inﬂectional forms. English words usually have more than one form with the same semantic meanings, for example, car and cars. To reduce the forms to their base forms helps us in building the keyword graph and the community mining process later. Both stemming and lemmatization could achieve this goal. Many researches use stemming because it is easy to do. Stemming methods usually just chop off the end of words according to a set of brutal heuristics. Lemmatization, on the other hand, is more reasonable. It utilizes dictionaries and morphological information, aiming to remove only the inﬂectional endings rather than chopping a large part off from the words [50]. For example, the word large is stemmed to larg with the famous Porter Stemmer but it is kept intact with the WordNet Lemmatizer. Therefore, in this work we use the WordNet Lemmatizer provided with the Natual Language Toolkit (NLTK) 2 to get the lemma for each word. A lemma is usually the base form of a word, just like how the word would appear in a dictionary. We also store the original words along with their lemmas. At the post-processing stage discussed in Section 4.5.7, we transform the lemmas back to their most frequent original form so that they make more sense to the users [72].
