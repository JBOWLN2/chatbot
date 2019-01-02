# importing regex and random libraries
import re
import random

# potential negative responses
negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
# keywords for exiting the conversation 
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
# random starter questions
random_questions = (
    "Why are you here? ", 
    "Are there many humans like you? ", 
    "What do you consume for sustenance? ", 
    "Is there intelligent life on this planet? ", 
    "Does Earth have a leader? ",
    "What planets have you visited? ",
    "What technology do you have on this planet?"
    )

name = ""

alienbabble = (
    # Your planet...
  {r'.*\s*your planet':
    ("My planet is a utopia of diverse organisms and species. ",
    "I am from Opidipus, the capital of the Wayward Galaxies. ")
    },
  # why do you...?
    {r'why\sdo\syou\s(.*[^\?]*)\??':
     ("What makes you think I {0}? ",
      "Do I {0}?",
      "Do you think I should {0}?",
     	"Why whould I ever do that?",
     	"What is {0}?")
    },
  # why...?
    {r'.*why\s+.*':
     ("Just passing through...",
      "I thought I would check things out since I was In the area",
      "I was sent to address the foul odors of the greenhouse gasses you are emitting")
    },
  # what...?
    {r'.*what\s+.*':
     ("Why do you ask?",
      "What do you think?",
      "That all depends. Why are you interested?")
    },
  # it is...
    {r'.*it\s+is':
     ("You seem quite sure. What makes you think that?",
      "Do you have any information to support that?",
     "Why jump to that conclusion?")
    },
  # I think...
    {r'.*i\s+think\s(.*)[\?\.\!]?':
     ("You don't sound too sure about {0}?",
      "You think {0}? Why?")
    },
  # Other responses
    {r'.*':
     ("Please tell me more. ",
      "Tell me more! ",
      "Why do you say that? ",
      "I see. Can you elaborate? ",
      "Interesting. Can you tell me more? ",
      "I see. How do you think? ",
      "Why? ",
      "How do you think I feel when you say that? ")
    }
)

# Define greet() below:
def greet():
  name = input("Hello, please tell me your name? ")

  will_help = input("Hi {}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? ".format(name))
  
  if will_help in negative_responses:
    print ("Ok, have a nice Earth day!")
    return
  return True

# Define make_exit() here:
def make_exit(reply):
  for i in exit_commands:
    if reply == i:
      print("I have to go now. Bye!")
      return True


# Define alienbot() next:
def alienbot():
  if greet() is True:
    reply = input(random.choice(random_questions)).lower()
    while make_exit(reply) is not True:
      reply = converse(reply)


# Define converse() below:

def converse(reply):
  for pair in alienbabble:
    for regex_pattern, alien_answers in pair.items():
      found_match = re.match(regex_pattern, reply)
      if found_match:
        alien_answer = random.choice(alien_answers)
        reply = input(formatted_alien_answer).lower()
      formatted_alien_answer = alien_answer.format(*[reflect(matching_group) 						for matching_group in found_match.groups()])
      return reply
        
    

# dictionary used to switch pronouns 
# and verbs in responses
reflections = {
    "i'm": "you are",
    "you're": "i'm",
    "was": "were",
    "i": "you",
    "are": "am",
    "am": "are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "I",
    "me": "you"
}
def reflect(response):
  words = response.split()
  for index, word in enumerate(words):
    if word in reflections:
      words[index] = reflections[word]
  return ' '.join(words)

alienbot()
