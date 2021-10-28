# STOCK INVESTMENT ANALYZER

Computes the best investments you can make !

## setup

First clone the repo :
```bash
git clone https://github.com/BNNJ/Project7
```
or with gh CLI:
```bash
gh repo clone BNNJ/Project7
```

Then go into the directory and make a virtual environment:
```bash
cd Project7
python3 -m venv .
```

Source the environment script:
| Platform    | Shell             | Command to activate virtual environment |
| ------------|-------------------|---------------------------------------- |
| POSIX       | bash/zsh          | `$ source ./bin/activate`               |
|             | fish              | `$ source ./bin/activate.fish`          |
|             | csh/tcsh          | `$ source ./bin/activate.csh`           |
|             | PowerShell Core   | `$ ./bin/Activate.ps1`                  |
| Windows     | cmd.exe           | `C:\> .\Scripts\activate.bat`           |
|             | PowerShell        | `PS C:\> .\Scripts\Activate.ps1`        |

now install required modules:
```bash
pip install -r requirements.txt
```

## usage

```bash
$ ./optimized.py [-h] [-m X] [-g] [-a] input
```

```bash
$ ./bruteforce [-h] input
```

| arg        | effect|
|------------|-------|
| -h         | Displays the help |
| -m --max X | Use X as the maximum cost (default=500) |
| --greedy   | Use a greedy algorithm instead of branch and bound |
| input      | The dataset to use in .csv format |