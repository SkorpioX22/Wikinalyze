import wikipediaapi
import matplotlib.pyplot as plt

def get_byte_count(title):
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent='Your User Agent'
    )
    page = wiki_wiki.page(title)
    return page.length

def plot_byte_counts(articles):
    titles = []
    byte_counts = []

    for article in articles:
        titles.append(article)
        byte_counts.append(get_byte_count(article))

    plt.bar(titles, byte_counts)
    plt.xlabel('Wikipedia Articles')
    plt.ylabel('Byte Count')
    plt.title('Byte Count of Wikipedia Articles')
    plt.xticks(rotation=15)
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    num_articles = int(input("Enter the number of Wikipedia articles (up to 5): "))
    if num_articles <= 0 or num_articles > 5:
        print("Invalid number of articles.")
    else:
        articles = []
        for i in range(num_articles):
            article = input(f"Enter the title of article {i + 1}: ")
            articles.append(article)

        plot_byte_counts(articles)
