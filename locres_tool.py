"""Minimal locres v3 read/rewrite: keeps entry section bytes verbatim, rewrites string array."""
import struct,sys
def rstr(f):
    n=struct.unpack("<i",f.read(4))[0]
    if n<0: return f.read(-n*2)[:-2].decode("utf-16le")
    return f.read(n)[:-1].decode("utf-8") if n else ""
def wstr(s):
    if s=="" : return struct.pack("<i",0)
    if all(ord(c)<128 for c in s):
        b=s.encode()+b"\0"; return struct.pack("<i",len(b))+b
    b=s.encode("utf-16le")+b"\0\0"; return struct.pack("<i",-(len(b)//2))+b
def load(path):
    d=open(path,"rb").read(); f=__import__("io").BytesIO(d)
    f.read(16); ver=f.read(1)[0]; assert ver==3, ver
    off=struct.unpack("<q",f.read(8))[0]
    head=d[:off]; f.seek(off); n=struct.unpack("<I",f.read(4))[0]
    strings=[]
    for _ in range(n):
        s=rstr(f); rc=struct.unpack("<I",f.read(4))[0]; strings.append([s,rc])
    return head,strings
def save(path,head,strings):
    off=len(head); head=head[:17]+struct.pack("<q",off)+head[25:]
    out=bytearray(head); out+=struct.pack("<I",len(strings))
    for s,rc in strings: out+=wstr(s)+struct.pack("<I",rc)
    open(path,"wb").write(out)
if __name__=="__main__":
    src,dst,prefix=sys.argv[1:4]
    head,strings=load(src)
    for e in strings: e[0]=prefix+e[0]
    save(dst,head,strings)
    # self-check
    h2,s2=load(dst); assert h2[:17]==head[:17] and len(s2)==len(strings) and s2[0][0].startswith(prefix)
    print("ok",dst,len(strings))
