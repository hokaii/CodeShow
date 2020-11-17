import aiml,os

kernel = aiml.Kernel()
os.chdir("H:\\Python\\Python3.6.6\\Lib\\site-packages\\aiml\\botdata\\alice")
kernel.learn("startup.xml")
kernel.respond("LOAD ALICE")

while True:
	print(kernel.respond(input(" >>")))