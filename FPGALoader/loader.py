import os, subprocess, sys
import tkinter.filedialog as fdialog

if __name__ == "__main__":
    
    xpath = 'xc3sprog/xc3sprog';
    ppath = '~/projects';
    if not os.geteuid()==0:
       sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")  
        
    bitfile = fdialog.askopenfilename(filetypes = [('Bistream', '*.bit')], title="Open Bitstream", initialdir=(os.path.expanduser(ppath) ) )
    print("loaded file: " + bitfile)
    args = [xpath, '-c', 'ftdi', '-v', bitfile]
    print("Command: " +  args[0] + " " + args[1] + " " +  args[2] + " " + args[3] + " " +  args[4])
    p = subprocess.Popen(args)    
    output, error = p.communicate()
    print(output)    
