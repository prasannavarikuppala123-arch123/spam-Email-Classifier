from tkinter import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
emails = [
    "Win money now",
    "Free offer just for you",
    "Claim your free prize",
    "Meeting at 5pm",
    "Project submission tomorrow"
]

labels = [1,1,1,0,0]

# Model training
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

# Function
def check_email():
    message = entry.get()

    test = vectorizer.transform([message])
    prediction = model.predict(test)

    if prediction[0] == 1:
        result.config(text="Spam Email")
    else:
        result.config(text="Not Spam")

# GUI Window
root = Tk()
root.title("Spam Email Detector")
root.geometry("400x300")

label = Label(root, text="Enter Email Message")
label.pack(pady=10)

entry = Entry(root, width=40)
entry.pack(pady=10)

button = Button(root, text="Check", command=check_email)
button.pack(pady=10)

result = Label(root, text="")
result.pack(pady=20)

root.mainloop()