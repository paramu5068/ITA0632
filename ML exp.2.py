import pandas as pd

# a) Create DataFrame
df = pd.DataFrame({
    "Student": ["Asha", "Bala", "Chitra", "Dinesh", "Esha"],
    "Marks": [78, 45, 88, 62, 35],
    "Attendance": [90, 75, 95, 85, 60]
})

print("a) DataFrame:")
print(df)
print("Column names:", df.columns)

print("\n----------------")

# b) First 3 rows, last 2 rows, shape
print("b) First 3 rows:")
print(df.head(3))
print("Last 2 rows:")
print(df.tail(2))
print("Shape:", df.shape)

print("\n----------------")

# c) Students scoring more than 70
print("c) Marks > 70:")
print(df[df["Marks"] > 70])

print("\n----------------")

# d) Result column
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")
print("d) With Result column:")
print(df)

print("\n----------------")

# e) Save to CSV and read back
df.to_csv("students.csv", index=False)
new_df = pd.read_csv("students.csv")
print("e) Data read from CSV:")
print(new_df)
