# 2021 April IOP Introduction To C++ Part1

Instructions tested on Ubuntu, compatability with MacOS likely to be good. On windows I would recommend install the Windows Linux Subsystem (WSL)

To build, we can use cmake:

```
cmake .
make
```
To run:
```
./simulation.exe
```
To animate, we need to have saved the output of the simulation

```
./simulation.exe > extras/File.txt
cd extras
python3 AnimateFigure.py
```
