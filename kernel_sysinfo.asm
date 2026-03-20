section .data
    msg db "Linux Kernel Syscall Demo (Assembly)",10
    msglen equ $-msg

section .text
    global _start

_start:

    ; write message to stdout
    mov rax,1
    mov rdi,1
    mov rsi,msg
    mov rdx,msglen
    syscall

    ; get process id
    mov rax,39
    syscall

    ; exit
    mov rax,60
    xor rdi,rdi
    syscall
