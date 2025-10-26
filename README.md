##  Chinook Database Analysis

The Chinook database contains information about a digital music store which includes artists, albums, tracks, customers, and invoices information. This analysis explores sales and track distributions to understand which artists and genres perform best.


###  Top 10 Artists by Total Sales

This chart highlights the **artists who generated the highest total revenue** based on invoice data. It combines information from the `Artist`, `Album`, `Track`, and `InvoiceLine` tables to calculate total sales per artist.

**Insight:**  
Artists like **Ieom Maiden**, **U2** and **Metallica** consistently appear among the top sellers, showing the strong influence of classic rock artists in the store's catalog.

![Top 10 Artists](top10_artists.png)https://github.com/Monishab3/Chinook-database-analysis/blob/main/Top%2010%20Artists.png

###  Top 10 Genres by Number of Tracks

This visualisation shows the **most common music genres** in the Chinook database, based on the number of available tracks per genre.

**Insight:**  
Genres such as **Rock**, **Latin** and **Metal** dominate the catalog, indicating that the store’s inventory heavily leans toward rock and its subgenres. 

![Top 10 Genres](top10_genres.png)https://github.com/Monishab3/Chinook-database-analysis/blob/main/Top%2010%20Genres%20by%20number%20of%20tracks.png

###  Tools Used
- **SQLite** — to query the Chinook database  
- **Pandas** — for data manipulation  
- **Matplotlib  and Seaborn** — for visualisation  
- **Python** — as the main analysis language

###  Conclusion
This mini-project demonstrates how to:
- Extract and aggregate data from a relational database
- Analyze business insights (sales, genres, trends)
- Visualise findings using Python data tools
