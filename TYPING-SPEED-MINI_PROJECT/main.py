import random
import time

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "In the midst of chaos, there is also opportunity.",
    "it is not the strongest of the species that survive",
    "nor the most intelligent",
    "but the one most responsive to change.",
]

def typing_test():
    test_sentence =random.choice(sentences)
    print("Type the following sentences as fast as you can:")
    print(test_sentence)
    input("Press Enter When you are ready for this...")
    start_time =time.time()
    user_input =input("\nStart Typing :\n")
    end_time =time.time()
    time_taken =end_time -start_time
    word_count = len(test_sentence.split(" "))
    typing_speed = word_count / (time_taken / 60)

    print("Results :")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed:{word_count}")
    print(f"Typing speed: {typing_speed:.2f} words per minute")

typing_test()    
    