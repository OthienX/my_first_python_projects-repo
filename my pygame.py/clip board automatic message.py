Text = {'agree': """it sound fine and am fine with it""",
        'busy':"""we do this later the week or next week""",
        'upsell':"""consider making this a monthy donation"""}
import sys, pyperclip
if len(sys.argv)<2:
        print('usage: py mclip.py;[key_pharse], copy pharse text')
        sys.exist()
        keypharse =sys.argv[1] # first comand line arge to tyhe key pharse
if keypharse in TEXT:
        pyperclip.copy(TEXT[keypharse])
        print('text for'+ keypharse+'copied to the clipboard')
else:
        print('there is no text for the '+ keypharse)