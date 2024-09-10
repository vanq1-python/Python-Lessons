def longest_common_prefix(words):
    if not words:
        return ""

    # Начинаем с первого слова в качестве префикса
    prefix = words[0]

    for word in words[1:]:
        # Уменьшаем префикс, пока он не будет общим для всех слов
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # Убираем последний символ
            if not prefix:
                return ""  # Если префикс стал пустым

    return prefix

# Пример использования
words = ["flower", "flow", "flight"]
result = longest_common_prefix(words)
print(result)  # Вывод: "fl"

