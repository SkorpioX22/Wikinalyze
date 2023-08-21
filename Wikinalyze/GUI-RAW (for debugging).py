import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import wikipediaapi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class WikipediaByteCountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wikinalyze")

        self.num_articles_label = ttk.Label(root, text="Enter (up to 50) the number of Wikipedia articles to compare:")
        self.num_articles_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.num_articles_entry = ttk.Entry(root)
        self.num_articles_entry.grid(row=0, column=1, padx=10, pady=10)

        self.submit_button = ttk.Button(root, text="Start Comparison", command=self.show_articles)
        self.submit_button.grid(row=0, column=2, padx=10, pady=10)

        self.github_button = tk.Button(root, text="Visit my GitHub page!", fg="white", bg="black", command=self.open_github)
        self.github_button.grid(row=0, column=3, padx=10, pady=10)

        self.byte_count_canvas = None

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

        articles = []
        for i in range(num_articles):
            article = self.input_article_title(f"Enter the title of article {i + 1}:")
            if not self.validate_article(article):
                self.show_error(f"Article '{article}' does not exist on Wikipedia.")
                return
            articles.append(article)

        self.plot_byte_counts(articles)

    def input_article_title(self, prompt):
        article = simpledialog.askstring("Enter Article Title", prompt)
        return article

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

    def plot_byte_counts(self, articles):
        if self.byte_count_canvas:
            self.byte_count_canvas.get_tk_widget().destroy()

        titles = []
        byte_counts = []

        for article in articles:
            titles.append(article)
            byte_counts.append(self.get_byte_count(article))

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(titles, byte_counts)
        ax.set_xlabel('Wikipedia Articles')
        ax.set_ylabel('Byte Count')
        ax.set_title('Byte Count of Wikipedia Articles')
        ax.set_xticklabels(titles, rotation=15)
        plt.tight_layout()

        self.byte_count_canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.byte_count_canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        toolbar_frame = ttk.Frame(self.root)
        toolbar_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        NavigationToolbar2Tk(self.byte_count_canvas, toolbar_frame)

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/SkorpioX22/Wikinalyze")

if __name__ == "__main__":
    root = tk.Tk()
    app = WikipediaByteCountApp(root)
    root.mainloop()
