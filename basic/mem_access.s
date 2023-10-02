.data
	var1: .word 3
	var2: .word 4

.text
.global _start

_start:
	mov r0, #10
	str r0, [sp]
	ldr r2, [sp]
	str r2, [sp, #2]
	str r0, [sp, #4]!
	str r3, [sp], #4
	mov r3, #4
	ldr r0, [sp, r3]
	mov r3, #2
	ldr r0, [sp, r3, lsl#2]
	mov r0, #511
	bkpt

