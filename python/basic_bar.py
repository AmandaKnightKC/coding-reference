#### bar graph

# --- 1. Setup -------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# (If you’re in a Jupyter notebook, uncomment the next line
#  so the plot appears under the cell.)
# %matplotlib inline

# --- 2. Sample data ------------------------------------------
data = pd.DataFrame({
    "name":  ["Alice", "Bob", "Carmen", "Dan"],
    "score": [85, 92, 78, 90]
})

# --- 3A. Bar chart with matplotlib ---------------------------
plt.figure(figsize=(6, 4))          # width, height in inches
plt.bar(data["name"], data["score"], width=0.6)
plt.title("Scores by Person")
plt.xlabel("Name")
plt.ylabel("Score")
plt.tight_layout()                  # prevent label cutoff
plt.show()

# --- 3B. Same chart with seaborn -----------------------------
plt.figure(figsize=(6, 4))
sns.barplot(x="name", y="score", data=data)
plt.title("Scores by Person (seaborn)")
plt.tight_layout()
plt.show()
