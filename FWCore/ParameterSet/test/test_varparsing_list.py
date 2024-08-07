import sys
from FWCore.ParameterSet.VarParsing import VarParsing

def parse(argv):
  sys.argv = ['test.py','maxEvents=100']+argv # emulate user arguments
  opts = VarParsing('standard')
  #print(">>> Registering...")
  def add(n, d, m, t):
    #sargs = (repr(n)+',').ljust(13)+(repr(d)+',').ljust(9) +\
    #        f"VarParsing.multiplicity.{m.split('_')[-1]}, " +\
    #        f"VarParsing.multiplicity.{t.split('_')[-1]}".ljust(30)
    #print(f">>>   opts.register({sargs})")
    opts.register(n, d, m, t)
  add('myInts0',   '',      VarParsing.multiplicity.list, VarParsing.varType.int)
  add('myInts1',   0,       VarParsing.multiplicity.list, VarParsing.varType.int)
  add('myInts2',   [0],     VarParsing.multiplicity.list, VarParsing.varType.int)
  add('myFloats0', '',      VarParsing.multiplicity.list, VarParsing.varType.float)
  add('myFloats1', 0,       VarParsing.multiplicity.list, VarParsing.varType.float)
  add('myFloats2', [0],     VarParsing.multiplicity.list, VarParsing.varType.float)
  add('myBools0',  '',      VarParsing.multiplicity.list, VarParsing.varType.bool)
  add('myBools1',  True,    VarParsing.multiplicity.list, VarParsing.varType.bool)
  add('myBools2',  [True],  VarParsing.multiplicity.list, VarParsing.varType.bool)
  add('myStrs0',   '',      VarParsing.multiplicity.list, VarParsing.varType.string)
  add('myStrs1',   'foo',   VarParsing.multiplicity.list, VarParsing.varType.string)
  add('myStrs2',   ['foo'], VarParsing.multiplicity.list, VarParsing.varType.string)
  #print(f">>> Parsing user arguments...")
  #print(f">>>   sys.argv={sys.argv!r}")
  #opts.parseArguments()
  #print(f">>> Parsed:")
  #for var in opts._lists:
  #  if var.startswith('my'):
  #    print(f">>>   opts.{var:<9s} = {getattr(opts,var)!r}")

# parse without user arguments
parse([ ])

# parse with user arguments
parse(['myInts1=0,1','myBools1=True,False','myStrs1=foo,bar','myStrs2=foo,bar'])