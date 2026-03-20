# Linux Kernel Observer

Experimental tool to observe Linux kernel runtime signals using `/proc`.

Features

- Kernel version inspection
- CPU core activity
- Memory state monitoring
- System load analysis
- Process inspection

Goal: explore how the Linux kernel exposes runtime telemetry to userspace.

Inspired by the work of @torvalds and the Linux kernel community.
## Assembly Kernel Syscall Demo

This program demonstrates how Linux system calls work directly from
x86_64 assembly without libc.

It uses the syscall interface to:

- write to stdout
- retrieve process id
- exit the program
