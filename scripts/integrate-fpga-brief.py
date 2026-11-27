from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
zh='''## 🔧 FPGA：接手交大專案，把既有基礎整合到實機

> [!NOTE]
> **接手交大開發到一半的專案後，五個月內完成整合。** 原先交大預計開發五年，在第三年中途我負責接手專案PM，包含整合、開發與驗證。

### 下單前風控閘道｜我主導整合與開發

把券商既有的價格、額度、庫存等檢查搬進FPGA，同時讓開發與驗證有共同的規則依據。

| 開發重點 | 我的工作與成果 |
| --- | --- |
| **規則萃取** | 整理兩代既有風控系統的57條差異，建立機器可讀規則表，作為開發與測試共同依據。 |
| **可預期延遲** | FPGA內部風控判斷為300 MHz、109個時脈，約**0.36 µs**；不是完整交易往返時間。 |
| **雙基準驗證** | 逐筆比較參考模型與FPGA准駁結果，上板後再比對實機與模擬；用12種刻意改壞資料確認比對流程能抓錯。 |
| **交易整合** | 在證交所測試環境完成委託成交與刪單；FPGA保留原單資料，補齊刪單所需資訊。 |
| **時序與異常處理** | 300 MHz時序收斂；處理連線序號、重連與重複送單風險，無法確認狀態時停止並核對。 |

### 期權平價套利系統｜我負責實機驗證

這是由大學團隊開發的產學合作系統，我負責讓它在實際環境中跑對，而非將原系統開發歸為個人成果。

- **錯誤委託60→0：**逐段追查計數器，定位到合成時被固定成常數的變數；修正後，同一晚、同一行情的對照測試中，錯誤套利委託由60筆降為0筆。
- **商品比對0→241,770次：**確認行情格式與解碼器不符，修正後在該次觀測中恢復成功比對。
- **連線問題定位：**從疑似硬體故障，追到主機與FPGA位址衝突；調整衝突網卡後連線成功。
- **行情服務釐清：**分辨彙整與逐筆行情取得方式，驗證FPGA能穩定接收逐筆資料。

### 資源與品質，仍然要由人負責

在人力由三人縮減至一人後，我負責規劃、進度與技術方向，將大部分程式實作交由AI協助，自己審查產出、核對現場配置並決定驗證方式。開發較原先預估工期提前一年以上。

我用計數器、封包紀錄與實機／模擬比對找證據，先確認要達成的目標，再判斷結果。這比單純讓AI產生程式，更接近我想帶進團隊的解決問題能力。

**技術：**`Alveo U50` · `HLS C++` · `10G Ethernet / TCP` · `FIX 4.4` · `300 MHz`

系統目前作為後續專案基底，尚未正式上線。數據各有量測範圍，不將單次對照結果描述為全面零錯誤。

[閱讀完整FPGA案例與量測範圍](projects/fpga.md)

'''
en='''## 🔧 FPGA: take over a university foundation and integrate it on hardware

> [!NOTE]
> **Completed integration within five months after taking over an in-progress National Chiao Tung University project.** The university had planned a five-year development schedule. I took over as project manager partway through the third year, with responsibility for integration, development, and validation.

### Pre-trade risk gateway | Integration and development lead

Moved existing price, credit-limit, inventory, and other risk checks into FPGA logic while establishing shared rules for development and validation.

| Focus | My work and outcomes |
| --- | --- |
| **Rules extraction** | Resolved 57 differences across two generations of existing systems and created machine-readable rules as a shared development and testing reference. |
| **Predictable latency** | FPGA-internal risk decisions took 109 cycles at 300 MHz, approximately **0.36 µs**; this is not end-to-end trading latency. |
| **Dual-reference validation** | Compared reference-model and FPGA decisions order by order, then hardware against simulation; 12 deliberately corrupted variants checked that the comparison detected faults. |
| **Trading integration** | Successful execution and cancellation in the TWSE test environment; retained original-order information to complete cancellation messages. |
| **Timing and recovery** | Timing closure at 300 MHz; handled sequence numbers, reconnection, and duplicate-submission risks, stopping for reconciliation when state was uncertain. |

### Options parity arbitrage | Hardware validation lead

The original system was developed by a university team. My responsibility was making it work correctly in the actual environment, not claiming the original system's development as my own.

- **Erroneous orders, 60 to 0:** traced stage counters to a variable synthesized into a constant. After correction, the same-night, same-market-data comparison went from 60 erroneous arbitrage orders to 0.
- **Instrument matches, 0 to 241,770:** corrected a market-data format and decoder mismatch, restoring successful matches in the reported observation.
- **Connectivity diagnosis:** traced a suspected hardware issue to an address conflict between the host and FPGA, then resolved the connection by changing the conflicting interface state.
- **Market-data services:** clarified aggregated versus tick-by-tick access and verified stable FPGA receipt of tick-by-tick data.

### People still own resource decisions and quality

When staffing fell from three people to one, I retained planning, progress tracking, and technical direction, using AI for most code implementation while reviewing output, checking the environment, and defining validation. Development progressed more than a year ahead of the original estimated schedule.

I use counters, packet captures, and hardware-versus-simulation comparisons to find evidence. Understanding the intended outcome comes before judging the result. This is the problem-solving responsibility I want to bring to a team.

**Technology:** `Alveo U50` · `HLS C++` · `10G Ethernet / TCP` · `FIX 4.4` · `300 MHz`

The system is a foundation for follow-on work and is not yet in production. Figures retain their measurement scope; a single comparison is not a claim of universal error-free behavior.

[Read the full FPGA case and measurement scope](projects/fpga.en.md)

'''
for name,body in [('README.md',zh),('README.en.md',en)]:
 p=root/name;s=p.read_text(encoding='utf8');start=s.index('## 🔧 FPGA');end=s.index('> [!TIP]',start);s=s[:start]+body+s[end:]
 if name=='README.md':
  s=re.sub(r'^\| \*\*FPGA 專案\*\*.*$', '| **FPGA交易系統** | 接手交大既有基礎，整合風控規則、實機與交易介接；人力三人縮至一人 | 五個月內完成整合；FPGA內部風控約0.36 µs。另負責套利系統實機驗證，同晚同行情對照的錯誤委託60→0。 |',s,flags=re.M)
 else:
  s=re.sub(r'^\| \*\*FPGA development\*\*.*$', '| **FPGA trading systems** | Took over a university foundation; integrated rules, hardware, and trading interfaces as staffing fell from three to one | Integration within five months; approximately 0.36 µs internal risk decisions. Separately led arbitrage-system validation: erroneous orders 60 to 0 in a same-night, same-data comparison. |',s,flags=re.M)
 p.write_text(s,encoding='utf8')
