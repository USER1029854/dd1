#!/usr/bin/env python3
"""Build the non-EVM cohort and classify each protocol's execution runtime.

Why the runtime matters, and why this is not a blanket sweep
-----------------------------------------------------------
The families derived from INC-2026-08-18-MAY are runtime-specific, and applying
them everywhere would manufacture false candidates:

  Cosmos SDK (Go)     a handler can write state, return an error, and have the
                      write survive if the caller does not use a cache context.
                      ALL FOUR runtime families apply.
  Substrate (Rust)    same class: without #[transactional] a dispatchable's
                      writes persist past an error. All four apply.
  Solana (Rust)       a failed instruction reverts the whole transaction, so the
                      two rollback families do NOT apply. The shared-key clobber
                      does -- instruction batches writing one PDA -- and so does
                      the stride family.
  Move (Sui/Aptos)    abort unwinds the transaction. Rollback families do NOT
                      apply; clobber and stride do.
  Cairo / TON / other  treated as UNKNOWN_RUNTIME: only the runtime-agnostic
                      stride family applies, and the pair is capped accordingly.

Everything here is DefiLlama metadata plus a public repository URL. No code has
been read at this stage.
"""
import json,sys,collections
B='/home/user/dd1/incident-intelligence'

EVM={'Ethereum','Arbitrum','Optimism','Base','Polygon','Binance','Avalanche','Fantom','Gnosis','xDai',
 'Linea','Scroll','Blast','Mantle','zkSync Era','Metis','Celo','Moonbeam','Moonriver','Cronos','Kava',
 'Aurora','Harmony','Heco','OKExChain','Boba','Canto','Core','opBNB','Mode','Fraxtal','Zora','Manta',
 'Taiko','Sonic','Berachain','Hyperliquid L1','Unichain','Ink','Soneium','Abstract','Sei','Bitlayer',
 'Merlin','Rootstock','Telos','Velas','Fuse','Astar','Evmos','Klaytn','Kaia','Milkomeda','Syscoin',
 'Ultron','Wanchain','Elastos','Meter','Tomochain','Shiden','Palm','Nova','Arbitrum Nova',
 'Polygon zkEVM','World Chain','Plume','Corn','Swellchain','Lisk','Zircuit','Morph','Bob','BSquared',
 'Duckchain','Story','Katana','Etherlink',
 # added after auditing what fell into UNKNOWN_RUNTIME: all EVM-equivalent execution,
 # so they belong to the main screen, not to this cohort.
 'Monad','Pulse','PulseChain','RSK','Rootstock','XDC','X Layer','Conflux','IoTeX','Plasma',
 'MegaETH','Bitkub','WEMIX','Plume Mainnet','Somnia','CORE','Mezo','Robinhood Chain','Chiliz',
 'Igra','Filecoin','Hemi','Botanix','Superposition','Sophon','Cyber','Redstone','Zeta','ZetaChain',
 'Kroma','Immutable zkEVM','Gravity','Ronin','Oasis Sapphire','Sapphire','Emerald','Beam','ApeChain',
 'Shape','Lens','Vana','Sanko','Zklink','Rari','Degen','Ancient8','opBNB','Nahmii','Fantom Sonic',
 'Arthera','Zeniq','Neon','Neon EVM','Fusion','Godwoken','Boba_Bnb','Boba Bnb','Ethereum Classic',
 'Callisto','Energi','Thundercore','GoChain','Kardia','Oasys','HPB','Smartbch','Nuls','Hoo',
 'Bittorrent','BitTorrent','Dogechain','Loop','Shibarium','Zyx','Cube','Dexit','Echelon','Ecoball'}

COSMOS={'Cosmos','Osmosis','Thorchain','Injective','Juno','Terra','Terra Classic','Kujira','Neutron',
 'Stargaze','Secret','Persistence','Comdex','Crescent','Chihuahua','Migaloo','Archway','Noble',
 'Stride','Quicksilver','Umee','Agoric','Axelar','Band','Sifchain','Bostrom','Nolus','Dymension',
 'Mayachain','Maya','Babylon','Elys','Nibiru','Cronos POS','dYdX','Celestia','Saga','Xion'}
