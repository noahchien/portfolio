# Team tools: virtual exchange and Logger Monitor

[繁體中文](testing-tools.md)　／　**English**

Colleagues often bring me problems they're stuck on. Some of them can be solved with a small tool that the whole team keeps using.

## Virtual exchange

**Users: the risk-control system development team.**

### Before

Testing relied on manual operation, many special cases were difficult to cover, and events that had happened in the real environment were hard to recreate.

### What I built

- Script-defined special scenarios that the team can author themselves.
- Automated stress testing.
- Import of actual logs to reproduce past incidents.

### What changed

Scenarios that can't be produced by hand are now a script away, and production incidents can be replayed from logs and examined at leisure.

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

Checks that used to be done by hand now run automatically, each team with its own settings, so fewer problems slip through.

## Technology and disclosure

Both tools are written in Python and Node.js. Company code, transaction logs, and internal settings are not published.

[Back to the portfolio](../README.en.md)
