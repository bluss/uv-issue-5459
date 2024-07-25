
Steps to reproduce:

```bash
cd foo
uv run -v i_am_foo.py ../cd_to.sh ../bar uv run -v i_am_bar.py
```

End of the output:

```
DEBUG Using Python 3.12.3 interpreter at: /home/user/uv-issue-5459/bar/.venv/bin/python3
DEBUG Running `python i_am_bar.py`
What? I thought I was isolated.. nooo
This is my sys path:
/home/user/uv-issue-5459/bar
/home/user/uv-issue-5459/bar/.venv/lib/python3.12/site-packages
/home/user/uv-issue-5459/foo/.venv/lib/python3.12/site-packages
/home/user/.local/share/uv/python/cpython-3.12.3-linux-x86_64-gnu/lib/python312.zip
/home/user/.local/share/uv/python/cpython-3.12.3-linux-x86_64-gnu/lib/python3.12
/home/user/.local/share/uv/python/cpython-3.12.3-linux-x86_64-gnu/lib/python3.12/lib-dynload
/home/user/uv-issue-5459/bar/src
```


The equivalent Rye command line is

```bash
rye run python i_am_foo.py ../cd_to.sh ../bar rye run python i_am_bar.py
```

And the output says among other things:

```
Pass, all is good
This is my sys path:
/home/user/uv-issue-5459/bar
/home/user/.local/share/uv/python/cpython-3.12.3-linux-x86_64-gnu/lib/python312.zip
/home/user/.local/share/uv/python/cpython-3.12.3-linux-x86_64-gnu/lib/python3.12
/home/user/.local/share/uv/python/cpython-3.12.3-linux-x86_64-gnu/lib/python3.12/lib-dynload
/home/user/uv-issue-5459/bar/.venv/lib/python3.12/site-packages
/home/user/uv-issue-5459/bar/src
```

