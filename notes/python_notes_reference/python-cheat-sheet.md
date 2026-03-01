## 🐍 Python Cheat Sheet for Data Analysis & Practice

### 📦 Core Python Syntax

| Concept | Example |
|--------|---------|
| **Variables** | `x = 5`, `name = "Alice"` |
| **Data types** | `int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`, `set` |
| **Conditionals** | `if`, `elif`, `else` |
| **Loops** | `for item in list:`, `while True:` |
| **Functions** | `def greet(name): return "Hello " + name` |
| **List comprehension** | `[x**2 for x in range(5)]` |

### 🗃 Lists, Dicts, and Useful Methods

```python
numbers = [1, 2, 3]
numbers.append(4)
numbers[0]  # → 1

data = {"name": "Alice", "age": 30}
data["name"]  # → "Alice"
data.get("age", 0)
📚 Built-in Functions
Function	Purpose
len()	Get number of items
type()	Check data type
sorted()	Sort items
range()	Create a range
enumerate()	Loop with index
zip()	Combine lists
```

### Built-in Functions

| Function      | Purpose             |
| ------------- | ------------------- |
| `len()`       | Get number of items |
| `type()`      | Check data type     |
| `sorted()`    | Sort items          |
| `range()`     | Create a range      |
| `enumerate()` | Loop with index     |
| `zip()`       | Combine lists       |


### 🧮 NumPy Basics
```python
import numpy as np

a = np.array([1, 2, 3])
a.mean()
a.shape
np.arange(0, 10, 2)
```

### 📊 pandas Basics
```python
import pandas as pd

df = pd.read_csv("data.csv")
df.head()
df.info()
df["col"].value_counts()
df[["col1", "col2"]].describe()
```

### Filtering & Grouping
``` python
df[df["score"] > 80]
df.groupby("region")["sales"].sum()
df.sort_values("date", ascending=False)
```

### Plotting (matplotlib / seaborn)
```python
import matplotlib.pyplot as plt
import seaborn as sns

df["value"].hist()
sns.barplot(x="category", y="amount", data=df)
plt.title("My Chart")
plt.show()
```
#### bar graph
```python
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
```


### Jupyter Notebook Tips
| Command         | Purpose                     |
| --------------- | --------------------------- |
| `Shift + Enter` | Run current cell            |
| `Esc + A/B`     | Insert new cell above/below |
| `%timeit`       | Benchmark execution time    |
| `?function`     | Show help                   |
| `!ls` or `!pwd` | Run shell commands          |

### File I/O
```python
with open("file.txt") as f:
    lines = f.readlines()

df = pd.read_csv("file.csv")
df.to_csv("output.csv", index=False)
```

### Data Cleaning Tips
| Task           | Code                                         |
| -------------- | -------------------------------------------- |
| Remove nulls   | `df.dropna()` or `df.fillna(value)`          |
| Rename columns | `df.rename(columns={"old": "new"})`          |
| Change types   | `df["col"] = df["col"].astype(int)`          |
| Apply function | `df["col"] = df["col"].apply(lambda x: x+1)` |
