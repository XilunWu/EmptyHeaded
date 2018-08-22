import sys
print(sys.path)

import numpy as np
import pandas as pd
from emptyheaded import *

def triangle_agg(db):
    tri_agg = \
              """
              TriangleList(a,b,c) :- Edge(a,b),Edge(b,c),Edge(a,c).
              """
    print "\nTRIANGLE LIST"
    db.eval(tri_agg)

    tri = db.get("TriangleList")
    df = tri.getDF()
    #print df
    
#    if tri.num_rows != 0:
#        raise ResultError("NUMBER OF ROWS INCORRECT: " + str(tri.num_rows))
    
#    if df.iloc[0][0] != 9672060L:
#        raise ResultError("ANNOTATION INCORRECT: " + str(df.iloc[0][0]))
                            
def test():
  build = True
  ratings = pd.read_csv(os.path.expandvars("$EMPTYHEADED_HOME")+"/test/graph/data/g+/gplus_simple.txt",\
                        sep=' ',\
                        names=["0","1"],\
                        dtype={"0":np.uint32,"1":np.uint32})
#  print ratings

  graph = Relation(
    name="Edge",
    dataframe=ratings,
    attribute_names=["a","b"])

  if build:
    db = Database.create(
      Config(num_threads=16),
      os.path.expandvars("$EMPTYHEADED_HOME")+"/test/graph/databases/triangle_counting",
      [graph])
    db.build()
  db = Database.from_existing(os.path.expandvars("$EMPTYHEADED_HOME")+"/test/graph/databases/triangle_counting")

  triangle_agg(db)

start()
os.system("rm -rf "+os.path.expandvars("$EMPTYHEADED_HOME")+"/test/graph/databases"+" && mkdir -p "+os.path.expandvars("$EMPTYHEADED_HOME")+"/test/graph/databases")
test()
stop()
