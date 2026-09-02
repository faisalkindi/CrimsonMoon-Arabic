import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
n=sys.argv[1]
for i,l in enumerate(open(f'review_chunks/r_{n}.jsonl',encoding='utf-8')):
    r=json.loads(l)
    print(f'#{i} [{r["speaker"]}|{r["category"]}] {r["key"]}')
    print('EN: '+r['source_en'].replace('\n',' \n '))
    fr=r.get('fr') or ''
    if fr.strip()!=r['source_en'].strip(): print('FR: '+fr.replace('\n',' \n '))
    print('AR: '+r['ar'].replace('\n',' \n '))
    print()
