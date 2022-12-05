import spacy

nlp = spacy.load("en_core_web_sm'")


text = """Tom went into the lighthouse and filled a bucket of water. Loved by the people in the house, Tom pulled in a stream of water and was rescued by only a woman. Shortly afterwards, the cat had drowned. It was found by a group of people and was taken to a lake. It is believed that it was drowned under a nearby flood, possibly because of unseen influences. The cat can still speak, but is currently suffering from multiple diseases, specifically tuberculosis. Tom will be reunited with his three friends over the next few days."""

doc = nlp(text)

print(doc.ents)
