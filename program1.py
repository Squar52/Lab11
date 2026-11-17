import os
from collections import Counter
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "text.txt")
MARK = "--- Vowel frequency ---"
VOWELS = "aeiou"
SAMPLE_TEXT = (
    "Technology has changed the way people live, work and communicate. "
    "A few decades ago, letters took days to arrive, and a simple question "
    "could take weeks to answer. Today a message crosses the planet in a second.\n"
    "Still, many people say that real learning needs time and patience. "
    "A student who reads a book slowly often remembers more than someone "
    "who only looks at a screen for a minute.\n"
    "The best solution is to use both: modern tools to find information quickly, "
    "and quiet hours to think about it carefully.\n"
)
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(SAMPLE_TEXT)
with open(FILENAME, "r", encoding="utf-8") as f:
    text = f.read()
text = text.split(MARK)[0].rstrip()
counter = Counter(ch for ch in text.lower() if ch in VOWELS)
total = sum(counter.values())
with open(FILENAME, "w", encoding="utf-8") as f:
    f.write(text + "\n\n" + MARK + "\n")
    for v in VOWELS:
        percent = counter[v] / total * 100 if total else 0
        f.write(f"{v}: {counter[v]} ({percent:.1f}%)\n")
print("Частоту голосних записано у файл text.txt")
for v in VOWELS:
    print(v, counter[v])