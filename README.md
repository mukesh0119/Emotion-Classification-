# Emotion-Classification-

The dataset provided is known for its use in sentiment analysis and is made up of more than 54,000 Reddit comments that have been categorised into 28 different emotional categories. I used Natural Language Processing (NLP) methods to analyse and classify the emotions presented in the text data.

## Selected Model: SVM
For the given dataset the SVC model performs better compared to the other models.
Random forest was also considered but using Random forest classifiers has few drawbacks such as lack of exploration, as it fails to explore more data other than the training data.
After comparing the models, I made the decision of going ahead with SVM model. There are many factors to consider while fitting the model with the selected dataset. There are various hyperparameters to taken into consideration for training the model. Firstly, I've used both count vectorizer and Tf-id vectorizer. But while using the model for the dataset I decided to go with the Tf-id Vectorizer, the major reason for this is because, the Tf-id vectorizer takes in consideration the frequency of words in the document with the rarity of it in the entire corpus.

## Building Web service
Using Python, I've decided to build Web Service of the SVM model analysis using Flask application. For the front end of web service, I have used HTML and CSS for styling.

In this first page, the user can enter a sentence in the given input box and when classify is pressed, it redirects the user to the next page, where the emotions what is shown in the sentence is classified and the result is displayed.

When then input is got is received from the user in the front end, it gets passed to the backend of the developed system and the received text is passed to the analysis code where I have used SVM and the analysis gets done and the output (label) gets passed again to the front end through Flask api and the results gets displayed in the results page.

## Audit :
For the basic monitoring feature which stores the data the user has checked, I have built it programmatically and included using a json file in the directory, when every time the user uses the service, the file stores the sentence that was given as input, predicted class, emotions, the date at which it was checked and the time at which it was checked.


