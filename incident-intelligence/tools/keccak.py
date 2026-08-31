"""Minimal pure-Python keccak-256 (Ethereum variant, 0x01 pad).

Only needed to derive 4-byte function selectors, so correctness is checked
against two publicly known selectors at import time. No dependencies.
"""
_RC=[0x0000000000000001,0x0000000000008082,0x800000000000808A,0x8000000080008000,
     0x000000000000808B,0x0000000080000001,0x8000000080008081,0x8000000000008009,
     0x000000000000008A,0x0000000000000088,0x0000000080008009,0x000000008000000A,
     0x000000008000808B,0x800000000000008B,0x8000000000008089,0x8000000000008003,
     0x8000000000008002,0x8000000000000080,0x000000000000800A,0x800000008000000A,
     0x8000000080008081,0x8000000000008080,0x0000000080000001,0x8000000080008008]
_RO=[[0,36,3,41,18],[1,44,10,45,2],[62,6,43,15,61],[28,55,25,21,56],[27,20,39,8,14]]
_M=(1<<64)-1
def _rol(x,n): return ((x<<n)|(x>>(64-n)))&_M
def _f(A):
    for rnd in range(24):
        C=[A[x][0]^A[x][1]^A[x][2]^A[x][3]^A[x][4] for x in range(5)]
        D=[C[(x-1)%5]^_rol(C[(x+1)%5],1) for x in range(5)]
        for x in range(5):
            for y in range(5): A[x][y]^=D[x]
        B=[[0]*5 for _ in range(5)]
        for x in range(5):
            for y in range(5): B[y][(2*x+3*y)%5]=_rol(A[x][y],_RO[x][y])
        for x in range(5):
            for y in range(5): A[x][y]=B[x][y]^((~B[(x+1)%5][y])&_M)&B[(x+2)%5][y]
        A[0][0]^=_RC[rnd]
    return A
def keccak256(data:bytes)->bytes:
    rate=136
    A=[[0]*5 for _ in range(5)]
    pad=data+b'\x01'+b'\x00'*((-len(data)-1)%rate)
    pad=pad[:-1]+bytes([pad[-1]^0x80])
    for off in range(0,len(pad),rate):
        blk=pad[off:off+rate]
        for i in range(rate//8):
            w=int.from_bytes(blk[i*8:i*8+8],'little')
            A[i%5][i//5]^=w
        A=_f(A)
    out=b''
    for i in range(4):
        out+=A[i%5][i//5].to_bytes(8,'little')
    return out[:32]
def selector(sig:str)->str: return '0x'+keccak256(sig.encode()).hex()[:8]
assert selector("owner()")=="0x8da5cb5b", selector("owner()")
assert selector("transfer(address,uint256)")=="0xa9059cbb", selector("transfer(address,uint256)")
