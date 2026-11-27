# Low-latency trading on FPGA

[繁體中文](fpga.md)　／　**English**

This was a five-year university partnership. I took over as project manager partway through its third year, responsible for integration, development, and validation. The development team later shrank from three people to one, and development still finished more than a year ahead of the original schedule.

| System | My role | Key results |
| --- | --- | --- |
| Pre-trade risk gateway | Led requirements, architecture, development, and validation | Risk check inside the FPGA in about 0.36 µs; five months from feasibility study to orders filled and cancelled on the stock exchange's test environment |
| Options put-call parity arbitrage | University built the first version; I led late-stage hardware debugging, fixes, and futures-exchange integration | Erroneous orders 60 → 0; decoder matches 0 → 241,770; FPGA logs in to the futures exchange directly |

## Pre-trade risk gateway

Every order has to pass price, credit-limit, and inventory checks before it is sent. Server software used to do this. This system moves the checks into an FPGA so they finish in a fixed time, and it must never let through an order the existing system would block.

### Rules and validation

The rules lived in two generations of existing risk systems that didn't fully agree. I extracted them one by one into a machine-readable rule table and resolved 57 differences. Development and testing both work from that table, so when a rule changes, every affected place can be found.

Validation compares two baselines: the same orders go to a reference model of the current system and to the FPGA, and every accept/reject decision is compared. Violations: 0. On hardware, results are compared against simulation, and 12 deliberately corrupted data sets confirm the comparison really catches errors.

### Latency and exchange integration

| Item | Result |
| --- | --- |
| Risk check inside the FPGA | 109 clock cycles at 300 MHz, about 0.36 µs. Internal processing only, no network round trip |
| Exchange | Logged in, had orders filled, and cancelled orders on the stock exchange's test environment |
| Cancellation | Cancel messages lack the original order's details. The FPGA keeps a copy when the order goes out and fills in the gaps in hardware. The exchange confirmed cancellations within 3 ms |
| Session safety | Sequence numbers and reconnect rules prevent duplicate orders; when state is uncertain, the system stops for manual review |
| Timing | Timing closure at 300 MHz. Hardware behavior that simulation can't show is tracked in a pre-deployment checklist |

The system is the base for a follow-on project and is not in production yet.

`Alveo U50` · `HLS C++` · `10G Ethernet / TCP` · `FIX 4.4` · `300 MHz`

## Options put-call parity arbitrage

The system takes live futures-exchange market data, computes the spread between calls, puts, and futures in hardware, and has the FPGA place orders when an arbitrage opportunity appears. The university team built the first version. It passed every simulation and then kept failing on live data. I led the late-stage hardware debugging, the fixes, and the exchange connection.

| Problem | How it was found and fixed | Result |
| --- | --- | --- |
| Hardware kept sending orders it shouldn't | Read counters stage by stage and found a variable that synthesis had turned into a constant | Same night, same feed: erroneous orders went from 60 to 0 |
| Symbol matches stuck at 0 | The market-data format didn't match the decoder; rewrote the decoder | Matches went from 0 to 241,770 |
| Exchange connection | Connected to the production market-data feed and had the FPGA log in to the futures exchange itself. Logins kept failing and looked like a hardware fault; the host and the FPGA were sharing one network address | With the host's interface turned off, both the futures and options sessions logged in |
| Market-data channels | Worked out how to obtain the aggregated feed (8 updates per second) and the tick-by-tick feed | Confirmed the FPGA receives the tick-by-tick feed reliably |

## Getting it done alone

Once I was the only developer, I handed most implementation to AI tools and kept planning, scheduling, technical direction, code review, on-site checks, and validation. The tools aren't always right: one once assumed a machine had a single network card when it had two, and I had to check the real configuration and correct it. So every conclusion needs evidence: counters, packet captures, and byte-by-byte comparisons between hardware and simulation. If they don't match, work stops until they do.

## How I work

- **Evidence first:** Use counters, file hashes, and packet captures to find where results diverge, and follow the data stage by stage.
- **Verify on hardware, not just in simulation:** Compare hardware output byte by byte. Passing simulation doesn't mean the hardware is right.
- **Write the spec first:** Rules, message formats, and error handling are written down in a form that can be checked.
- **Stop when state is unclear:** Keep the evidence, review manually, then decide how to recover.

Company code, real orders, network settings, and partners' internal documents are not published.

[Back to the portfolio](../README.en.md)
