"""Create deterministic diagnostic assets, not final creative work."""
from pathlib import Path
import math, struct, wave, json
root = Path(__file__).resolve().parents[1]
base = root / 'assets'
(base / 'images').mkdir(parents=True, exist_ok=True)
(base / 'audio').mkdir(parents=True, exist_ok=True)
for view, target in [('a', 340), ('b', 865)]:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">
<rect width="1280" height="720" fill="#1a2832"/>
<path d="M0 0L280 130H1000L1280 0Z" fill="#253844"/>
<path d="M0 720L280 490H1000L1280 720Z" fill="#273a44"/>
<path d="M0 0L280 130V490L0 720Z" fill="#21313b"/>
<path d="M1280 0L1000 130V490L1280 720Z" fill="#18252d"/>
<g fill="none" stroke="#425660" stroke-width="2"><path d="M280 130H1000V490H280Z"/><path d="M0 0L280 130M1280 0L1000 130M0 720L280 490M1280 720L1000 490"/><path d="M110 630H1170M200 557H1080M420 490L310 720M640 490V720M860 490L970 720"/></g>
<rect x="520" y="180" width="220" height="310" rx="3" fill="#101e26" stroke="#4a626b" stroke-width="3"/>
<path d="M630 185V485" stroke="#39515b" stroke-width="2"/>
<rect x="600" y="310" width="60" height="6" fill="#a4e7cf"/>
<rect x="{target-60}" y="310" width="180" height="145" rx="4" fill="#30464e" stroke="#82b7a8" stroke-width="3"/>
<rect x="{target-42}" y="328" width="144" height="72" rx="2" fill="#162b2d"/>
<path d="M{target-25} 350h90M{target-25} 367h65M{target-25} 384h80" stroke="#81ac9c" stroke-width="3"/>
<rect x="300" y="143" width="240" height="4" fill="#80a597"/><rect x="740" y="143" width="240" height="4" fill="#80a597"/>
<text x="50" y="60" fill="#a7b8bc" font-family="Arial" font-size="15" letter-spacing="3">VIEW {view.upper()} / GEOMETRY FIXTURE</text>
<text x="50" y="685" fill="#93a5ab" font-family="Arial" font-size="13" letter-spacing="2">IMAGE REPLACEMENT TARGET · 1280 × 720</text>
</svg>'''
    (base / 'images' / f'view-{view}.svg').write_text(svg,encoding='utf-8')
rate=22050
with wave.open(str(base / 'audio' / 'test-tone.wav'),'wb') as audio:
    audio.setparams((1,2,rate,0,'NONE','not compressed'))
    samples=[]
    for i in range(rate*4):
        t=i/rate
        envelope=min(1,t/.08,(4-t)/.15)
        samples.append(struct.pack('<h',int(4500*envelope*math.sin(2*math.pi*440*t))))
    audio.writeframes(b''.join(samples))
records=[]
for name in ['images/view-a.svg','images/view-b.svg','audio/test-tone.wav']:
    records.append({'path':'assets/'+name,'author':'AI-assisted diagnostic code; not student creative work','source':'scripts/create_fixtures.py','license':'Project diagnostic fixture; no third-party source','modifications':'Generated locally','use':'technical test only; replace before final submission'})
(base / 'manifest.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
print('Created two image fixtures and one audio fixture.')
