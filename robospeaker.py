# import os
# if __name__=='__main__':
#     x = input("Enter the sentence or word: ")
#     command = "say {}".format(x)
#     os.system(command)
import pyttsx3

if __name__ == '__main__':
    
    while True:
        text = input("Enter the sentence or word: ")
    # Initialize the text-to-speech engine
        engine = pyttsx3.init()
    # Set properties (optional)
        if text=="quit":
            break
        
        else:
            engine.setProperty('rate', 150)  # Speed of speech
            engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
            # Say the input text
            engine.say(text)

            # Wait for speech to finish
            engine.runAndWait()
    
    