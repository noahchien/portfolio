[![Noah Chien | I build software. With people in mind.](docs/assets/cover-en.svg)](https://noahchien.github.io/portfolio/en.html)

# I'm Noah Chien. I help move problems toward solutions.

[繁體中文](README.md)　／　**English**

**Target roles: Project Manager / Senior Software Engineer**　|　10+ years in software development

![Project leadership](docs/assets/badge-role.svg) ![Financial systems](docs/assets/badge-domain.svg) ![Problem solving](docs/assets/badge-focus.svg)

[Portfolio website](https://noahchien.github.io/portfolio/en.html)　·　[Engineering](projects/work.en.md)　·　[Background](about.en.md)　·　[Writing](projects/novel.en.md)　·　[Games](projects/cryptfall.en.md)

From speech applications to financial systems, my work has covered implementation, systems analysis, project planning, and coordination. What I'd like you to remember is **my ability to keep a difficult problem moving toward a solution, even in an unfamiliar domain or with limited resources**.

Colleagues often come to me when a project gets stuck. Sometimes the next step is clearer requirements; sometimes it's understanding why a case cannot be tested. And sometimes the most useful answer is a small tool that keeps a whole team from getting stuck in the same place again.

## Three projects to start with

> [!IMPORTANT]
> **FPGA development completed more than a year ahead of the original estimate**, after development staffing fell from three people to one. I owned planning, technical direction, code review, and validation. **Not yet in production**; now a foundation for a follow-on project.

| Project | The challenge | My responsibility and outcome |
| --- | --- | --- |
| **FPGA development** | A specialized, logic-circuit-oriented domain; development staffing fell from three people to one | Owned planning, development, progress, and quality decisions. Reorganized implementation around engineer-led AI collaboration and completed development more than a year ahead of the original estimated development schedule. Not yet in production; serving as a foundation for the next project. |
| **Virtual exchange** | Manual testing could not cover many edge cases; real incidents were difficult to reproduce | Built tooling for the risk-control development team, supporting scripted scenarios, automated stress tests, and replay of actual incidents from imported logs. |
| **Logger Monitor** | Multiple IT teams relied on manual log checks, with a risk of missed issues | Checks file existence and error keywords, supports team-specific INI settings, and sends notifications through LINE and Telegram Bot APIs. |

Together, they illustrate **project ownership, test design, and reusable tooling for teams**.

## 🔧 FPGA: keeping development moving after the team shrank

### The challenge

FPGA development was a specialized area with a strong logic-circuit focus, and staffing fell from three people to just me. The way I had been developing the project needed to change so that implementation would not crowd out planning and quality work.

### How I organized the work

I moved most code implementation to AI-assisted development while retaining responsibility for:

- **Direction and planning:** what to build, whether the technical direction was sound, and when to adjust it.
- **Code review:** reading the output and checking its assumptions and domain understanding.
- **On-site judgment:** verifying the actual environment when AI assumptions did not match the machines.
- **Validation and quality:** understanding the intended outcome, choosing how to verify it, and checking actual results against the goal.
- **Progress management:** organizing and tracking development after staffing was reduced.

For example, the AI assumed the machine had one network interface when the actual setup had two. I checked the environment, explained the incorrect premise, and worked with it to correct the implementation. **Generating code and knowing whether that code fits the real environment are different responsibilities.**

### Outcome and current status

Development was completed **more than a year ahead of the original estimated development schedule**. The project is not yet in production; it is being used as a technical foundation for a follow-on project. The schedule improvement refers to development, not a production launch or an unreported performance benchmark.

[Read the FPGA case study](projects/fpga.en.md)

> [!TIP]
> **Tools used by real teams:** the virtual exchange supports risk-control developers with **scripted edge cases, stress tests, and log replay**. Logger Monitor helps multiple IT teams with **configurable checks and LINE / Telegram notifications**.

## 🧪 Virtual exchange: make difficult cases reproducible

The risk-control development team had relied on manual testing. Many edge cases were difficult to cover, and even incidents that had already occurred in the real environment were hard to recreate.

I developed a virtual exchange so the team could:

- Write scripts to define special test scenarios.
- Run automated stress tests with less reliance on manual operation.
- Import real logs to reproduce events and support investigation.

The value is **turning a one-off incident into a scenario the team can observe and analyze again**.

[Read the testing-tools case study](projects/testing-tools.en.md)

## 🔎 Logger Monitor: take repeatable checks out of manual inspection

IT teams had been checking logs by hand, which left room for omissions. I developed Logger Monitor for use across multiple teams, with configurable checks and notifications.

| Check | Approach |
| --- | --- |
| File existence | Confirm that the expected log file exists |
| Error indicators | Look for configured keywords, such as ERROR, termination-related messages, and catch |
| Team-specific needs | Adjust checks through INI configuration |
| Notifications | Send alerts through LINE and Telegram Bot APIs |

The virtual exchange and Logger Monitor use technologies including Python and Node.js. They serve the risk-control development team and multiple IT teams respectively. I do not claim unmeasured time savings or zero missed alerts.

## What I can bring to the next team

| Capability | Experience behind it |
| --- | --- |
| **Break down an unfamiliar problem** | FPGA planning, implementation trade-offs, on-site checks, and validation decisions |
| **Adapt delivery to limited resources** | Reorganized AI-assisted implementation and review after staffing fell from three people to one |
| **Turn experience into reusable tools** | Scripted scenarios, log-based incident reproduction, and cross-team log monitoring |
| **Connect financial workflows with software** | Securities risk control and trading, trust services, and insurance payment platforms |
| **Connect requirements, development, and people** | Systems analysis, architecture and database design, code reviews, vendor progress, and requirements discussions |

## 🛠️ Technical background

- **Backend and systems:** Java/Spring, C/C++, Node.js, Python, JavaScript, REST APIs, and database design.
- **Development and delivery:** Git, Docker, Jenkins, Linux, and DevOps collaboration.
- **Other project experience:** MongoDB, Elasticsearch, data-observation platforms, and speech recognition and synthesis applications.
- **Recent focus:** FPGA projects, engineer-led AI collaboration, testing tools, and monitoring tools.

## Career experience

| Organization | Focus |
| --- | --- |
| Concord Securities · R&D Assistant Manager | Risk control and trading, development coordination, maintenance, workflow digitization |
| CTBC Bank · Engineer | Trust services, system upgrades, architecture, and testing |
| Fubon Life · Senior Specialist | Payment platforms, system and database design, code reviews, vendor coordination |
| Institute for Information Industry · Software Engineer | Frontend/backend development, data platforms, Redmine, and DevOps |
| NCCC, Cyberon, Inventec | Systems analysis, speech applications, mobile/Windows software, and production-line testing |

Computer Science graduate, National Chiao Tung University. [Read my background](about.en.md)

## Outside work, I'm creating worlds of my own

[![Watch the Cryptfall in-engine video](docs/media/cryptfall-preview.gif)](https://noahchien.github.io/portfolio/en.html#projects)

**[Watch the game videos](https://noahchien.github.io/portfolio/en.html#projects)**: monster rigs and attack wind-up at 0.6x speed, plus a half-speed mage casting preview. These are in-engine tests, not full normal-speed gameplay.

**Fiction and content tooling:** As stories grow, so do characters, settings, and loose threads. Git, outline checks, relationship maps, and mobile review pages help me keep the work connected. The finalized manuscript currently reaches Chapter 35; longer-term outlines and tooling remain in progress. [Writing project](projects/novel.en.md)

**Cryptfall:** A Godot prototype exploring procedural dungeons, class-based combat, equipment, and upgrade choices. It is a development prototype, not a released game. [Game project](projects/cryptfall.en.md)

## An attitude I want to keep

> Don't be afraid to make mistakes. Be afraid of repeating them.

I want each solved problem to leave behind something useful for the next one. That connects my work on testing tools, monitoring, and AI-assisted project delivery.

If your team needs someone who can understand a problem, work through it, and take responsibility for planning and delivery, these cases are an introduction to how I work.

---

Work cases describe the problem, my responsibilities, methods, and outcomes. Company code and internal materials are not published due to confidentiality requirements. Personal projects include AI-assisted work, with completed work and future plans clearly distinguished.
