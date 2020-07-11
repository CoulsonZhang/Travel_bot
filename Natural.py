#This take charge of natural lanuage process & extra the entities
# & preparation of the following search
#

import spacy
nlp = spacy.load('en_core_web_sm')

include_entities = ['DATE', 'ORG', 'PERSON']

def extract_entities(message):
    # Create a dict to hold the entities
    ents = {}
    doc = nlp(message)
    for ent in doc.ents:
        ents[ent.label_] = ent.text
    return ents

print(extract_entities('Coulson need a Delta flight tomorrow from ORD airport'))
print(extract_entities('people who graduated from MIT in 1999'))

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
# Create a trainer
trainer = Trainer(config.load("config_spacy.yml"))
training_data = load_data('nlu.md')
interpreter = trainer.train(training_data)

# Try it out
print(interpreter.parse("I'm looking for a flight to Zhengzhou"))