SOLANA={'Solana','Eclipse','Pythnet','Fogo','Sonic SVM','SOON'}
MOVE={'Sui','Aptos','Movement','Initia','Iota','IOTA','Supra','Umi'}
SUBSTRATE={'Polkadot','Kusama','HydraDX','Acala','Karura','Bifrost','Interlay','Phala','Centrifuge',
 'Moonbase','Darwinia','Edgeware','Hydration','Mangata','Zeitgeist','Pendulum','Amplitude'}
CAIRO={'Starknet','Paradex'}
OTHERVM={'TON','Tezos','Cardano','Algorand','Stellar','Waves','Near','Elrond','MultiversX','Tron',
 'EOS','WAX','Hedera','Radix','Zilliqa','Icon','Ergo','Kaspa','Bitcoin','Stacks','Zcash','Dash',
 'Litecoin','Dogecoin','Ripple','XRPL','Flare','Songbird','Chia','Concordium','Massa','Alephium',
 'ICP','Flow','Mixin','Proton','Bitcoincash','NEO','Fuel','VeChain','Nervos','Sia','Arweave',
 'Obyte','Nimiq','Verus','Komodo','Qtum','Decred','Handshake','Nano','Vite','Aeternity','Harmony ONE'}

# family -> which runtimes it may legitimately be screened against
RUNTIME_FAMILIES={
 'RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER':{'COSMOS_SDK_GO','SUBSTRATE_RUST'},
 'RUNTIME-HANDLER-ERROR-NO-ROLLBACK':{'COSMOS_SDK_GO','SUBSTRATE_RUST'},
 'RUNTIME-BATCHED-MESSAGE-SHARED-KEY-CLOBBER':{'COSMOS_SDK_GO','SUBSTRATE_RUST','SOLANA_RUST','MOVE'},
 'RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE':{'COSMOS_SDK_GO','SUBSTRATE_RUST','SOLANA_RUST','MOVE',
                                           'CAIRO','OTHER_VM','UNKNOWN_RUNTIME'},
}
EXT={'COSMOS_SDK_GO':['.go'],'SUBSTRATE_RUST':['.rs'],'SOLANA_RUST':['.rs'],'MOVE':['.move'],
     'CAIRO':['.cairo'],'OTHER_VM':['.rs','.go','.ts','.fc','.tact','.py','.hs'],
     'UNKNOWN_RUNTIME':['.rs','.go','.move','.ts']}

def runtime(chains):
    c=set(chains or [])
    if c & COSMOS:    return 'COSMOS_SDK_GO'
    if c & SUBSTRATE: return 'SUBSTRATE_RUST'
    if c & SOLANA:    return 'SOLANA_RUST'
    if c & MOVE:      return 'MOVE'
    if c & CAIRO:     return 'CAIRO'
    if c & OTHERVM:   return 'OTHER_VM'
    return 'UNKNOWN_RUNTIME'

def main():
    U=json.load(open(f'{B}/protocols/defillama_universe.json'))
    rows=[]
    for u in U:
        t=u.get('_tvl') or 0
        ch=u.get('_chains') or []
        if t<50_000 or not ch: continue
        if set(ch) & EVM: continue                     # EVM is already covered by the main screen
        rt=runtime(ch)
        gh=(u.get('_github') or [])
        rows.append({"slug":u['slug'],"name":u['name'],"tvl":t,"chains":ch[:6],
          "category":u.get('_cat'),"runtime":rt,"github":gh,
          "defillama_url":u.get('_defillama_url'),
          "in_band":50_000<=t<=30_000_000,
          "screenable_families":sorted(f for f,rs in RUNTIME_FAMILIES.items() if rt in rs),
          "source_extensions":EXT[rt],
          "conditions":u.get('_conditions') or [],
          "audit_links":u.get('_audit_links') or [],"deprecated":bool(u.get('_deprecated')),
          "listedAt":u.get('listedAt')})
    rows.sort(key=lambda r:(-r['tvl']))
    json.dump(rows,open(f'{B}/protocols/nonevm_cohort.json','w'),indent=1)
    band=[r for r in rows if r['in_band']]
    gh=[r for r in band if r['github']]
    print(json.dumps({
      "non_evm_above_floor":len(rows),
      "in_band":len(band),
      "in_band_with_public_repo":len(gh),
      "by_runtime_all":dict(collections.Counter(r['runtime'] for r in rows)),
      "by_runtime_screenable":dict(collections.Counter(r['runtime'] for r in gh)),
      "tvl_in_band_with_repo":round(sum(r['tvl'] for r in gh),2)},indent=2))

if __name__=='__main__': main()
