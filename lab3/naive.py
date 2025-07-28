from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset
X = ["rainy day", "sunny day", "rainy and cold", "hot and sunny", "cold and dry"]
y = ["bad", "good", "bad", "good", "bad"]  # Labels

# Convert text to numeric features
vectorizer = CountVectorizer()
X_counts = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_counts, y, test_size=0.2, random_state=42)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
print("Predictions:", y_pred)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
