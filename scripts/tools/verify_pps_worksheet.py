import json,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
TEMP=tempfile.TemporaryDirectory()
WORK=Path(TEMP.name)
from pathlib import Path
bank=json.loads((ROOT/'college/1-1/programming-problem-solving/worksheets/worksheet-1.json').read_text())
for q in bank['problems']:
 exe=str(WORK/q['number']);Path(exe+'.c').write_text(q['code']);subprocess.run(['cc','-std=c11','-Wall','-Wextra','-Werror',exe+'.c','-lm','-o',exe],check=True)
 p=subprocess.run([exe],input=q['test_input'],capture_output=True,text=True,timeout=3)
 assert p.returncode==0,(q['number'],p.stdout,p.stderr)
 assert q['expected']in p.stdout,(q['number'],q['expected'],p.stdout)
print('30/30 C11 programs compile warning-free and pass example tests.')
# Cases that commonly expose incorrect beginner solutions.
cases={'1a':[('4 2 0\n','Cannot divide by zero.',1)],'1b':[('0\n','Armstrong',0),('154\n','Not Armstrong',0)],'2b':[('0\n','Palindrome',0),('120\n','Not palindrome',0)],'2c':[('1 2 1\n','Repeated root: -1',0),('1 0 1\n','Complex roots:',0),('0 2 -6\n','Linear root: 3',0)],'3a':[('0\n','0 ',0)],'3c':[('1 2 3 1\n','Incompatible',1)],'5a':[('1\n','Not perfect',0)],'5b':[('3 3 1 2\n','sorted',1),('3 1 2 3 9\n','Not found',0)],'6a':[('0\n','Not prime',0),('1\n','Not prime',0),('2\n','Prime',0),('49\n','Not prime',0)],'8a':[('0\n','Factorial: 1',0),('20\n','2432902008176640000',0)],'9c':[('\n','Copy: ',0)],'10c':[('0\n','Reverse: 0',0)]}
n=0
for id,tests in cases.items():
 for input,expected,code in tests:
  p=subprocess.run([str(WORK/id)],input=input,capture_output=True,text=True,timeout=3);assert p.returncode==code and expected in p.stdout,(id,p.stdout);n+=1
print(n,'additional boundary/error cases PASS')
