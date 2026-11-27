from pathlib import Path
root=Path(__file__).resolve().parents[1]
zh='**接手交大開發到一半的專案後，五個月內完成整合。** 原先交大預計開發五年，在第三年中途我負責接手專案PM，包含整合、開發與驗證。'
en='**Completed integration within five months after taking over an in-progress National Chiao Tung University project.** The university had planned a five-year development schedule. I took over as project manager partway through the third year, with responsibility for integration, development, and validation.'
for name in ['README.md','projects/fpga.md','scripts/integrate-fpga-brief.py']:
 p=root/name;s=p.read_text(encoding='utf8')
 s=s.replace('**接手交大專案後，五個月內完成整合。** 既有研究與程式來自交大；我負責接手後的整合、開發與驗證，不是從零獨立開發。',zh)
 s=s.replace('**接手交大專案後，五個月內完成整合。** 以既有研究與程式基礎為起點，負責接手後的整合、開發與驗證，不將成果描述為從零獨立開發。',zh)
 p.write_text(s,encoding='utf8')
for name in ['README.en.md','projects/fpga.en.md','scripts/integrate-fpga-brief.py']:
 p=root/name;s=p.read_text(encoding='utf8')
 for old in ['**Completed integration within five months after taking over a National Chiao Tung University project.** Existing research and code came from the university. I owned subsequent integration, development, and validation, rather than building everything independently from scratch.', '**Completed integration within five months after taking over a National Chiao Tung University project.** The work built on existing university research and code. My contribution was subsequent integration, development, and validation, not an independent build from scratch.']:
  s=s.replace(old,en)
 p.write_text(s,encoding='utf8')
old='接手交大專案後，五個月內完成整合。'
new='交大原訂五年開發計畫，我於第三年中途接手專案PM，負責整合、開發與驗證，五個月內完成整合。'
old_en='Completed integration within five months after taking over a National Chiao Tung University project.'
new_en='The university project had a five-year development plan. I took over as project manager partway through its third year, responsible for integration, development, and validation, and completed integration within five months.'
for name in ['docs/index.html','scripts/translations.en.json','scripts/integrate-fpga-brief.py']:
 p=root/name;s=p.read_text(encoding='utf8').replace(old,new).replace(old_en,new_en);p.write_text(s,encoding='utf8')
