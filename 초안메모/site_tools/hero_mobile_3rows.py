import numpy as np, sys
from PIL import Image
src='/Users/yacom/everpaw/Captures/탭1_1028저녁/단체/단체사진_원본_4800x2700.jpg'
im=np.asarray(Image.open(src).convert('RGB')).astype(np.int32)
Y0,Y1=1100,1600; W=1890; OV=40
band=im[Y0:Y1]; r,g,b=band[...,0],band[...,1],band[...,2]
cost=(~((g>r+8)&(g>b+25))).astype(np.float64)*10+0.01
def find_seam(xa,xb):
    c=cost[:,xa:xb]; H,Wc=c.shape; acc=c.copy(); back=np.zeros((H,Wc),int)
    for y in range(1,H):
        p=acc[y-1]; st=np.vstack([np.r_[np.inf,p[:-1]],p,np.r_[p[1:],np.inf]]); k=st.argmin(0); acc[y]+=st.min(0); back[y]=k-1
    s=np.zeros(H,int); s[-1]=acc[-1].argmin()
    for y in range(H-1,0,-1): s[y-1]=s[y]+back[y,s[y]]
    print('seam',xa+s.min(),xa+s.max(),'dog px',int((c[np.arange(H),s]>1).sum()))
    return s+xa
s1=find_seam(int(sys.argv[2]),int(sys.argv[3])); s2=find_seam(int(sys.argv[4]),int(sys.argv[5]))
fill=im[Y1+40:Y1+40+(Y1-Y0)]
H=Y1-Y0
def strip(x0,left,right):
    out=band[:,x0:x0+W].astype(float); f=fill[:,x0:x0+W].astype(float)
    xs=np.arange(x0,x0+W)[None,:]
    a=np.ones((H,W))
    if left is not None: a=np.minimum(a,np.clip((xs-left[:,None])/20.0,0,1))
    if right is not None: a=np.minimum(a,np.clip((right[:,None]-xs)/20.0,0,1))
    return out*a[...,None]+f*(1-a[...,None])
# 줄마다 가운데 맞추기: 줄의 강아지 범위 가운데에 W 폭
c1=(60+s1.max())//2; c2=(s1.min()+s2.max())//2; c3=(s2.min()+4620)//2
x1=max(0,min(4800-W,c1-W//2)); x2=max(0,min(4800-W,c2-W//2)); x3=max(0,min(4800-W,c3-W//2))
rows=[strip(x1,None,s1),strip(x2,s1,s2),strip(x3,s2,None)]
out=rows[0]
for rr in rows[1:]:
    w=np.linspace(1,0,OV)[:,None,None]
    blend=out[-OV:]*w+rr[:OV]*(1-w)
    out=np.vstack([out[:-OV],blend,rr[OV:]])
Image.fromarray(np.clip(out,0,255).astype(np.uint8)).save(sys.argv[1]); print(out.shape, out.shape[1]/out.shape[0])
