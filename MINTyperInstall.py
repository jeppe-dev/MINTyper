import  os
cmd = "chmod a+x MINTyper"
os.system(cmd)
cmd = "mv MINTyper ~/bin/"
os.system(cmd)
cmd = "chmod a+x MINTyperFunctions.py"
os.system(cmd)
cmd = "mv MINTyperFunctions.py ~/bin/"
os.system(cmd)
#Kma
cmd = "git clone https://bitbucket.org/genomicepidemiology/kma.git"
os.system(cmd)
cmd = "cd kma && make"
os.system(cmd)
cmd = "mv kma/kma ~/bin/"
os.system(cmd)
cmd = "cd .."
os.system(cmd)
#ccphylo
cmd = "git clone https://bitbucket.org/genomicepidemiology/ccphylo.git"
os.system(cmd)
cmd = "cd ccphylo && make"
os.system(cmd)
cmd = "mv ccphylo/ccphylo ~/bin/"
os.system(cmd)
cmd = "cd .."
os.system(cmd)