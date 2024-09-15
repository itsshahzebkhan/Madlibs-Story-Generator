# step 1 - to start this project you need to install PyCharm community edition or VS Code
# step 2 - you need a story with replaceable words also known as a Mad libs story in order to start this project
# step 3 - go to ChatGPT and type a prompt - "write a short mad libs story in not more than 50 words where replaceable words should be under <word>"
# step 4 - now copy that story and come back to the IDE that you are going to be using for this project
# step 5 - open a new file right next to your main Python/project file and name it "story.txt"
# step 6 - you can also use the stories that I have provided
# step 7 - paste the copied story in that text file
# step 8 - start coding


with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

print(words)


answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)

# note - your story does not have to be under 50 words, it can be as long as you want it to be!
