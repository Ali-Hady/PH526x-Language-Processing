import os
import pandas as pd
from read import read_book, word_count, word_stats
from given_code import count_words_fast


hamlets = hamlets = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@hamlets.csv", 
                      index_col=0)
num_rows = 1

"""
# My own attempt
language, text = hamlets.iloc[0]
data = pd.DataFrame(columns=("word", "count", "length", "frequency"))
counter = count_words_fast(text)
for num, word in enumerate(counter, start=1):
    count = counter[word]
    if count > 10:
        frequency = "frequent"
    elif count == 1:
        frequency = "unique"
    else:
        frequency = "infrequent"
        
    data.loc[num] = word, count, len(word), frequency

print(data[data.frequency=="infrequent"]["length"].mean())
"""

def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"
    
    data["length"] = data["word"].apply(len)
    
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)

grouped_data = pd.DataFrame(columns=("language", "frequency", "mean_word_length", "num_words"))

for i in range(3):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    grouped_data = pd.concat((grouped_data, sub_data))

print(grouped_data)

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")

plt.savefig("stats.pdf")