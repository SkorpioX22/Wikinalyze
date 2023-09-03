import tkinter as tk
from tkinter import ttk, messagebox
import wikipediaapi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import progressbar

class WikipediaByteCountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wikipedia Article Byte Count Comparison")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        self.header_label = ttk.Label(root, text="Wikinalyze, by skorpiox22", font=("Helvetica", 12, "bold"))
        self.header_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.num_articles_label = ttk.Label(root, text="Enter the number of Wikipedia articles (up to 50):")
        self.num_articles_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.num_articles_entry = ttk.Entry(root)
        self.num_articles_entry.grid(row=1, column=1, padx=10, pady=10)

        self.submit_button = ttk.Button(root, text="Submit", command=self.show_articles)
        self.submit_button.grid(row=1, column=2, padx=10, pady=10, sticky="e")

        # Styling the GitHub button
        self.style = ttk.Style()
        self.style.configure("Black.TButton", foreground="white", background="black")
        
        self.github_button = tk.Button(root, text="Visit GitHub", fg="white", bg="black", command=self.open_github)
        self.github_button.grid(row=1, column=3, padx=10, pady=10)

        self.article_labels = []
        self.articles = []

        self.byte_count_canvas = None

    # (rest of your code remains the same)


    def validate_article(self, title):
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent='Your User Agent'
        )
        page = wiki_wiki.page(title)
        return page.exists()

    def show_articles(self):
        num_articles = int(self.num_articles_entry.get())
        if num_articles <= 0 or num_articles > 50:
            self.show_error("Invalid number of articles. Please enter a value between 1 and 50.")
            return

        # Clear previous articles and labels
        for label in self.article_labels:
            label.destroy()
        self.article_labels = []
        self.articles = []

        for i in range(num_articles):
            label = ttk.Label(self.root, text=f"Enter the title of article {i + 1}:")
            label.grid(row=i + 2, column=0, padx=10, pady=10, sticky="w")
            self.article_labels.append(label)

            entry = ttk.Entry(self.root)
            entry.grid(row=i + 2, column=1, padx=10, pady=10)
            self.articles.append(entry)

        self.submit_button.config(command=self.plot_byte_counts)

    def plot_byte_counts(self):
        if self.byte_count_canvas:
            self.byte_count_canvas.get_tk_widget().destroy()

        titles = []
        byte_counts = []

        with progressbar.ProgressBar(max_value=len(self.articles)) as bar:
            for i, entry in enumerate(self.articles):
                article = entry.get()
                if not self.validate_article(article):
                    self.show_error(f"Article '{article}' does not exist on Wikipedia.")
                    return
                titles.append(article)
                byte_counts.append(self.get_byte_count(article))
                bar.update(i + 1)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(titles, byte_counts)
        ax.set_xlabel('Wikipedia Articles')
        ax.set_ylabel('Byte Count')
        ax.set_title('Byte Count of Wikipedia Articles')
        ax.set_xticklabels(titles, rotation=15)
        plt.tight_layout()

        self.byte_count_canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.byte_count_canvas.get_tk_widget().grid(row=len(self.articles) + 2, column=0, columnspan=4, padx=10, pady=10)

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/SkorpioX22/Wikinalyze")

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def get_byte_count(self, title):
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent='Your User Agent'
        )
        page = wiki_wiki.page(title)
        return page.length

if __name__ == "__main__":
    root = tk.Tk()
    app = WikipediaByteCountApp(root)
    root.mainloop()
