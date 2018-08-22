set -e
source env.sh
cd dependencies && ./install.sh && cd -
source compile.sh

export PYTHONPATH=~/.local/lib/python2.7/site-packages/:$PYTHONPATH
export PATH=~/.local/bin:$PATH

cd $EMPTYHEADED_HOME/query_compiler && sbt test && cd -
# LD_HOME=/homes/wu636/.linuxbrew/lib/
# $LD_HOME/ld-linux-x86-64.so.2 $PY_HOME/python2.7 test/graph/triangles_listing.py y
python test/graph/triangles_listing.py y

