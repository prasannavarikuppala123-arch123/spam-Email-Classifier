from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = [
    "Win money now",
    "Free offer just for you",
    "Claim your free prize",
    "Lottery winner click now",
    "Meeting at 5pm",
    "Project submission tomorrow",
    "Team meeting scheduled",
    "Lunch at 1pm"
]

labels = [1,1,1,1,0,0,0,0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

test = [input("enter email message: ")]
test_vector = vectorizer.transform(test)

prediction = model.predict(test_vector)

if prediction[0] == 1:
    print("Spam Email")
else:
    print("Not Spam")