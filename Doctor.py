import random

history = []

hedges = ("Please tell me more.",
          "Many of my Patients tell me the same thing.",
          "please continue.")

qualifiers = ("Why do you say that",
              "you seem to think that",
              "can you exlain why")

replacement = {"I": "you", "me": "you", "my": "your",
               "we": "you", "us": "you", "mine": "yours",
               "you": "I", "your": "my", "yours": "mine"}


class Doctor:
    def __init__(self):
        pass

    #greeting message
    def greeting(self):
        return "Good morning, I hope you are doing good!.\n What can I do for you?"

    #fare well message
    def farewell(self):
        return "Have a nice day!"

    #reply strategies
    def reply(self,sentence):

        replyToPatientStrategy = random.randint(1,5)
        if replyToPatientStrategy in (1,2):
            #Just Hedge
            answer = random.choice(hedges)
        elif replyToPatientStrategy == 3 and len(history) > 3:
            #Go Back To an earlier topic
            answer = "Last time you said that" + \
                    changePerson(random.choice(history))
        else:
            # take the current input and structure a reply to patient
            answer = random.choice(qualifiers) + changePerson(sentence)

        history.append(sentence)
        return answer


    #change the person / patient
    def changePerson(sentence):
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(replacement.get(word,word))
        return "".join(replyWords)


    #Manage Interaction between patient and doctor.

    def main():
        Doctor= Doctor()
        print(Doctor.greeting())
        while True:
            sentence.upper('\n>>')
            if sentence.upper()=="QUIT":
                print(Doctor.farewell())
                break
            print(Doctor.reply(sentence))


#main
if __name__== "__main__":
    main()


