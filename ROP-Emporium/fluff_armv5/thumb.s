.section .text
.global _start

_start:

	.code 32
	ldr r1, =0x12345678
	str r1, [sp]
	pop {r2}
	add r3, pc, #1
	bx r3

	.code 16
	str r1, [sp, #4]

	bkpt
	
