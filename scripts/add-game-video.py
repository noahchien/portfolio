from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
page=root/'docs/index.html';text=page.read_text(encoding='utf8')
visual='''<div class="project-visual game-video"><video controls muted playsinline loop preload="metadata" poster="media/cryptfall-video-poster.jpg" aria-label="Cryptfall怪物骨架與攻擊前搖，引擎內測試，0.6倍速"><source src="media/cryptfall-monster-motion.mp4" type="video/mp4">瀏覽器不支援影片，請下載觀看。</video></div>'''
pattern=r'<div class="project-visual"><svg[^>]*aria-label="地城餘燼的程序地城概念示意，非遊戲實機畫面"[\s\S]*?</svg></div>'
text,count=re.subn(pattern,lambda m:visual,text,count=1)
if count!=1 and 'class="project-visual game-video"' not in text:raise SystemExit('Game visual not found')
marker='<small class="project-status">開發原型，尚未正式發行；手機實機驗證仍待完成。</small>'
extra='''<p class="video-note">怪物骨架與攻擊前搖 · Godot引擎內測試 · 0.6倍速 · 無聲</p><details class="video-details"><summary>再看法師施法動畫</summary><video controls muted playsinline preload="none" aria-label="法師施法動畫，引擎內雙角度半速預覽"><source src="media/cryptfall-mage-motion.mp4" type="video/mp4">瀏覽器不支援影片，請下載觀看。</video><p class="video-note">法師施法動畫 · 引擎內半速預覽 · 無聲</p><p class="video-credit">法師模型與貼圖由Meshy 6 Lite依原創設定生成，採CC BY 4.0；遊戲端調整網格、骨架、蒙皮並整合武器與動畫。</p><a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0授權</a></details>'''
if 'class="video-details"' not in text:text=text.replace(marker,extra+marker)
page.write_text(text,encoding='utf8')
file=root/'scripts/translations.en.json';data=json.loads(file.read_text(encoding='utf8'));data.update({
'Cryptfall怪物骨架與攻擊前搖，引擎內測試，0.6倍速':'Cryptfall monster rigging and attack wind-up, in-engine test at 0.6x speed',
'瀏覽器不支援影片，請下載觀看。':'Your browser does not support this video. Please download it to watch.',
'怪物骨架與攻擊前搖 · Godot引擎內測試 · 0.6倍速 · 無聲':'Monster rigs & attack wind-up · Godot in-engine test · 0.6x speed · Silent',
'再看法師施法動畫':'Watch the mage casting preview',
'法師施法動畫，引擎內雙角度半速預覽':'Mage casting animation, dual-angle in-engine preview at half speed',
'法師施法動畫 · 引擎內半速預覽 · 無聲':'Mage casting animation · In-engine preview at half speed · Silent',
'法師模型與貼圖由Meshy 6 Lite依原創設定生成，採CC BY 4.0；遊戲端調整網格、骨架、蒙皮並整合武器與動畫。':'Mage model and textures generated with Meshy 6 Lite from original character concepts, licensed under CC BY 4.0. The game includes mesh, rigging, and skinning changes, with integrated weapons and animation.',
'CC BY 4.0授權':'CC BY 4.0 license'
});file.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
for name,heading,body in [
('README.md','## 工作以外，我也在創造自己的世界','[![播放Cryptfall引擎內測試影片](docs/media/cryptfall-video-poster.jpg)](https://noahchien.github.io/portfolio/#projects)\n\n**[播放遊戲影片](https://noahchien.github.io/portfolio/#projects)**：怪物骨架與攻擊前搖（0.6倍速），另有法師半速施法預覽。均為引擎內測試，非完整正常速度遊玩片段。'),
('README.en.md',"## Outside work, I'm creating worlds of my own",'[![Watch the Cryptfall in-engine video](docs/media/cryptfall-video-poster.jpg)](https://noahchien.github.io/portfolio/en.html#projects)\n\n**[Watch the game videos](https://noahchien.github.io/portfolio/en.html#projects)**: monster rigs and attack wind-up at 0.6x speed, plus a half-speed mage casting preview. These are in-engine tests, not full normal-speed gameplay.')]:
 p=root/name;s=p.read_text(encoding='utf8')
 if 'docs/media/cryptfall-video-poster.jpg' not in s:s=s.replace(heading,heading+'\n\n'+body)
 p.write_text(s,encoding='utf8')
