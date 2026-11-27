# Team tools | Reproduce problems and reduce missed checks

[繁體中文](testing-tools.md)　／　**English**

Colleagues come to me when they are unsure how to move a project problem forward. Some of those problems are worth solving with a small tool so that a one-time solution can be reused by a team.

## Virtual exchange

**Users: the risk-control system development team.**

### Before

Testing relied on manual operation, many special cases were difficult to cover, and events that had happened in the real environment were hard to recreate.

### What I built

- Script-defined special scenarios that the team can author themselves.
- Automated stress testing.
- Import of actual logs to reproduce past incidents.

### What changed

The team can describe difficult scenarios in scripts and revisit real events through logs. The value is a more reproducible set of test conditions and a clearer basis for investigation.

## Logger Monitor

**Users: multiple teams in the IT department.**

### Before

Teams checked logs manually, leaving room for issues to be missed.

### Checks and notifications

1. Confirm that the expected file exists.
2. Look for error-related keywords such as ERROR, termination-related messages, and catch.
3. Let teams adjust checks through INI configuration.
4. Notify through LINE and Telegram Bot APIs when a problem is found.

### What changed

Some repeatable checks move out of manual inspection and into configurable tooling, reducing manual work and the risk of omissions across different teams.

## Technology and disclosure

The two tools use technologies including Python and Node.js. Their individual language assignments have not been separately specified.

No claims are made about zero missed alerts, exact hours saved, or unreported stress-test throughput. Company code, real transaction logs, machine configurations, and internal notification content remain private.

[Back to the portfolio](../README.en.md)
