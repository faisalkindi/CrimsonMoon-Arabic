import json,io
def writesub(chunk,F):
    src={}
    for l in open(f'review_chunks/r_{chunk}.jsonl',encoding='utf-8'):
        r=json.loads(l); src[r['key']]=r
    out=[]
    for k,subs,sev,why,conf in F:
        r=src[k]; fix=r['ar']
        for old,new in subs:
            assert fix.count(old)>=1,(k,old)
            fix=fix.replace(old,new)
        assert fix!=r['ar']
        assert r['ar'].count('\n')==fix.count('\n'),('newline',k)
        for p in r['placeholders']: assert p in fix,(k,p)
        out.append({"id":r['id'],"source_en":r['source_en'],"ar_before":r['ar'],"ar_fixed":fix,"severity":sev,"reason":why,"confidence":conf})
    with io.open(f'review_findings/A_r_{chunk}.jsonl','w',encoding='utf-8') as f:
        for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
    print(f'r_{chunk} findings: {len(out)}')
