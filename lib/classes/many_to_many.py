class Article:
    _all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self._all.append(self)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise AttributeError("Can't change the title of the article once set")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author class")
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine class")
        self._magazine = magazine
        




class Author:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Can't change the name of the author once set")
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    def articles(self):
        return [article for article in Article._all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
    
    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass






class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Category must be a non-empty string")
        self._category = category

    def articles(self):
        return [article for article in Article._all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))
    
    def article_titles(self):
        pass

    def contributing_authors(self):
        pass