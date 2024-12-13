class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().lower()\
                    .replace(',', '').replace('.', '')\
                    .replace('=', '').replace('!', '')\
                    .replace('?', '').replace(';', '')\
                    .replace(':', '').replace(' - ', '')\
                    .split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        find_words = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                find_words[file_name] = words.index(word.lower()) + 1
        return find_words

    def count(self, word):
        count_words = {}
        for file_name, words in self.get_all_words().items():
            count = 0
            if word.lower() in words:
                count += words.count(word.lower())
                count_words[file_name] = count
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
