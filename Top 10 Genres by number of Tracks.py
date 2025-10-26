import sqlite3, pandas as pd, seaborn as sns, matplotlib.pyplot as plt

conn = sqlite3.connect("Chinook_Sqlite.sqlite")

query="""
SELECT g.Name , count(t.TrackId) as total FROM Genre as g
JOIN Track as t on g.GenreId = t.GenreId
Group by g.Name
Order by total DESC
LIMIT 10;"""

df=pd.read_sql_query(query,conn)

print(df)

sns.barplot(x = "Name", y= "total", data=df, palette="cividis")
plt.title("Top 10 Genres by Number of Tracks")
plt.xlabel("Number of Tracks")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()

conn.close()