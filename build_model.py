from modeller import *
from modeller.automodel import *

env = Environ()
a = AutoModel(env, alnfile='m1-mult.ali',
              knowns=('4cmpA','6ifoA','7s37P'), sequence='Q99ZW2_M') #changes made here
a.starting_model = 1
a.ending_model = 3 #important - jitne bologe utni files banengi of types  NS3.B99990001.pdb, NS3.D00000001, NS3.V99990001
a.make()