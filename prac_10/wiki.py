import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    title = input("Enter page title: ").strip()
    while title:
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        except Exception as e:
            print("An unexpected error occurred:", e)
    print("Thank you.")

if __name__ == "__main__":
    main()
