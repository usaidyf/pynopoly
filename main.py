import subprocess

def main():
   width = 160
   height = 45
   subprocess.Popen(f'start /wait cmd /k "mode con: cols={width} lines={height} && python game.py"', shell=True)
   

if __name__ == "__main__":
   main()