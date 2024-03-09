# Phikeia Oath
print("The Phikeia Oath:")
print("When you type in a sentence correctly you will move on to the next. If you get anything wrong you will try again.")


for j in range(15):
    print(" ")


# The Phikeia Oath:
sentence1 = "I, Phikeia *, now declare that I pledge myself and my services to the Phi Delta Theta Fraternity."
s1 = False
sentence2 = "That I will discharge faithfully the duties devolving upon me as a Phikeia, and that I will try to promote the welfare of the Fraternity, and that I will be always mindful of the basic principles of the Fraternity."
s2 = False
sentence3 = "And further, I pledge myself as a college man to uphold the honor and dignity of Phi Delta Theta, everywhere and at all times."
s3 = False
sentence4 = "I will never bring disgrace to this, my Fraternity, by any act of dishonesty or moral cowardice."
s4 = False
sentence5 = "I will stand firm for the ideals and sacred things of my Fraternity, both alone and with my Phikeia brothers."
s5 = False
sentence6 = "I will revere and obey the laws of the Fraternity, and do my best to incite a like respect and reverence in my Phikeia brothers and in every member of this chapter."
s6 = False
sentence7 = "I will strive in all ways to transmit the Fraternity to those who may follow after, not only not less, but greater than it was transmitted to me."
s7 = False


string = [ sentence1, sentence2, sentence3, sentence4, sentence5, sentence6, sentence7]
s = [ s1, s2, s3, s4, s5, s6, s7]
def ask(sentence):
    sentenceI = input("\nEnter Here:  ")
    if sentence == sentenceI:
        #print("Good.")
        return True
    elif "Skip" == sentenceI:
        print(sentence)
        return True
    else:
        ccount = 0
        if len(sentenceI) <= len(sentence):
            index = 0
            for l in sentenceI:
                if l == sentence[index]:
                    ccount += 1
                    index += 1
                else:
                    break

            print("\nYou have the first " + str(ccount) + " matching letters.")
        else:
            print("\nToo many characters.")


        print("There are " + str(len(sentence) + 1) + " total characters in this sentence. \nYou have: " + str(len(sentenceI)))
        return False



i = 0
end = 7
guess = 0
while i < end:
    if s[i] == False:
        if guess >= 3:
            prompt = "How much of the sentence do you need? Choose 1 - " + str(len(string[i])+1) + ": "
            uinp = input(prompt)
            g = int(uinp)
            print(string[i][0:g])
            guess = 0
            
        s[i] = ask(string[i])
        print(s[i])
        guess += 1
    else:
        i += 1
        guess = 0
    