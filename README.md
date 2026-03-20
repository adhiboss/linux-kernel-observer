# Linux Kernel Observer

Experimental tool to observe Linux kernel runtime signals using `/proc`.

Features

- Kernel version inspection
- CPU core activity
- Memory state monitoring
- System load analysis
- Process inspection

Goal: explore how the Linux kernel exposes runtime telemetry to userspace.

## Assembly Kernel Syscall Demo

This program demonstrates how Linux system calls work directly from
x86_64 assembly without libc.

It uses the syscall interface to:

- write to stdout
- retrieve process id
- exit the program
Inspired by the work of @torvalds and the Linux kernel community.
This project explores ideas inspired by the Linux kernel.

Reference:
https://github.com/torvalds/linux
## Kernel Telemetry Tool

A low-level C program that reads Linux kernel telemetry directly from `/proc`.

Features

- Kernel version inspection
- System load analysis
- Memory statistics
- Direct interaction with kernel telemetry interfaces
## Kernel Time-Travel Recorder

Experimental tool that records system runtime snapshots so kernel
behavior can be replayed later for analysis.

Features:
- CPU core state history
- memory usage timeline
- process activity tracking
- time-series system replay
