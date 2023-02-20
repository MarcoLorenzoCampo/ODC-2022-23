'''

undefined8 main(void)

{
  int iVar1;
  char *strndupped;
  long in_FS_OFFSET;
  int index;
  char buf [40];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  fgets(buf,0x20,stdin);
  strndupped = strndup(buf,0x1f);


	//focus here
  for (index = 0; index < 31; index = index + 1) {
    strndupped[index] = (char)((strndupped[index] + 0x73) / 2);
  }


	//focus here
  iVar1 = strncmp(strndupped,s__\_`bl[\ct\FgatHt]ct]F]oulmtDFe_00104060,0x20);
  if (iVar1 == 0) {
    puts("thats correct fella hackerz!");
  }


  else {
    puts("git gud");
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}



This function returns a pointer to a null-terminated byte string, which is a duplicate of the string pointed to by buf
it gets transposed by line 19

on gdb go to strcmp and check how every character is mapped, trial and error because of overlapping mappings
check the output iVar1 with strncpm and reverse engineer the flag

put it on ncat...