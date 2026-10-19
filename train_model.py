import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("data.csv")
print(df["thal"].unique()) 

# Show data (optional check)
print(df.head())

# Split features and target
X = df.drop("target", axis=1)
y = df["target"]

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model (better than basic models)
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)
print("✅ Accuracy:", accuracy)

# Save model
joblib.dump(model, "model.pkl")

print("🎉 Model trained and saved as model.pkl")