import os
import pandas as pd
import matplotlib.pyplot as plt
from read import read_book, word_stats

# reading and collecting data
stats = pd.DataFrame(columns=("Language", "Author", "Title", "Length", "Unique"))
book_dir = "./Books"
row_num = 1
for lang in os.listdir(book_dir):
    language  = os.listdir(book_dir + "/" + lang)
    for auth in language:
        author = os.listdir(book_dir + "/" + lang + "/" + auth)
        for title in author:
            book_path = book_dir + "/" + lang + "/" + auth + "/" + title
            text = read_book(book_path)
            num_unique, counts = word_stats(text)
            stats.loc[row_num] = lang, auth.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            row_num += 1

# plotting
plt.figure(figsize=[10, 18])
subset = stats[stats.Language=="English"]
plt.loglog(subset.Length, subset.Unique, "o", label="English", color="crimson")
subset = stats[stats.Language=="French"]
plt.loglog(subset.Length, subset.Unique, "o", label="French", color="forestgreen")
subset = stats[stats.Language=="German"]
plt.loglog(subset.Length, subset.Unique, "o", label="German", color="orange")
subset = stats[stats.Language=="Portuguese"]
plt.loglog(subset.Length, subset.Unique, "o", label="Portuguese", color="blueviolet")
plt.legend()
plt.savefig("book_plot.pdf")
