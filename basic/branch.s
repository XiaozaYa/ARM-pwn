.section .text
.global _start

_start:
	.code 32
	add r2, pc, #1
	bx r2
	
	

	.code 16
	mov r0, #1
