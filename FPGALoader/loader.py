import os, subprocess, sys
import tkinter.filedialog as fdialog

if __name__ == "__main__":

# specify path to xproject    
    xpath = 'xc3sprog/xc3sprog';
#specify starting path in file dialog
    ppath = '/home/';

#running as root?
    if not os.geteuid()==0:
       sys.exit("\nYou must be root to run this application, please    use sudo and try again.\n")  

# Choose bitfile, change ('bitsream', '*.bit") if you want to use other files
    bitfile = fdialog.askopenfilename(filetypes = [('Bistream', '*.bit')], title="Open Bitstream", initialdir=(os.path.expanduser(ppath) ) )
    print("loaded file: " + bitfile)

#Setup command and run it
    args = [xpath, '-c', 'ftdi', '-v', bitfile]
    print("Command: " +  args[0] + " " + args[1] + " " +  args[2] + " " + args[3] + " " +  args[4])
    p = subprocess.Popen(args)
    #print errors
    print("errors:\n");    
    output, error = p.communicate()
    print(output)    
