import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# connect to the database 
conn = sqlite3.connect("Chinook_Sqlite.sqlite")

# Top 10 artists by total sales 
query = """
SELECT a.Name AS Artist,
       ROUND(SUM(il.UnitPrice * il.Quantity), 2) AS Total
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
JOIN Album al ON t.AlbumId = al.AlbumId
JOIN Artist a ON al.ArtistId = a.ArtistId
GROUP BY a.Name
ORDER BY Total DESC
LIMIT 10;
"""

top_artists = pd.read_sql_query(query, conn)

print(top_artists)
# plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
# The order is from highest to lowest in the plot
top_artists = top_artists.sort_values("Total", ascending=False)

sns.barplot(data=top_artists, x="Total", y="Artist")
plt.title("Top 10 Artists by Total Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Artist")

# annotate the bars with values
for i, v in enumerate(top_artists["Total"]):
    plt.text(v + 0.5, i, f"{v:.2f}", va="center")

plt.tight_layout()
# show the plot window
plt.show()

# close connection
conn.close()

