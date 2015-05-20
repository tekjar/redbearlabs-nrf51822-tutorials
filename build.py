import os
import subprocess
import argparse
import sys
import textwrap

SDK_PATH = '/Users/ravitejareddy/Desktop/nrf51822_development/nRF51_SDK_8.1.0_b6ed55f/'

s110 = SDK_PATH + 'components/softdevice/s110/hex/s110_softdevice.hex'
s120 = SDK_PATH + 'components/softdevice/s120/hex/s120_softdevice.hex'
s130 = SDK_PATH + 'components/softdevice/s130/hex/s130_softdevice.hex'

#srec_cat ~/Desktop/nrf51822_development/s110_nrf51_8.0.0/s110_nrf51_8.0.0_softdevice.hex -intel /Users/ravitejareddy/Google\ Drive/nrf51822_development/nRF51_SDK_8.1.0_b6ed55f/examples/ble_peripheral/ble_app_beacon/pca10028/s110/armgcc/_build/nrf51422_xxac_s110.hex  -intel -o beaconfull.hex -intel --line-length=44

#parse commandline arguments and options
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
                    Usage Examples
            --------------------------------
            python build.py xml> -s s110 examples/ble_peripheral/ble_app_beacon -o beaconfull.hex


            NOTE: Defaults --> softdevice:s110, outputfilename:outputfull.hex '''))


parser.add_argument('-s', '--softdevice', dest="softdevice", default= "s110", help="Softdevice version")
parser.add_argument('-o', '--output', dest="output", default= "outputfull.hex", help="Output file name")
parser.add_argument('project_name', nargs=1, help='Name of the project whose make you want to invoke')
args = parser.parse_args()

softdevice = args.softdevice


app_hex_path = SDK_PATH + args.project_name[0] + '/pca10028/' + args.softdevice + '/armgcc/_build/nrf51422_xxac_' + args.softdevice + '.hex'
makefile_path = SDK_PATH + args.project_name[0] + '/pca10028/' + args.softdevice + '/armgcc/'

if args.softdevice == 's110':
    softdevice = s110
elif args.softdevice == 's120':
    softdevice = s120
elif args.softdevice == 's130':
    softdevice = s130


make_command = ('make', '-C', makefile_path)


merge_command = ('srec_cat', softdevice, '-intel', app_hex_path, '-intel', '-o', args.output, '-intel',  '--line-length=44')

try:
    print('making' + makefile_path)
    make_popen = subprocess.Popen(make_command, stdout=subprocess.PIPE)
    make_popen.wait()
    print(make_popen.stdout.read())

    print('merging' + softdevice + 'and' + app_hex_path)
    merge_popen = subprocess.Popen(merge_command, stdout=subprocess.PIPE)
    merge_popen.wait()
    print(merge_popen.stdout.read())
except:
    print("Unable to execute commands")

#print("the commandline is {}".format(merge_popen.args))
