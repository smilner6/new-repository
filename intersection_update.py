text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

new_text = set(text.split())

preps = new_text.intersection(prepositions)
print(preps)

