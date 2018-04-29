# saythanks-cli

Say Thanks via CLI!

Do you know about @kennethreitz's [saythanks.io](https://saythanks.io) project?
It's awesome and you should use it more often!

... And that's exactly why this little CLI tool exists:

Use it to conviniently *say thanks* to other people without leaving the terminal! :tada:

```bash
python3 -m pip install saythanks-cli
```

Say thanks:

```bash
echo 'Request is soo great! Thanks.' | thx kennethreitz
```

If you don't pipe anything into `thx` it'll pull up your favorite text editor
and you can enter your message there. Just save and the message will be sent!
