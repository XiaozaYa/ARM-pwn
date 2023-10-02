.section .text
.globl _start
#.set noreorder

_start:
	mov r0, pc
	mov r1, #16
	mov r0, r1	

	mvn r0, #1
	
	add r0, r1
	add r0, r1, #10
	add r2, r1, r1
	add r3, r0, #30
	movle r3, #20	
	mov r4, r1, LSL #2
	bkpt
