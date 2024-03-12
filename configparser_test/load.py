import sys
import configparser

if len(sys.argv) < 2:
    print("arg error")

cfg = configparser.ConfigParser()
cfg.read(sys.argv[1])
print(cfg.sections())
for sec in cfg.keys():
    print(sec)
    for key, value in cfg[sec].items():
        print(f"\t{key}({type(value)}):{value}")