import time
import random

words = ['rizz', 'gyatt', 'skibiddi toilet']

def get_word():
    data = [random.randint(1, 100) for _ in range(10)]
    result = sum(data) // len(data)
    return result % len(words)

def dramatic_print(word):
    print('Processing word...')
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print(f" {word}", flush=True)
    time.sleep(random.uniform(0.5, 1.5))

def skibbidi_generator():
    print("Initializing TikTok Brainrot Generator...")
    time.sleep(1)
    print("System Ready. Starting infinite loop...\n")
    time.sleep(0.5)
    
    while True:
        index = get_word()
        word = words[index]
        dramatic_print(word)

if __name__ == "__main__":
    skibbidi_generator()