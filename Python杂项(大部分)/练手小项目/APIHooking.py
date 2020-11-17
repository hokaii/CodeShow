import utils, sys
from pydbg import *
from pydbg import dbg

'''
BOOL WINAPI WriteFile(
    _In_    HANDLE hFile,
    _In_    LPCVOID lpBuffer,
    _In_    DWORD nNumberOfBytesTowrite,
    _Out_opt_   LPDWORD lpNumberOfBytesToWritten,
    _Inout_opt_ LPOVERLAPPED lpOverlapped
);
'''
dbg = dbg()
isProcess = False

orgPattern = "love"
repPattern = "hate"
isProcessName = "notepad.exe"

def replaceString(dbg, args):
    buffer = dbg.read_process_memory(args[1], args[2])

    if orgPattern in buffer:
        print("[APIHooking] Before : %s" % buffer)
        buffer = buffer.replace(orgPattern, repPattern)
        replace = dbg.write_process_memory(args[1], buffer)
        print("[APIHooking] After : %s" % dbg.read_process_memory(args[1], args[2]))

    return DBG_CONTINUE
