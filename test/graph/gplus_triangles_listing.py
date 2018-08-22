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
                            
def test():
  build = True
  ratings = pd.read_csv(os.path.expandvars("$EMPTYHEADED_HOME")+"/test/graph/data/g+/gplus_coded_unique.txt",\
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
      Config(num_threads=1),
      os.path.expandvars("$EMPTYHEADED_HOME")+"/test/graph/databases/triangle_counting",
      [graph])
    db.build()
  db = Database.from_existing(os.path.expandvars("$EMPTYHEADED_HOME")+"/test/graph/databases/triangle_counting")

  triangle_agg(db)

start()
os.system("rm -rf "+os.path.expandvars("$EMPTYHEADED_HOME")+"/test/graph/databases"+" && mkdir -p "+os.path.expandvars("$EMPTYHEADED_HOME")+"/test/graph/databases")
test()
stop()
