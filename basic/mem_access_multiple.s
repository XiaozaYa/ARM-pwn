.section .text
.global _start

_start:
	ldm sp, {r0-r3}
	ldm sp, {r4, r6}

	ldr r0, =3
	ldr r1, =4
	ldr r2, =5
	ldr r3, =6
	ldr r4, =7
	ldr r5, =8
	ldr r6, =9
	stm sp, {r0-r6}

	ldr r0, =0
	ldr r1, =0
	ldr r2, =0
	ldr r3, =0
	ldr r4, =0
	ldr r5, =0
	ldr r6, =0

	ldmib sp, {r0-r3}	
	
	add sp, #12
	ldmda sp!, {r0-r3}

	push {r0, r1}
	pop {r3, r4}

	bkpt	
