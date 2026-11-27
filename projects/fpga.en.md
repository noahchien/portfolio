# FPGA project | Reorganizing development and quality ownership

[繁體中文](fpga.md)　／　**English**

## At a glance

| Area | Summary |
| --- | --- |
| Challenge | A specialized, logic-circuit-oriented domain; staffing fell from three people to one |
| My responsibilities | Planning, development, progress tracking, code review, validation approach, and quality decisions |
| Collaboration | Initially developed the code myself; later used AI for most implementation while retaining judgment and review |
| Outcome | Completed development more than a year ahead of the original estimated development schedule |
| Current status | Not yet in production; serving as a foundation for a follow-on project |

## The problem behind the implementation

After staffing was reduced, moving every existing task onto one person without changing the workflow was not enough. I needed to reconsider the balance between implementation and planning while keeping control of technical direction and quality.

I used AI for most code implementation while taking responsibility for reading the code, checking direction, choosing validation methods, and deciding how to adjust the work.

## A concrete example of engineering judgment

The AI did not automatically know the actual machine configuration. In one instance, it assumed a single network interface when there were two, leading to an incorrect understanding of the network setup.

I checked the physical environment, supplied the missing information, and worked with the AI to correct the premise and implementation. This required both domain understanding and knowledge of the actual environment to distinguish a logic problem from an incorrect assumption about the machine.

## How I think about validation

Start by understanding what the system is supposed to achieve, then decide how to verify the output. A plausible explanation of the code cannot replace checking whether actual results meet the requirements.

My responsibilities included defining the validation approach, reviewing output, supplying correct environmental information, and judging results against the intended goal.

## What the outcome means

The schedule improvement compares completed development with the original estimated development schedule. The project has not launched into production and is currently a base for the next project. No unreported performance metrics or production outcomes are claimed.

This case illustrates resource planning, AI collaboration, on-site judgment, and quality ownership. Company source code, IP addresses, hardware models, and internal architecture remain private.

[Back to the portfolio](../README.en.md)
