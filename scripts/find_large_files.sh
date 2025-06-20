git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  grep '^blob' | \
  cut -d' ' -f2,3,4- | \
  sort -k2 -rh | \
  while read hash size path; do
    if [ ! -f "$path" ]; then
      echo "$size $path"
    fi
  done | head -n 30