page=root/'docs/index.html';s=page.read_text(encoding='utf8');old=re.search(r'<article class="work-item"><div class="work-company">FPGA專案[\s\S]*?</article>',s)
assert old
paragraph='交大原訂五年開發計畫，我於第三年中途接手專案PM，負責整合、開發與驗證，五個月內完成整合。我主導風控規則萃取、整合開發與雙基準驗證，FPGA內部風控判斷約0.36 µs；另負責大學團隊套利系統的實機驗證，同晚同行情對照中錯誤委託由60降至0。既有研究與程式來自交大，成果建立在接手整合與實機驗證之上。'
new=re.sub(r'<h3>.*?</h3>','<h3>接手既有基礎，把系統整合到實機。</h3>',old.group(),count=1)
new=re.sub(r'<p>.*?</p>','<p>'+paragraph+'</p>',new,count=1);s=s.replace(old.group(),new);page.write_text(s,encoding='utf8')
f=root/'scripts/translations.en.json';d=json.loads(f.read_text(encoding='utf8'));d.update({
'接手既有基礎，把系統整合到實機。':'Build on an existing foundation. Integrate it on real hardware.',
paragraph:'The university project had a five-year development plan. I took over as project manager partway through its third year, responsible for integration, development, and validation, and completed integration within five months. I led risk-rule extraction, integration development, and dual-reference validation, with FPGA-internal risk decisions of approximately 0.36 µs. Separately led hardware validation of a university-developed arbitrage system: erroneous orders fell from 60 to 0 in the same-night, same-data comparison. The work built on existing university research and code.'});f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
