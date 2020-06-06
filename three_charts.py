# three_charts.py

#
# CHART 1 (PIE) 
# THIS PRINTS OUT IN A NEW WINDOW
#
import matplotlib.pyplot as plt

plt.show()
pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

labels = [i["company"] for i in pie_data]
sizes = [i["market_share"] for i in pie_data]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.


print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data
plt.show()

#
# CHART 2 (LINE)
#THIS PRINTS OUT IN YOUR BROWSER AS A FILE HTML
#

import plotly
import plotly.graph_objs as go

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

time = [x["date"] for x in line_data]
price = [i["stock_price_usd"] for i in line_data]

plotly.offline.plot({
    "data": [go.Scatter(x= time, y=price)],
    "layout": go.Layout(title="Stock Price (Jan 2019)")
}, auto_open=True)


print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data) # TODO: create a line graph based on the line_data

#
# CHART 3 (HORIZONTAL BAR)
#THIS PRINTS OUT IN A NEW WINDOW
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]



print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

x = [i["genre"] for i in bar_data]
viewers = [i["viewers"] for i in bar_data]

x_pos = [i for i, _ in enumerate(x)]

plt.barh(x_pos, viewers, color='green')
plt.ylabel("Genre")
plt.xlabel("Viewers")
plt.title("Movie Viewership by Genre")

plt.yticks(x_pos, x)

plt.show()


#THE BELOW IS FOR A VERTICAL BAR CHART
#plt.style.use('ggplot')
#
#genre = [i["genre"] for i in bar_data]
#viewers = [i["viewers"] for i in bar_data]
#
#x_pos = [i for i, _ in enumerate(genre)]
#
#plt.bar(x_pos, viewers, color='blue')
#plt.xlabel("Genre")
#plt.ylabel("Viewers")
#plt.title("Movie Viewership by Genre")
#
#plt.xticks(x_pos, genre)
#
#plt.show()