import markovify

with open("data.txt", "r") as f:
    text = f.read()

model = markovify.Text(text)

for i in range(5):
    print(model.make_sentence())
