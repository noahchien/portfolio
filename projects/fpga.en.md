# Low-latency FPGA trading systems | Integration and hardware validation

[繁體中文](fpga.md)　／　**English**

> [!IMPORTANT]
> **Completed integration within five months after taking over a National Chiao Tung University project.** The work built on existing university research and code. My contribution was subsequent integration, development, and validation, not an independent build from scratch.

## Two projects, distinct responsibilities

| Project | My role | Representative outcome |
| --- | --- | --- |
| Pre-trade risk gateway | Led requirements, architecture, integration development, and validation after taking over the project | Approximately 0.36 µs for FPGA-internal risk decisions; successful order execution and cancellation in the TWSE test environment |
| Options parity-arbitrage system | Validation lead in an industry–university collaboration; the original system was developed by a university team | Diagnosed erroneous orders, market-data decoding, and connectivity issues, with comparative tests to verify fixes |

## Pre-trade risk gateway: make business rules verifiable in hardware

Each order needs price, credit-limit, inventory, and other checks before submission. The aim was predictable hardware processing while preserving the rejection behavior required by existing risk controls.

### Start with rules and validation references

Rules were distributed across two generations of systems. I extracted machine-readable rules and resolved **57 differences**, establishing a common reference for implementation, testing, and change tracking.

Validation compared acceptance and rejection decisions for the same orders across an existing-system reference model and the FPGA design, followed by hardware-versus-simulation comparisons. The supplied test summary reports zero violations in the tested set. **Twelve deliberately corrupted data variants** checked that the comparison process could actually detect errors. These results do not establish universal error-free behavior.

### Latency and integration scope

| Area | Result and scope |
| --- | --- |
| FPGA-internal risk decision | **109 cycles at 300 MHz, approximately 0.36 µs**; not end-to-end order latency |
| Integration | **Completed within five months of taking over the university project**, building on its existing foundation |
| Test environment | Successful execution in the Taiwan Stock Exchange test environment; not a production launch |
| Cancellation | FPGA retained original-order information to complete cancellation messages; the exchange responded successfully within 3 ms in the reported test, not a general latency guarantee |
| Timing | Timing closure at 300 MHz, with hardware-specific issues captured in a pre-deployment checklist |

Cancellation messages lacked complete original-order information, so the FPGA retained the necessary data when submitting new orders. Connection sequence and reconnection handling addressed duplicate-submission risks after disconnects or restarts. Uncertain states stopped processing for manual reconciliation.

**Technology:** Alveo U50, HLS C++, 10G Ethernet/TCP, FIX 4.4, and timing closure at 300 MHz.

## Options parity arbitrage: make a simulated design work correctly on hardware

The original university-developed system received futures-exchange market data, calculated price differences between calls, puts, and futures, and submitted orders in hardware. My responsibility was hardware validation and diagnosis across counters, decoders, and the network environment.

| Issue | Diagnosis and correction | Observed comparison |
| --- | --- | --- |
| Unintended arbitrage orders | Traced stage counters to a variable synthesized into a constant and corrected it | **60 erroneous orders reduced to 0 in the same-night, same-market-data comparison** |
| No successful instrument matches | Identified a mismatch between market-data format and decoder, then revised decoding | Matches rose from 0 to 241,770 in the reported observation |
| Intermittent connectivity | Isolated an address conflict between the host and FPGA | Disabling the conflicting host interface resolved that connection attempt |
| Different market-data services | Clarified access to eight-updates-per-second aggregated data versus tick-by-tick data | Verified stable receipt of tick-by-tick data on the FPGA |

## Resource planning and AI collaboration

When development staffing fell from three people to one, I shifted most implementation to AI assistance while retaining planning, progress tracking, technical direction, code review, on-site checks, and validation decisions. Compared with the original estimated development schedule, development progressed more than a year ahead.

In one AI collaboration example, it assumed a single network interface in a dual-interface environment. I checked the machine and corrected its understanding. This example is kept distinct from the address-conflict incident above; they are not assumed to be the same event.

## How I approach problems

- **Evidence first:** counters, file hashes, and packet captures help locate where behavior diverges.
- **Validate on hardware:** byte-level comparisons check actual outputs against simulation.
- **Specifications before code:** rules, message formats, and failure handling become shared, checkable references.
- **Stop when state is uncertain:** retain evidence and reconcile before recovery.

Figures come from the project summary supplied for this portfolio; company raw test records are not included in the public repository. Source code, actual orders, IP addresses, and internal partner documents remain private. The system serves as a foundation for follow-on work and is not yet in production.

[Back to the portfolio](../README.en.md)
