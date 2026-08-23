#!/usr/bin/env python3
"""Extract per-protocol configs from ALL shared DefiLlama registry adapters
(compound.js, aave.js, curators.js) plus the authoritative deadAdapters.json."""
import json,re,glob,os,collections
B='/home/user/dd1/incident-intelligence'; AD=f'{B}/sources/defillama/adapters'
def newest(pat):
    fs=glob.glob(f'{AD}/*{pat}')
    return sorted(fs,key=os.path.getsize)[-1] if fs else None
def split_blocks(src, names=('const configs','const aaveV2Configs','const aaveConfigs')):
    out={}
    for nm in names:
        out.update(_one(src,nm))
    return out
def _one(src,nm):
    i=src.find(nm)
    if i<0: return {}
    i=src.find('{',i); out={}; depth=0; key=None; start=None; j=i
    while j<len(src):
        ch=src[j]
        if depth==1 and ch in '\'"':
            q=ch; k=src.find(q,j+1)
            if k>0 and re.match(r'\s*:',src[k+1:k+6]): key=src[j+1:k]; start=None
        if ch=='{':
            depth+=1
            if depth==2 and key and start is None: start=j
        elif ch=='}':
            depth-=1
            if depth==1 and key and start is not None: out[key]=src[start:j+1]; key=None; start=None
            if depth==0: break
        j+=1
    return out
ROLES=('comptroller','unitroller','cether','morphoVaultOwners','morpho','euler','turtleclub',
       'vaults','silo','registry','addressesProvider','lendingPoolAddressesProvider','poolAddressesProvider')
res={}
srcs={'compound':newest('registries__compound.js'),
      'aave':f'{AD}/_registry__aave.js' if os.path.exists(f'{AD}/_registry__aave.js') else newest('registries__aave.js'),
      'curators':newest('registries__curators.js')}
for tag,f in srcs.items():
    if not f: print('missing registry',tag); continue
    src=open(f,encoding='utf-8',errors='replace').read()
    for k,b in split_blocks(src).items():
        e=res.setdefault(k.lower(),{"registry_keys":[],"addresses":{},"flags":[],"registry_files":[]})
        e["registry_keys"].append(f"{tag}:{k}")
        if os.path.basename(f) not in e["registry_files"]: e["registry_files"].append(os.path.basename(f))
        for role in ROLES:
            for m in re.finditer(role+r"\s*:\s*(\[[^\]]*\]|'0x[a-fA-F0-9]{40}'|\"0x[a-fA-F0-9]{40}\")",b):
                a=re.findall(r'0x[a-fA-F0-9]{40}',m.group(1))
                if a: e["addresses"][role]=sorted(set((e["addresses"].get(role) or [])+a))
        # bare `chain: '0x...'` shorthand used by both registries
        for m in re.finditer(r"(\w+)\s*:\s*'(0x[a-fA-F0-9]{40})'",b):
            ch,a=m.group(1),m.group(2)
            if ch not in ROLES:
                e["addresses"].setdefault('chain_shorthand',[])
                if a not in e["addresses"]['chain_shorthand']: e["addresses"]['chain_shorthand'].append(a)
        for fl in ('isInsolvent','isDeprecated','blacklist'):
            if re.search(fl+r'\s*:\s*true',b) and fl not in e["flags"]: e["flags"].append(fl)
        e[f"{tag}_config_excerpt"]=b[:1200]
        e["chains_in_config"]=sorted(set(re.findall(
          r'\b(ethereum|arbitrum|optimism|base|bsc|binance|polygon|avax|avalanche|xdai|gnosis|linea|scroll|blast|mantle|sonic|metis|core|fantom|celo|moonbeam|moonriver|kava|canto|era|zksync|unichain|berachain|hyperliquid|plasma|katana|fraxtal|mode|manta|taiko|zircuit)\b',b,re.I)))
json.dump(res,open(f'{B}/protocols/registry_configs.json','w'),indent=1)

dead=json.load(open(f'{AD}/_registry__deadAdapters.json')) if os.path.exists(f'{AD}/_registry__deadAdapters.json') else {}
json.dump(dead,open(f'{B}/protocols/dead_adapters.json','w'))

E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
def norm(s): return re.sub(r'[^a-z0-9]','',(s or '').lower())
regnorm={norm(k):k for k in res}; deadnorm={norm(k):k for k in dead}
m={}; dm={}
for slug,r in E.items():
    proj=(r.get('_module') or '').split('/')[0].replace('.js','')
    for cand in (proj,slug,r.get('name') or ''):
        k=regnorm.get(norm(cand))
        if k: m[slug]=k; break
    for cand in (proj,slug,r.get('name') or ''):
        k=deadnorm.get(norm(cand))
        if k: dm[slug]=k; break
json.dump(m,open(f'{B}/protocols/registry_slug_map.json','w'),indent=1)
json.dump(dm,open(f'{B}/protocols/dead_adapter_slug_map.json','w'),indent=1)
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
wl=list(dict.fromkeys(w['protocol_slug'] for w in W))
print(json.dumps({"registry_entries":len(res),
 "compound":sum(1 for v in res.values() if any(x.startswith('compound:') for x in v['registry_keys'])),
 "aave":sum(1 for v in res.values() if any(x.startswith('aave:') for x in v['registry_keys'])),
 "curators":sum(1 for v in res.values() if any(x.startswith('curators:') for x in v['registry_keys'])),
 "dead_adapters":len(dead),
 "slug_to_registry":len(m),"slug_to_dead":len(dm),
 "worklist_mapped_registry":sum(1 for s in wl if s in m),
 "worklist_mapped_dead":sum(1 for s in wl if s in dm),
 "with_comptroller":sum(1 for v in res.values() if v['addresses'].get('comptroller')),
 "with_aave_registry":sum(1 for v in res.values() if v['addresses'].get('registry') or v['addresses'].get('addressesProvider')),
 "with_curator_vaults":sum(1 for v in res.values() if v['addresses'].get('morpho') or v['addresses'].get('morphoVaultOwners'))},indent=2))
